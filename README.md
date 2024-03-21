# www-randomizer

`www-randomizer` is a simple url random redirector. Given a list of urls, visiting `/random` will randomly redirect to one of them.

## Running

To run a gunicorn instance, run the following from the project root:

```console
$ ./run.sh
```

## Environment variables

- `SECRET_KEY_FILE`: A file containing a secret key suitable for use with django.
- `RANDOMIZER_URL_LIST`: A json file containing url entries. See below for its schema.

## RANDOMIZER_URL_LIST Schema

An example:

```json
{
  "entries": [
    { "link": "https://google.com" },
    { "link": "https://github.com" }
  ]
}
```
