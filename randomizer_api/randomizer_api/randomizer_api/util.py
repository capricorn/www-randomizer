import os

ENV_SECRET_KEY_FILE = 'SECRET_KEY_FILE'

def read_secret_key(environ=os.environ):
    if key_file := environ.get(ENV_SECRET_KEY_FILE):
        with open(key_file, 'r') as f:
            return f.read()

    raise KeyError(f'Environment key {ENV_SECRET_KEY_FILE} does not exist.')