import os
#from os.path import dirname
from ConfigParser import ConfigParser
import logging

#get root folder of project
#base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

_config = None
_params = {}
_base_config = None


def get_context_param(param):
    """
    Context parameters are used to transfer parameters from osth runner script to lettuce terrain
    """

    if param in _params:
        return _params[param]

def set_context_param(param, value):
    """
    Context parameters are used to transfer parameters from osth runner script to lettuce terrain
    """

    _params[param] = value

def parameter(section, parameter_name):
    if not _config:
        return None
    if _config.has_option(section, parameter_name):
        return _config.get(section, parameter_name)
    elif _base_config and _base_config.has_option(section, parameter_name):
        return _base_config.get(section, parameter_name)
    else:
        return None


def int_parameter(section, name):
    value = parameter(section, name)
    return value is not None and int(value) or None


def load_config(config_file_name=None):
    if not config_file_name:
        raise ValueError("Config file isn't defined")
    if not os.path.exists(config_file_name):
        raise ValueError('Config file %s not exists' % config_file_name)
    config = ConfigParser()
    config.read(config_file_name)

    global _base_config
    if config.has_option("common", "base_config"):
        base_config_file_name = config.get("common", "base_config")
        base_config = ConfigParser()
        base_config.read(base_config_file_name)
        _base_config = base_config
        
    global _config
    _config = config
    logging.debug('Config loaded')

