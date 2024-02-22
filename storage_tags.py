import header_generator as hg
import requests


url = 'https://api.optilogic.app/v0'


def remove_tags(api_key, storage_name, labels):
    options = {
        'labels': labels
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f'{url}/storage/{storage_name}/labels', headers=headers, params=options)
    return response.text


def get_labels(api_key, storage_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/{storage_name}/labels', headers=headers)
    return response.text


def add_label(api_key, storage_name, labels):
    options = {
        'labels': labels
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{url}/storage/{storage_name}/labels', headers=headers, params=options)
    return response.text


def replace_label(api_key, storage_name, labels):
    options = {
        'labels': labels
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{url}/storage/{storage_name}/labels', headers=headers, params=options)
    return response.text
