import yaml

with open('uygulama_v1.yaml', 'r') as f:
    yaml_data = yaml.safe_load(f)

import xmltodict

xml_data = xmltodict.unparse({'root': yaml_data}, pretty=True)

with open('dosya.xml', 'w') as f:
    f.write(xml_data)

