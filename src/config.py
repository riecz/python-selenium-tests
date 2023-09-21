import os
from pconf import Pconf
from src.api.file_reader import read_json_file

Pconf.env(separator='__')
Pconf.env()


def load_config_file(filename):
    '''
    This function assumes that 'filename' is the full path to a json file that
    is to be used to load into Pconf
    to get all the configuration variables from that file
    '''


# Load the default config.json file
config_file = os.path.join(os.path.dirname(__file__), '../config.json')
if not os.path.isfile(config_file):
    print('Warning: Could not find configuration file \'{file}\''.format(
        file=config_file))
else:
    try:
        # Check that the file is correct json format
        read_json_file(config_file)
    except ValueError:
        raise Exception(
            '\'{file}\' is not a valid json file. Please check the format'
            .format(file=config_file))
    print('Loading config file \'{filename}\''.format(filename=config_file))
    Pconf.file(config_file, encoding='json')

# Get all the config values parsed from the sources
config = Pconf.get()
