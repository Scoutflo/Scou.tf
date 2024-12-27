# Scoutf

Scoutf is a utility tool designed by scoutflo.com to parse HCL (HashiCorp Configuration Language) code to JSON and vice versa. This tool is particularly useful for managing and converting infrastructure as code configurations.

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

```python
from scoutf import ScoutfParser

def main():
    content = {
        'provider': [{'aws': {'region': 'var.region'}}],
        'data': [{'aws_availability_zones': {'available': {'filter': [{'name': 'opt-in-status', 'values': ['opt-in-not-required']}]}}}],
        'locals': [{'cluster_name': 'var.cluster_name'}],
        'resource': [{'aws_eks_addon': {'ebs-csi': {'cluster_name': '${module.eks.cluster_name}', 'addon_name': 'aws-ebs-csi-driver'}}}],
        'module': [{'vpc': {'source': 'terraform-aws-modules/vpc/aws', 'version': '3.19.0'}}]
    }
    
    scoutflo_parser = ScoutfParser()
    hcl_code = scoutflo_parser.json_to_hcl(content)
    print(hcl_code)

if __name__ == "__main__":
    main()
```

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more information.