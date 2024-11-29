# comdi-cli: command line access to comdirect

Comdi-cli is an implementation in Python to retrieve account information, transactions and documents via the comdirect REST API.

The program allows to retrieve account transactions and to download all PDF documents.

It is a hobby project that combines the pleasant with the useful. So I can learn a little Python and also retrieve account transactions including the mandate reference. (Unfortunately, the corresponding CSV export on the comdirect website does not include mandate references.)

Neither is it endorsed by comdirect or Commerzbank AG nor am I in any relationship with these companies.

Use at your own risk!

## Installation

Clone the repo and install e.g. with pip:

```sh
git clone https://github.com/ExploracuriousAlex/comdi-cli.git
cd comdi-cli
pip install .
```

## Usage

Run:

```sh
comdi-cli
```

If you put a 'credentials.json' file in the comdi-cli folder, comdi-cli will use the credentials from it for the login to your comdirect account.

The file format is:

```text
{
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}
```

Otherwise you will be asked to input the credentials.
You will also have the option to save your entered credantials as 'credentials.json' file.

The credentials are only sent to comdirect for authentication purposes. Never anywhere else!

## Further possible usages

```sh
comdi-cli tim
```

Will use credentials.json_tim as credentials file.

```sh
comdi-cli tim /my/own/folder
```

Will use credentials.json_tim as credentials file if and store the documents in /my/own/folder instead of output.
If the path does not exist, output will be used.

## Important notes

- Registration is required to use the API and, accordingly, this program!

  Please visit this website:
  
  [comdirect REST API | comdirect.de](https://www.comdirect.de/cms/kontakt-zugaenge-api.html)
  
- The implementation is prepared for different TAN procedures, but so far **only the authorization via push function of the photoTAN app has been tested!**
