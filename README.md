# poetry-demo
test
test
This is a template repository for Python projects that use Poetry for the dependency management.

For more detailed instructions, please refer to the [poetry's documention](https://python-poetry.org/docs/basic-usage/)

# Getting Started
Before started, ensure you have met the following requirements:
- Python 3.x installed
- Poetry installed (You can install poetry using  ```pip install poetry```)

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
Alternatively, you can initialize Poetry in an existing project:
```
poetry init
```
This will create a ```pyproject.toml``` file, where you can specify the dependencies your project requires.

For detailed information on specifying dependencies, you can visit the [poetry's dependency specification](https://python-poetry.org/docs/dependency-specification/).

## Installation
To install the defined dependencies in ```pyproject.toml``` for your project, just run
```
poetry install
```
It will create a ```poetry.lock``` file, which resolves and installs all dependencies that you listed in ```pyproject.toml```. 

 You should commit the ```poetry.lock``` file to your project repo so that all people working on the project are locked to the same versions of dependencies

Note that Poetry uses the exact versions listed in ```poetry.lock``` to ensure that the package versions are consistent for everyone working on the project.

## Update
To add new dependencies or update existing versions, modify your ```pyproject.toml``` file accordingly. After making changes, execute:
```
poetry update
```
This command updates the ```poetry.lock```, fetching the latest compatible versions as specified in your pyproject.toml, and ensures the lock file reflects these new versions.

## Usage
Here's a quick example of how to run a script using Poetry:
```
poetry run python your_script.py
```

# Example
Here's the example demo to run the project.

First, install the required dependencies:
```
poetry install
```
Next, execute the demo script:
```
poetry run python demo/demo.py
```

