import json
import os

from ..utils.utils import build_graph
from ..constants import MEMBERS

#  ===========================
#          HANDLE I/O
#  ===========================

def serialize_as_json(filename, data, open_as='w'):
    with open(filename, open_as) as f:
        f.write(json.dumps(data))

def deserialize_json(filename):
    data = None
    if os.path.isfile(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            data = json.load(f)
    return data

def load_graph(filename):
    data = deserialize_json(filename)
    if data is None:
        return build_graph(MEMBERS)
    return data

def update_existing_groupings_file(filename, existing_data, groups):
    excluded_member = None
    for idx in range(len(groups)):
        group = groups[idx]
        if len(group) == 1:
            excluded_member = group[0]
            groups = groups[1:]
            break
    existing_data.append({
        "excluded": [excluded_member],
        "groupings": groups
    })
    serialize_as_json(filename, existing_data)