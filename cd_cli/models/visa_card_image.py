import pprint


class VisaCardImage(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "visa_card_image_id": "str",
        "image_description": "str",
        "image_base_filename": "str",
    }

    attribute_map = {
        "visa_card_image_id": "visaCardImageId",
        "image_description": "imageDescription",
        "image_base_filename": "imageBaseFilename",
    }

    def __init__(
        self, visa_card_image_id=None, image_description=None, image_base_filename=None
    ):
        """VisaCardImage"""

        self._visa_card_image_id = None
        self._image_description = None
        self._image_base_filename = None

        if visa_card_image_id is not None:
            self.visa_card_image_id = visa_card_image_id
        if image_description is not None:
            self.image_description = image_description
        if image_base_filename is not None:
            self.image_base_filename = image_base_filename

    @property
    def visa_card_image_id(self):
        """Gets the visa_card_image_id of this VisaCardImage.

        Visa card image ID to be used in the application

        :return: The visa_card_image_id of this VisaCardImage.
        :rtype: str
        """
        return self._visa_card_image_id

    @visa_card_image_id.setter
    def visa_card_image_id(self, visa_card_image_id):
        """Sets the visa_card_image_id of this VisaCardImage.

        Visa card image ID to be used in the application

        :param visa_card_image_id: The visa_card_image_id of this VisaCardImage.
        :type: str
        """

        self._visa_card_image_id = visa_card_image_id

    @property
    def image_description(self):
        """Gets the image_description of this VisaCardImage.

        Description of the image

        :return: The image_description of this VisaCardImage.
        :rtype: str
        """
        return self._image_description

    @image_description.setter
    def image_description(self, image_description):
        """Sets the image_description of this VisaCardImage.

        Description of the image

        :param image_description: The image_description of this VisaCardImage.
        :type: str
        """

        self._image_description = image_description

    @property
    def image_base_filename(self):
        """Gets the image_base_filename of this VisaCardImage.

        Base filename for the files representing the image. The name has to be extended with a postfix indicating the resolution and file type, e.g. -1x.jpg. The resulting filename can be used to retrieve the image from the comdirect CMS

        :return: The image_base_filename of this VisaCardImage.
        :rtype: str
        """
        return self._image_base_filename

    @image_base_filename.setter
    def image_base_filename(self, image_base_filename):
        """Sets the image_base_filename of this VisaCardImage.

        Base filename for the files representing the image. The name has to be extended with a postfix indicating the resolution and file type, e.g. -1x.jpg. The resulting filename can be used to retrieve the image from the comdirect CMS

        :param image_base_filename: The image_base_filename of this VisaCardImage.
        :type: str
        """

        self._image_base_filename = image_base_filename

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in iter(self.attribute_types.items()):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(VisaCardImage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VisaCardImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VisaCardImage):
            return True

        return self.to_dict() != other.to_dict()
