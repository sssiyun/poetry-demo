# poetry-demo
This is a template repository for Python projects that use Poetry for the dependency management.

To get more detailed instruction, you could refer to [poetry's documention](https://python-poetry.org/docs/basic-usage/)

# Getting Started
Before started, ensure you have met the following requirements:
- Python 3.x installed
- Poetry installed (You could install poetry by  ```pip install poetry```)

## Initiation
To create a new project:
```
poetry new Your-Project-Name
```
This will create the project directory with the following content:
```
Your-Project-Name
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```
Or you could initiate into a pre-existing project
```
poetry init
```
It will create a ```pyproject.toml``` file that you could add the dependencies you needed.

For more specification of the dependency, you could visit [poetry's dependency specification](https://python-poetry.org/docs/dependency-specification/).

## Installation
To install the defined dependencies in ```pyproject.toml``` for your project, just run
```
poetry install
```
It will create a ```poetry.lock``` file, which resolves and installs all dependencies that you listed in ```pyproject.toml```. 

 You should commit the ```poetry.lock``` file to your project repo so that all people working on the project are locked to the same versions of dependencies

Note that Poetry uses the exact versions listed in ```poetry.lock``` to ensure that the package versions are consistent for everyone working on the project.

## Update
If you need to add new dependencies or modify their version, you'll need to go to ```pyproject.toml``` for the modification. Then you need to run
```
poetry update
```
to update ```poetry.lock```

This will fetch the latest matching versions (according to your ```pyproject.toml``` ) and update the lock file with the new versions.

## Usage
Here's a quick example of how to run a script using Poetry:
```
poetry run python your_script.py
```

# Example
Here's the example demo to run the project.

Firstly, install dependencies
```
poetry install
```
Then run the demo script
```
poetry run python demo/demo.py
```

