import datetime
import os
import re
import sys
import tempfile

import cd_cli.models as models
from cd_cli.utils import get_colored_logger

logger = get_colored_logger(__name__)

PRIMITIVE_TYPES = (float, bool, bytes, str, int)
NATIVE_TYPES_MAPPING = {
    "int": int,
    "long": int,
    "float": float,
    "str": str,
    "bool": bool,
    "date": datetime.date,
    "datetime": datetime.datetime,
    "object": object,
}


def deserialize(response, response_type):
    """Deserializes response into an object.

    :param response: RESTResponse object to be deserialized.
    :param response_type: class literal for
        deserialized object, or string of class name.

    :return: deserialized object.
    """
    # handle file downloading
    # save response body into a tmp file and return the instance
    if response_type == "file":
        return __deserialize_file(response)

    # fetch data from response object
    try:
        data = response.json()
    except AttributeError:
        data = response

    return __deserialize(data, response_type)


def __deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if isinstance(klass, str):
        if klass.startswith("list["):
            sub_kls = re.match(r"list\[(.*)\]", klass).group(1)
            return [__deserialize(sub_data, sub_kls) for sub_data in data]

        if klass.startswith("dict("):
            sub_kls = re.match(r"dict\(([^,]*), (.*)\)", klass).group(2)
            return {k: __deserialize(v, sub_kls) for k, v in iter(data.items())}

        # convert str to class
        if klass in NATIVE_TYPES_MAPPING:
            klass = NATIVE_TYPES_MAPPING[klass]
        else:
            klass = getattr(models, klass)

    if klass in PRIMITIVE_TYPES:
        return __deserialize_primitive(data, klass)
    elif klass == object:
        return __deserialize_object(data)
    elif klass == datetime.date:
        return __deserialize_date(data)
    elif klass == datetime.datetime:
        return __deserialize_datatime(data)
    else:
        return __deserialize_model(data, klass)


def __deserialize_file(response):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    :param response:  RESTResponse.
    :return: file path.
    """

    fd, path = tempfile.mkstemp()
    os.close(fd)
    os.remove(path)

    content_disposition = response.getheader("Content-Disposition")
    if content_disposition:
        filename = re.search(
            r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition
        ).group(1)
        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(response.data)

    return path


def __deserialize_primitive(data, klass):
    """Deserializes string to primitive type.

    :param data: str.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    """
    try:
        return klass(data)
    except UnicodeEncodeError:
        return str(data)
    except TypeError:
        return data


def __deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def __deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :return: date.
    """
    try:
        return datetime.datetime.fromisoformat(string).date()
    except ImportError:
        return string
    except ValueError:
        logger.critical('Failed to parse "%s" as date object.', string, exc_info=False)
        sys.exit()


def __deserialize_datatime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :return: datetime.
    """
    try:
        return datetime.datetime.fromisoformat(string).date()
    except ImportError:
        return string
    except ValueError:
        logger.critical(
            'Failed to parse "%s" as datetime object.', string, exc_info=False
        )
        sys.exit()


def __hasattr(obj, name):
    return name in obj.__class__.__dict__


def __deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :param klass: class literal.
    :return: model object.
    """

    if not klass.attribute_types and not __hasattr(klass, "get_real_child_model"):
        return data

    kwargs = {}
    if klass.attribute_types is not None:
        for attr, attr_type in iter(klass.attribute_types.items()):
            if (
                data is not None
                and klass.attribute_map[attr] in data
                and isinstance(data, (list, dict))
            ):
                value = data[klass.attribute_map[attr]]
                kwargs[attr] = __deserialize(value, attr_type)

    instance = klass(**kwargs)

    if (
        isinstance(instance, dict)
        and klass.attribute_types is not None
        and isinstance(data, dict)
    ):
        for key, value in data.items():
            if key not in klass.attribute_types:
                instance[key] = value
    if __hasattr(instance, "get_real_child_model"):
        klass_name = instance.get_real_child_model(data)
        if klass_name:
            instance = __deserialize(data, klass_name)
    return instance
