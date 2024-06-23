# pdfutils

Just a Python API to get metadata from a pdf file. A while ago I created an npm package for the same purpose, but javascript doesn't have a comprehensible library.

The main purpose of this package is to provide information about the PDF document in Litterarum.

## Requirements

    Our main requirements are
    * Python 3.10
    * pypdf
    * fastapi

The other requirements are in requirements.txt.

## Development workflow

The project uses pipenv to manage package dependencies. So the dev workflow is just as follows:

* Makes available pip bin and packages installed in the system. Useful if you had used the install pip with get-pip.py script.
* Install from Pipfile.lock
* Prompt it to pipenv that active the virtualenv

```bash
source ./setup-pip.sh 
pipenv sync # install dependencies
pipenv shell # move forward to the virtualenv
```

For more information about pipenv go to <https://pipenv.pypa.io/en/latest/workflows.html>

### Docker build configuration

Since I'm still using the recommended fastapi build process for docker, every time that we install a new package we must run the following command to update the requirements.txt file.

```bash 
pip freeze > requirements.txt # inside the pipenv shell
```
