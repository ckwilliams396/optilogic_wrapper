import requests
import headers.header_generator as hg


url = "https://api.optilogic.app/v0"


def get_workspaces(api_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}workspaces", headers=headers)
    return response.text


def get_workspace_by_id(api_key, workspace_id):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_id}", headers=headers)
    return response.text


# this has some filtering option that will need to be looked at later
def get_jobs(api_key, workspace_id, command="", history="", run_secs_max="", run_secs_min="", status="", tags=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_id}/jobs", headers=headers)
    return response.text


def get_job_stats(api_key, workspace_id, command="", history="", run_secs_max="", run_secs_min="", status="", tags=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_id}/jobs/stats", headers=headers)
    return response.text


def queue_job(api_key, workspace_id, directory_path, file_name, command="", command_args="", resource_config="3XS",tags="", timeout=60):
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_id}/jobs", headers=headers)
    return response.text


def get_job_info(api_key, workspace_id, job_key, op=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_id}/jobs/{job_key}", headers=headers)
    return response.text


def stop_job(api_key, workspace_id, job_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f"{url}/{workspace_id}/jobs/{job_key}", headers=headers)
    return response.text


def queue_jobs(api_key, workspace_id, jobs_to_be_queued, resource_config="3XS", tags=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_id}/jobBatch/jobify", headers=headers, body=jobs_to_be_queued)
    return response.text


def queue_jobs_from_search_terms(api_key, workspace_id, jobs_to_be_queued, resource_config="3XS", tags=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_id}/jobBatch/jobify/searchNRun", headers=headers, body=jobs_to_be_queued)
    return response.text


def run_jobs_back_to_back(api_key, workspace_id, jobs_to_run, resource_config="3XS", tags=""):
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_id}/jobBatch/backToBack", headers=headers, body=jobs_to_run)
    return response.text