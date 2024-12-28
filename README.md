# Scoutf

Scoutf is a utility tool designed by www.scoutflo.com to parse HCL (HashiCorp Configuration Language) code to JSON and vice versa. This tool is particularly useful for managing and converting infrastructure as code configurations.

## Features

- Convert JSON structures to HCL format.
- Convert HCL code to JSON format.

## Installation

To install the required dependencies, use [Poetry](https://python-poetry.org/):

```sh
poetry install
```

## Running Tests

To run tests, use the following command:

```sh
poetry run pytest
```

## Usage

### HCL To JSON
```python
poetry run scoutf/cli.py main.tf output.json --to-json
```

### JSON To HCL
```python
poetry run scoutf/cli.py input.json output.tf  --to-hcl
```

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more information.
