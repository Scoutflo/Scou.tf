#!/usr/bin/env python3
import argparse
import json
from scoutf import ScoutfParser

def main():
    parser = argparse.ArgumentParser(description='Convert JSON to HCL or HCL to JSON using ScoutfloParser.')
    parser.add_argument('input_file', type=str, help='Path to the input file (JSON or HCL).')
    parser.add_argument('output_file', type=str, help='Path to the output file (HCL or JSON).')
    parser.add_argument('--to-hcl', action='store_true', help='Convert JSON to HCL.')
    parser.add_argument('--to-json', action='store_true', help='Convert HCL to JSON.')

    args = parser.parse_args()

    scoutflo_parser = ScoutfParser()

    if args.to_hcl:
        with open(args.input_file, 'r') as infile:
            input_content = infile.read()
        input_data = json.loads(input_content)
        output_content = scoutflo_parser.json_to_hcl(input_data)
        with open(args.output_file, 'w') as outfile:
            outfile.write(output_content)
    elif args.to_json:
        output_content = scoutflo_parser.hcl_to_json(args.input_file)
        with open(args.output_file, 'w') as outfile:
            outfile.write(json.dumps(output_content))
    else:
        raise ValueError('You must specify either --to-hcl or --to-json.')

    

if __name__ == "__main__":
    main()