# Flask pypendency extension
Flask extension for [Pypendency](https://github.com/Feverup/pypendency). 
Pypendency is a dependency injection library for python 3.6+.

## Installation

## Integration with Flask

## Usage

#### Examples

## Contributing / Running project locally
Build the docker image:
```bash
docker build . -t pypendency-flask-dev
```

Run tests:
```bash
docker run -v $(pwd)/.:/usr pypendency-flask-dev bash -c "pipenv run make run-tests"
```
