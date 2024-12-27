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
                    hcl_output.append("}")

        # Process data block
        if 'data' in data:
            for data_block in data['data']:
                for key, value in data_block.items():
                    hcl_output.append(f"data \"{key}\" {{")
                    for k, v in value.items():
                        hcl_output.append(f"  {k} = {self._hcl_value(v)}")
                    hcl_output.append("}")

        # Process locals block
        if 'locals' in data:
            for local in data['locals']:
                for key, value in local.items():
                    hcl_output.append(f"locals {{")
                    hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                    hcl_output.append("}")

        # Process resource block
        if 'resource' in data:
            for resource in data['resource']:
                for resource_type, resource_value in resource.items():
                    hcl_output.append(f"resource \"{resource_type}\" {{")
                    for key, value in resource_value.items():
                        hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                    hcl_output.append("}")

        # Process module block
        if 'module' in data:
            for module in data['module']:
                for module_name, module_value in module.items():
                    hcl_output.append(f"module \"{module_name}\" {{")
                    for key, value in module_value.items():
                        hcl_output.append(f"  {key} = {self._hcl_value(value)}")
                    hcl_output.append("}")

        return "\n".join(hcl_output)



    def _hcl_value(self,value):
        """
        Converts a value into a proper HCL format. 
        """
        if isinstance(value, str):
            # If it's a string and contains "${", treat it as an expression
            if value.startswith("${") and value.endswith("}"):
                return value
            # Otherwise, treat it as a string value (with quotes)
            return f"\"{value}\""
        
        elif isinstance(value, list):
            # If it's a list, convert it to an HCL list format
            return "[" + ", ".join([self._hcl_value(v) for v in value]) + "]"
        
        elif isinstance(value, dict):
            # If it's a dict, convert it to an HCL block
            return "{" + "\n".join([f"{k} = {self._hcl_value(v)}" for k, v in value.items()]) + "}"
        
        else:
            # For other types (int, bool, etc.), just return the value as is
            return str(value)
        
    def hcl_to_json(self,hcl_code):
        data = hcl2.load(hcl_code)

        return data

