import os
import json


APP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'website')

with open(os.path.join(APP_DIR, 'resources', 'keys.json'), 'r') as f:
    KEYS = json.load(f)

with open(os.path.join(APP_DIR, 'resources', 'config.json'), 'r') as f:
    CONFIG = json.load(f)
