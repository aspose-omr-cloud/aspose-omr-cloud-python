import os
import json

def read_file(filepath):
    with open(filepath, 'r') as content_file:
        return content_file.read()



CONFIG = 'test_config.json'
DATA = 'Data'

curr_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
while curr_path != os.path.abspath(os.path.join(curr_path, os.pardir)) and not os.path.isfile(
        os.path.join(curr_path, CONFIG)):
    curr_path = os.path.abspath(os.path.join(curr_path, os.pardir))
if os.path.isfile(os.path.join(curr_path, CONFIG)):
    with open(os.path.join(curr_path, CONFIG)) as f:
        config = json.loads(f.read())
if os.path.isdir(os.path.join(curr_path, DATA)):
    data_dir = os.path.join(curr_path, DATA)
