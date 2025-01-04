import hcl2

class ScoutfParser:
    """
    A scoutflo utility to parse the hcl code to json and json code to hcl.
    """
    def json_to_hcl(self,data):
        """
        Convert the given JSON structure to HCL format.
        """
        hcl_output = []

        # Process provider block
        if 'provider' in data:
            for provider in data['provider']:
                for key, value in provider.items():
                    hcl_output.append(f"provider \"{key}\" {{")
                    for k, v in value.items():
                        hcl_output.append(f"  {k} = {self._hcl_value(v)}")
                    hcl_output.append("}\n")

        if 'data' in data:
            for data_block in data['data']:
                for key, value in data_block.items():
                    for sub_key, sub_value in value.items():
                        hcl_output.append(f"data \"{key}\" \"{sub_key}\" {{")
                        for k, v in sub_value.items():
                            if isinstance(v, list) and all(isinstance(i, dict) for i in v):
                                for item in v:
                                    hcl_output.append(f"  {k} {{")
                                    for item_key, item_value in item.items():
                                        hcl_output.append(f"    {item_key} = {self._hcl_value(item_value)}")
                                    hcl_output.append("  }")
                            else:
                                hcl_output.append(f"  {k} = {self._hcl_value(v)}")
                        hcl_output.append("}\n")

        # Process locals block
        if 'locals' in data:
            for local in data['locals']:
                for key, value in local.items():
                    hcl_output.append(f"locals {{")
                    hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                    hcl_output.append("}\n")

        if 'resource' in data:
            for resource in data['resource']:
                for resource_type, resource_value in resource.items():
                    for resource_name, resource_properties in resource_value.items():
                        hcl_output.append(f"resource \"{resource_type}\" \"{resource_name}\" {{")
                        for key, value in resource_properties.items():
                            hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                        hcl_output.append("}\n")

        # Process module block
        if 'module' in data:
            for module in data['module']:
                for module_name, module_value in module.items():
                    hcl_output.append(f"module \"{module_name}\" {{")
                    for key, value in module_value.items():
                        hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                    hcl_output.append("}\n")

        return "\n".join(hcl_output)



    def _hcl_value(self,value):
        """
        Converts a value into a proper HCL format. 
        """
        if isinstance(value, str):
            # If it's a string and contains "${", treat it as an expression
            if value.startswith("${") and value.endswith("}"):
                return value[2:-1]  # Remove the "${" and "}"
            # Otherwise, treat it as a string value (with quotes)
            return f"\"{value}\""
        
        elif isinstance(value, list):
            # If it's a list, convert it to an HCL list format
            return "[\n" + ",\n ".join([self._hcl_value(v) for v in value]) + "]\n"
        
        elif isinstance(value, dict):
            # If it's a dict, convert it to an HCL block
            return "{" + "\n".join([f"{k} = {self._hcl_value(v)}" for k, v in value.items()]) + "}\n"
            
        elif isinstance(value, bool):
            # If it's a boolean, convert it to HCL boolean format
            return "true" if value else "false"
        
        else:
            # For other types (int, bool, etc.), just return the value as is
            return str(value)
        
    def hcl_to_json(self,hcl_code_file):
        with open(hcl_code_file, 'r') as f:
            data = hcl2.load(f)

        return data

