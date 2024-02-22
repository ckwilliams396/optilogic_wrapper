import requests
import headers.header_generator as hg


url = "https://api.optilogic.app/v0"


def get_workspaces(api_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}workspaces", headers=headers)
    return response.text


def get_workspace_by_id(api_key, workspace_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}", headers=headers)
    return response.text


def get_jobs(api_key, workspace_name, command=None, history=None, run_secs_max=None, run_secs_min=None, status=None, tags=None):
    options = dict()
    if command is not None:
        options['command'] = command
    if history is not None:
        options['history'] = history
    if run_secs_max is not None:
        options['runSecMax'] = run_secs_max
    if run_secs_min is not None:
        options['runSecsMin'] = run_secs_min
    if status is not None:
        options['status'] = status
    if tags is not None:
        options['tags'] = tags
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/jobs", headers=headers, params=options)
    return response.text


def get_job_stats(api_key, workspace_name, command=None, history=None, run_secs_max=None, run_secs_min=None, status=None, tags=None):
    options = dict()
    if command is not None:
        options['command'] = command
    if history is not None:
        options['history'] = history
    if run_secs_max is not None:
        options['runSecMax'] = run_secs_max
    if run_secs_min is not None:
        options['runSecsMin'] = run_secs_min
    if status is not None:
        options['status'] = status
    if tags is not None:
        options['tags'] = tags
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/jobs/stats", headers=headers, params=options)
    return response.text


def queue_job(api_key, workspace_name, directory_path, file_name, command=None, command_args=None, resource_config=None, tags=None, timeout=None):
    options = {
        'directoryPath': directory_path,
        'fileName': file_name,
    }
    if command is not None:
        options['command'] = command
    if command_args is not None:
        options['commandArgs'] = command_args
    if resource_config is not None:
        options['resourceConfig'] = resource_config
    if tags is not None:
        options['tags'] = tags
    if timeout is not None:
        options['timeout'] = timeout
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/jobs", headers=headers, params=options)
    return response.text


def get_job_info(api_key, workspace_name, job_key, op=None):
    options = dict()
    if op is not None:
        options['op'] = op
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/jobs/{job_key}", headers=headers, params=options)
    return response.text


def stop_job(api_key, workspace_name, job_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f"{url}/{workspace_name}/jobs/{job_key}", headers=headers)
    return response.text


def queue_jobs(api_key, workspace_name, jobs_to_be_queued, resource_config=None, tags=None):
    options = dict()
    if resource_config is not None:
        options['resourceConfig'] = resource_config
    if tags is not None:
        options['tags'] = tags
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/jobBatch/jobify", headers=headers, data=jobs_to_be_queued, params=options)
    return response.text


def queue_jobs_from_search_terms(api_key, workspace_name, jobs_to_be_queued, resource_config=None, tags=None):
    options = dict()
    if resource_config is not None:
        options['resourceConfig'] = resource_config
    if tags is not None:
        options['tags'] = tags
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/jobBatch/jobify/searchNRun", headers=headers, data=jobs_to_be_queued, params=options)
    return response.text


def run_jobs_back_to_back(api_key, workspace_name, jobs_to_run, resource_config=None, tags=None, timeout=None, verbose_output=False):
    options = {
        'verboseOutput': verbose_output
    }
    if resource_config is not None:
        options['resourceConfig'] = resource_config
    if tags is not None:
        options['tags'] = tags
    if timeout is not None:
        options['timeout'] = timeout
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/jobBatch/backToBack", headers=headers, data=jobs_to_run, params=options)
    return response.text


def run_jobs_back_to_back_from_search_terms(api_key, workspace_name, jobs_to_run, resource_config=None, tags=None, timeout=None, verbose_output=False):
    options = {
        'verboseOutput': verbose_output
    }
    if resource_config is not None:
        options['resourceConfig'] = resource_config
    if tags is not None:
        options['tags'] = tags
    if timeout is not None:
        options['timeout'] = timeout
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/jobBatch/backToBack/searchNRun", headers=headers, data=jobs_to_run, params=options)
    return response.text


def get_files(api_key, workspace_name, search_filter=None, max_depth=None, base_dir=None, include_dir=False):
    options = {
        'includeDir': include_dir
    }
    if search_filter is not None:
        options['filter'] = search_filter
    if max_depth is not None:
        options['maxDepth'] = max_depth
    if base_dir is not None:
        options['baseDir'] = base_dir
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/files", headers=headers, params=options)
    return response.text


def get_job_ledger(api_key, workspace_name, job_key, keys=None, limit=None):
    options = dict()
    if keys is not None:
        options['keys'] = keys
    if limit is not None:
        options['limit'] = limit
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/job/{job_key}/ledger", headers=headers, params=options)
    return response.text


def get_job_metrics(api_key, workspace_name, job_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/job/{job_key}/metrics", headers=headers)
    return response.text


def get_job_metrics_stats(api_key, workspace_name, job_key):
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/job/{job_key}/metrics/stats", headers=headers)
    return response.text


def copy_file(api_key, workspace_name, source_directory_path, source_file_name, target_directory_path, target_file_name, overwrite=False):
    options = {
        'sourceDirectoryPath': source_directory_path,
        'sourceFilename': source_file_name,
        'targetDirectoryPath': target_directory_path,
        'targetFilename': target_file_name,
        'overwrite': overwrite
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/file/copy", headers=headers, params=options)
    return response.text


def share_file(api_key, workspace_name, source_directory_path, source_file_name, target_user):
    options = {
        'sourceDirectoryPath': source_directory_path,
        'sourceFilePath': source_file_name,
        'targetUser': target_user
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/file/share", headers=headers, params=options)
    return response.text


def get_file(api_key, workspace_name, directory_path, file_name, op):
    options = dict()
    if op is not None:
        options['op'] = op
    headers = hg.generate_api_key_header(api_key)
    response = requests.get(f"{url}/{workspace_name}/file/{directory_path}/{file_name}", headers=headers, params=options)
    return response.text


def upload_file(api_key, workspace_name, directory_path, file_name, path_to_local_file, overwrite=False):
    options = {
        'overwrite': overwrite
    }
    with open(path_to_local_file, 'rb') as file:
        data = file.read()
    headers = hg.generate_api_key_header(api_key)
    headers['content-type'] = 'application/octet-stream'
    headers['content-length'] = f'{len(data)}'
    response = requests.post(f"{url}/{workspace_name}/file/{directory_path}/{file_name}", data=data, headers=headers, params=options)
    return response.text


def delete_file(api_key, workspace_name, directory_path, file_name):
    headers = hg.generate_api_key_header(api_key)
    response = requests.delete(f"{url}/{workspace_name}/file/{directory_path}/{file_name}", headers=headers)
    return response.text


def share_folder(api_key, workspace_name, source_directory_path, target_users, include_hidden=False):
    options = {
        'sourceDirectoryPath': source_directory_path,
        'targetUsers': target_users,
        'includeHidden': include_hidden
    }
    headers = hg.generate_api_key_header(api_key)
    response = requests.post(f"{url}/{workspace_name}/folder/share", headers=headers, params=options)
    return response.text