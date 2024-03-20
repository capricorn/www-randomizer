#!/bin/bash

PROJ_ROOT="${HOME}/www-randomizer"

cd randomizer_api/randomizer_api
DJANGO_DEBUG='False'\
    SECRET_KEY_FILE="${PROJ_ROOT}/randomizer_api/randomizer_api/secret.txt"\
    RANDOMIZER_URL_LIST="${PROJ_ROOT}/urls.json"\
    poetry run python -m gunicorn randomizer_api.wsgi