import yaml


def get_config(file_name='config.yaml'):
    with open(file_name, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config