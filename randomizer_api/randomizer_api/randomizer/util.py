import os
import json
from typing import *

RANDOMIZER_URL_LIST_KEY = 'RANDOMIZER_URL_LIST'

def load_urls(environ=os.environ) -> List[str]:
    if url_list_path := environ.get(RANDOMIZER_URL_LIST_KEY):
        urls_json = json.load(open(url_list_path, 'r'))
        return [ entry['link'] for entry in urls_json['entries'] ]
    else:
        return []