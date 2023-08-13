# flake8-github
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/maxkrivich/flake8-github/main.svg)](https://results.pre-commit.ci/latest/github/maxkrivich/flake8-github/main)
[![License](https://img.shields.io/pypi/l/flake8-github.svg)](https://github.com/maxkrivich/flake8-github/blob/main/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/flake8-github.svg)](https://pypi.org/project/flake8-github/)


> This extension seamlessly integrates with Flake8, providing clear and elegant error annotations directly on GitHub's interface, making it easier than ever to identify and address code issues during pull request reviews.

## Table of Contents

- [flake8-github](#flake8-github)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Local Development Setup](#local-development-setup)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

Prerequisites

- flake8 = ^6.0.0

You can install `flake8-github` using pip:

```sh
$ pip install flake8-github
```

## Usage
After installing the formatter, you can enable it in your Flake8 configuration. For example, in your `.flake8`, `setup.cfg` file:

```
[flake8]
format = github
```


Run Flake8 as usual to start using github formatter:

```sh
$ flake8 src/ --format=github
```


## Local Development Setup

To contribute to this project or develop the plugin further locally, follow these steps:

1. Clone the repository:
```sh
$ git clone <https://github.com/your-username/flake8-github.git>
$ cd flake8-github
```

2. Create a virtual environment and install development dependencies:

```sh
$ pip install pre-commit poetry
$ pre-commit install
$ poetry install
```

3. How to bumpversion when you are done with the changes:
```sh
$ poetry self add poetry-bumpversion
$ poetry version {major, minor, patch, etc.}
```

Now you're ready to make changes and test your plugin locally.


## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a feature branch (git checkout -b feature/my-feature).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature/my-feature).
5. Create a new Pull Request.

Please ensure your code adheres to the project's coding standards and includes tests.


## License

This project is licensed under MIT License - see the [LICENSE](https://github.com/maxkrivich/flake8-github/blob/master/LICENSE) file for details.
