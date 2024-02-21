

def generate_api_key_header(api_key):
    return {
        'API_KEY': api_key
    }


def generate_refresh_key_header(refresh_key):
    return {
        'X-REFRESH-KEY': refresh_key
    }


def generate_basic_auth_header(username, password):
    return {
        'X-USER-ID': username,
        'X-USER-PASSWORD': password
    }