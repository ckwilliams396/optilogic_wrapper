import requests
import headers.header_generator as hg


def get_db_data_export_list(api_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get("https://api.optilogic.app/v0/job/db-data-export/list", headers=headers)
    return response.text


def get_db_data_export_by_id(api_key, job_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"https://api.optilogic.app/v0/job/db-data-export/{job_key}", headers=headers)
    return response.text
