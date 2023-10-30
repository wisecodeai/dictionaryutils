"""
This script dumps all schema files in currently installed gdcdictionary
to one json schema to ./artifacts folder.

"""
import json
import os

#from gdcdictionary import SCHEMA_DIR
from dictionaryutils import dump_schemas_from_dir


def order_array_by_array(schema, ordered_array):
    ordered = {}
    for key in ordered_array:
        if key in schema:
            ordered[key] = schema[key]
        else:
            print("ERROR: Missing key " + key)
    return ordered


try:
    os.mkdir("artifacts")
except OSError:
    pass

shema_path = "../../gdcdictionary/schemas/PROD"
node_order = ["food.yaml", "ingredient.yaml", "nfp.yaml", "nfp_plus.yaml", "code.yaml"]

# Order nodes
yaml_schemas = dump_schemas_from_dir(shema_path)
ordered_schema_tmp = {k: v for k,
                           v in yaml_schemas.items() if k in node_order}
ordered_schema = order_array_by_array(ordered_schema_tmp, node_order)

everything_else = {k: v for k,
                           v in yaml_schemas.items() if k not in node_order}

yaml_schemas = {**everything_else, **ordered_schema}


# Save files
# with open(os.path.join("artifacts", "schema.json"), "w", encoding='utf-8') as f:
with open(os.path.join("artifacts", "schema.json"), "w") as f:
    json.dump(yaml_schemas, f)






