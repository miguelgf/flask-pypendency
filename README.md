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
Pypendency(app)
```

## Configuration

## Usage

#### Examples

## Contributing / Running project locally
Build the docker image:
```bash
docker build . -t flask-pypendency-dev
```

Run tests:
```bash
docker run -v $(pwd)/.:/usr/src/app flask-pypendency-dev bash -c "pipenv run make run-tests"
```
