import yaml


def get_config():
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


if __name__ == '__main__':
    pass
