import header_generator as hg
import requests
from multipledispatch import dispatch
import config


@dispatch(str, str)
def generate_api_key(username, password):
    headers = hg.generate_basic_auth_header(username, password)
    response = requests.post(f'{config.url}/refreshApiKey', headers=headers)
    return response.text


@dispatch(str)
def generate_api_key(refresh_token):
    headers = hg.generate_refresh_key_header(refresh_token)
    response = requests.post(f'{config.url}/refreshApiKey', headers=headers)
    return response.text
