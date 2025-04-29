import json
import os

def load_secrets(path=None):
    if path is None:
        # Default to project root
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'secrets.json')
    with open(path, 'r') as f:
        return json.load(f)
