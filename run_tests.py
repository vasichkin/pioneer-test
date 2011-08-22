#! /usr/bin/env python
import os
from optparse import OptionParser


debug_level = '-v3'
lettuce_args = ''


class ConfigurationException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return self.msg

def _run_lettuce(args, config_name):
    print 'PIONEER_TEST_CONFIG_NAME=%s' % config_name
    print 'lettuce args: %s' % args

    from lettuce import lettuce_cli
    args=['./features']
    lettuce_cli.main(args)

def run_all_tests(args):
    if len(args) < 1:
        raise ConfigurationException('You must specify config')

    config_name = args[0]
    if not os.path.exists(config_name):
        raise ConfigurationException('Config %s doesn\'t exist' % config_name)
    _run_lettuce(lettuce_args, config_name)

def run_single_test(args):
    pass

def run_special_test(args):
    pass


def show_options():
    parser = OptionParser(usage='''Usage: %prog <command> <path_to_config>
        <command> - type of test to run: full, single, special
        <path_to_config> - path to config file. (Default:cfg/default.cfg)''')

    (options, args) = parser.parse_args()
    if len(args) < 2:
        print 'Not enough parameters\n'
        parser.print_help()
        return

    command_map = {'full': run_all_tests,
                   'single': run_single_test,
                   'special': run_special_test}
    command = args[0]
    if command in command_map:
        try:
            command_map[command](args[1:])

        except ConfigurationException as e:
            print e.msg
            print "run %s -h for usage" % parser.get_prog_name()
            return
    else:
        print 'unknown option %s' % command
        parser.print_help()
        return

show_options()
