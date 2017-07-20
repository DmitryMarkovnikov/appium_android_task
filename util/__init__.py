import os

import yaml


def load_yaml(file_name):
    """
    Parse yaml file from data folder and return parsing result
    :param file_name: name of a file from data folder
    :return: dictionary with parsed data
    """
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', file_name))

    with open(file_name, 'r') as stream:
        data = yaml.load(stream)
    return data
