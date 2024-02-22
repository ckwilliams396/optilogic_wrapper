import headers.header_generator as hg
import requests

url = 'https://api.optilogic.app/v0'


def get_secrets(api_key, secret_type=None):
    options = dict()
    if secret_type is not None:
        options['type'] = secret_type
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/secrets', headers=headers, params=options)
    return response.text


def get_secret(api_key, secret_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/secret/{secret_name}', headers=headers)
    return response.text


def add_secret(api_key, secret_name, secret_value, secret_type=None, meta=None, description=None):
    options = {
        'value': secret_value
    }
    if secret_type is not None:
        options['type'] = secret_type
    if meta is not None:
        options['meta'] = meta
    if description is not None:
        options['description'] = description
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{url}/secret/{secret_name}', headers=headers, params=options)
    return response.text


def update_secret(api_key, secret_name, updated_name=None, secret_value=None, secret_type=None, meta=None, description=None):
    options = dict()
    if updated_name is not None:
        options['name'] = updated_name
    if secret_value is not None:
        options['value'] = secret_name
    if secret_type is not None:
        options['type'] = secret_type
    if meta is not None:
        options['meta'] = meta
    if description is not None:
        options['description'] = description
    if options == {}:
        raise Exception('At least one parameter must be passed.')
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{url}/secret/{secret_name}', headers=headers, params=options)
    return response.text


def delete_secret(api_key, secret_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f'{url}/secret/{secret_name}', headers=headers)
    return response.text