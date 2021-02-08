# API Testing

## Quickstart

### Deploy to a local environment

First step is to clone the code:

``` bash
    $ git clone https://github.com/edurmada/ApiTesting.git <folder_to_locate_project>
```

Install the required Python3 dependencies to run the tests included in **requirements.txt**. It is recommended to use a virtualenvironment: use virtualenv with the **-p python3** option or venv depending on your python install:

``` bash
    $ cd <folder_to_locate_project>
    $ virtualenv --python=python3 .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt
```

Finally, make sure the chromedriver provided in *libs/drivers* for your OS supports the Chrome version installed in your computer. To do so, use "tcrunner.py" and pass on the path to test. If you're running tests using Browserstack, provide the access token together with the correct configuration of OS & Browser in *tcrunner-default.json* (remember to set **LOCAL** to false). To Run tests under a specific path:

``` bash
    $ python tcrunner.py Tests/Functionality
```

Please reffer to the configuration section for further insight on how to custom configure the tool.

