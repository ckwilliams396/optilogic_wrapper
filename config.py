import configparser
parser = configparser.ConfigParser()
parser.read_file(open('config/config.ini'))

url = parser.get('url', 'base_path')
