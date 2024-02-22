import header_generator as hg
import requests
import config


def get_connection_info(api_key, storage_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{config.url}/storage/{storage_name}/connection-string', headers=headers)
    return response.text


def get_schema(api_key, storage_name, schema=None, table=None):
    options = dict()
    if schema is not None:
        options['schema'] = schema
    if table is not None:
        options['table'] = table
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{config.url}/storage/{storage_name}/schema', headers=headers, params=options)
    return response.text


def get_tables(api_key, storage_name, schema, row_count=False):
    options = {
        'rowCount': row_count
    }
    if schema is not None:
        options['schema'] = schema
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{config.url}/storage/{storage_name}/tables', headers=headers, params=options)
    return response.text


def empty_tables(api_key, storage_name, tables_to_empty, dry_run=False):
    options = {
        'dryRun': dry_run
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{config.url}/storage/{storage_name}/empty-tables', data=tables_to_empty,  headers=headers, params=options)
    return response.text


def export_data(api_key, storage_name, data_to_export, source_schema=None, source_group=None, file_format=None):
    options = dict()
    if source_schema is not None:
        options['sourceSchema'] = source_schema
    if source_group is not None:
        options['sourceGroup'] = source_group
    if file_format is not None:
        options['format'] = file_format
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{config.url}/storage/{storage_name}/db-data-export', data=data_to_export,  headers=headers, params=options)
    return response.text


def move_file(api_key, storage_name, source, dest):
    options = {
        'source': source,
        'dest': dest
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{config.url}/storage/{storage_name}/file/move', headers=headers, params=options)
    return response.text


def move_folder(api_key, storage_name, source, dest):
    options = {
        'source': source,
        'dest': dest
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{config.url}/storage/{storage_name}/folder/move', headers=headers, params=options)
    return response.text


def copy_folder(api_key, storage_name, source, dest, dest_storage_name=None):
    options = {
        'source': source,
        'dest': dest
    }
    if dest_storage_name is not None:
        options['destStorageName'] = dest_storage_name
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{config.url}/storage/{storage_name}/folder/copy', headers=headers, params=options)
    return response.text
