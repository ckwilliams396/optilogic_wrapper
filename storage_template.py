import header_generator as hg
import requests
import config


def get_database_templates(api_key, template_id=None, schema=None, schema_type=None, include_non_default=False):
    options = {
        'includeNonDefault': include_non_default
    }
    if template_id is not None:
        options['id'] = template_id
    if schema is not None:
        options['schema'] = schema
    if schema_type is not None:
        options['schemaType'] = schema_type
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{config.url}/storages/db-templates', headers=headers, params=options)
    return response.text


def get_unique_database_templates(api_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{config.url}/storages/db-templates', headers=headers)
    return response.text

