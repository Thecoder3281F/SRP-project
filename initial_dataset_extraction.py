# import requirements
from ord_schema.message_helpers import load_message, write_message
from ord_schema.proto import dataset_pb2

# load the binary ord file

# from https://github.com/open-reaction-database/ord-data/blob/main/data/5c/ord_dataset-5c9a10329a8a48968d18879a48bb8ab2.pb.gz
# https://open-reaction-database.org/dataset/ord_dataset-5c9a10329a8a48968d18879a48bb8ab2



dataset = load_message("chanlamcoupling.pb.gz", dataset_pb2.Dataset)
# save the ord file as human readable text
write_message(dataset, "chanlamcoupling.pbtxt")
print("Saved dataset to pbtxt file")

# import requirements
import json

from ord_schema.message_helpers import load_message, write_message
from ord_schema.proto import dataset_pb2
from google.protobuf.json_format import MessageToJson

input_fname = "chanlamcoupling.pb.gz"
dataset = load_message(
    input_fname,
    dataset_pb2.Dataset,
)

all_reactions = []

for rxn in dataset.reactions:
    rxn_json = json.loads(
        MessageToJson(
            message=rxn,
            including_default_value_fields=False,
            preserving_proto_field_name=True,
            indent=None,  # no internal indentation, for speed
            sort_keys=False,
            use_integers_for_enums=False,
            ensure_ascii=False,
        )
    )
    all_reactions.append(rxn_json)

# Save all reactions in a single JSON file
with open("chanlamcoupling_all.json", "w", encoding="utf-8") as f:
    json.dump(all_reactions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(all_reactions)} reactions to chanlamcoupling_all.json")