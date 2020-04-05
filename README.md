![](https://github.com/miguelgf/flask-pypendency/workflows/Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/Flask-Pypendency.svg)](https://badge.fury.io/py/Flask-Pypendency)

# Flask pypendency extension
Flask extension for [Pypendency](https://github.com/Feverup/pypendency). 
Pypendency is a dependency injection library for python 3.6+.

## Installation
To install from source, download the source code, then run this:

```bash
python setup.py install
```

Or install with pip:
    
```bash
pip install Flask-Pypendency
```

## Integration with Flask
Adding the extension to your Flask app is simple:

```python
from flask import Flask
from flask_pypendency import Pypendency

app = Flask(__name__)
pypendency = Pypendency(app)
```

## Usage

Anywhere in your app, you will be able to access the container using the app

```python
from flask import current_app as app

@app.route('/hello')
def hello():
    service = pypendency.container.get('my.service')
    
    return service.say_hello()
```

## Configuration

The Flask App could be configure before the `init_app` of Flask-Pypendency, with the following parameteres:

##### `PYPENDENCY_DI_FOLDER_NAME`
> Specify the name of the folder containing the definitions of services, it should be the same across all
> the app (if more than one path is defined).
>
> Default: `_dependency_injection`

##### `PYPENDENCY_DISCOVER_PATHS`
> Iterable of absolute paths where to search for definitions of services
>
> Default: [Flask's app root path](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.root_path)

#### Examples
The file `test/test_flask_pypendency.py` has a end-to-end test that shows how the extension could
be used on a real Flask app.

## Contributing / Running project locally
Build the docker image:
```bash
docker build . -t flask-pypendency-dev
```

Run tests:
```bash
docker run -v $(pwd)/.:/usr/src/app flask-pypendency-dev bash -c "pipenv run make run-tests"
```
