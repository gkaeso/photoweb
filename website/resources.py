import os
import json


APP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'website')

with open(os.path.join(APP_DIR, 'resources', 'keys.json'), 'r') as f:
    KEYS = json.load(f)

