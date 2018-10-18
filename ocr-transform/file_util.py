import json
from os import path, mkdir


def create_folders(filename, level=3):
    if level > 0:
        create_folders(path.dirname(filename), level - 1)
    if filename and not path.exists(filename):
        mkdir(filename)


def load_json(filename, warning=False):
    if path.exists(filename):
        try:
            with open(filename) as f:
                return json.load(f)
        except Exception as e:
            print(filename, e)
    elif warning:
        print('%s not exist' % filename)


def save_json(obj, filename, sort_keys=False):
    with open(filename, 'w') as f:
        json.dump(obj, f, ensure_ascii=False, sort_keys=sort_keys)
