import header_generator as hg
import requests


url = 'https://api.optilogic.app/v0'


def get_database_schema(api_key, storage_name, table):
    options = dict()
    if table is not None:
        options['table'] = table
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/{storage_name}/customizations', headers=headers, params=options)
    return response.text


# docs says /ping?
def get_column_types(api_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/db-column-types', headers=headers)
    return response.text


def create_custom_column(api_key, storage_name, table_name, column_name, datatype, character_maximum_length=None, is_nullable=None, default_value=None, is_table_key_column=None, true_datatype=None, is_required=None):
    payload = {
        'tableName': table_name,
        'columnName': column_name,
        'dataType': datatype,
    }
    if character_maximum_length is not None:
        payload['characterMaximumLength'] = character_maximum_length
    if is_nullable is not None:
        payload['isNullable'] = is_nullable
    if default_value is not None:
        payload['defaultValue'] = default_value
    if is_table_key_column is not None:
        payload['isTableKeyColumn'] = is_table_key_column
    if true_datatype is not None:
        payload['trueDataType'] = true_datatype
    if is_required is not None:
        payload['isRequired'] = is_required
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{url}/storage/{storage_name}/custom-column', headers=headers, data=payload)
    return response.text


def get_column_details(api_key, storage_name, table_name, column_name):
    options = {
        'tableName': table_name,
        'columnName': column_name
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/{storage_name}/custom-column', headers=headers, params=options)
    return response.text


def update_column(api_key, storage_name, table_name, column_name, new_column_name=None, datatype=None, character_maximum_length=None, is_nullable=None, default_value=None, is_table_key_column=None, true_datatype=None, is_required=None):
    options = {
        'tableName': table_name,
        'columnName': column_name
    }
    if datatype is not None:
        options['dataType'] = datatype
    if new_column_name is not None:
        options['newColumnName'] = new_column_name
    if character_maximum_length is not None:
        options['characterMaximumLength'] = character_maximum_length
    if is_nullable is not None:
        options['isNullable'] = is_nullable
    if default_value is not None:
        options['defaultValue'] = default_value
    if is_table_key_column is not None:
        options['isTableKeyColumn'] = is_table_key_column
    if true_datatype is not None:
        options['trueDataType'] = true_datatype
    if is_required is not None:
        options['isRequired'] = is_required
    headers = hg.generate_api_key_header(api_key)
    response = requests.put(f'{url}/storage/{storage_name}/custom-column', headers=headers, params=payload)
    return response.text


def delete_column(api_key, storage_name, table_name, column_name):
    options = {
        'tableName': table_name,
        'columnName': column_name
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f'{url}/storage/{storage_name}/custom-column', headers=headers, params=options)
    return response.text


def get_columns(api_key, storage_name, table_name):
    options = {
        'tableName': table_name
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/{storage_name}/custom-columns', headers=headers, params=options)
    return response.text


def validate_columns(api_key, storage_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f'{url}/storage/{storage_name}/custom-columns/validate', headers=headers)
    return response.text


def repair_columns(api_key, storage_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f'{url}/storage/{storage_name}/custom-columns/repair', headers=headers)
    return response.text
