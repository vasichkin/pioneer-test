import logging
import pdb
from framework.config import parameter
from lettuce import step
from lettuce.registry import world

from framework import nova_manage
#from novatests.util.utils import replace_prefix
#import novatests.log

#_logger = logging.getLogger(__name__)

test_user=parameter('test-auth','test_user')
test_project=parameter('test-auth','test_project')
test_network=parameter('test-auth','test_network')
test_nets=parameter('test-auth','test_nets')
test_ips=parameter('test-auth','test_ips')



## INIT ENVIROMENT
@step(u'Do all to set up nova')
def do_all_to_set_up_nova(step):
    step.behave_as("""
        Create admin user "osth-user-admin"
        Create project "osth-test-project" for user "osth-user-admin"
        Create network "10.222.0.0/24" with "1" nets, "256" ips per network
        Check novarc function for project "osth-test-project", user "osth-user-admin"
        """)

@step(u'Do all to clean nova')
def do_all_to_clean_nova(step):
    step.behave_as("""
        Delete network "10.222.0.0/24"
        Delete project "osth-test-project" for user "osth-user-admin"
        Delete user "osth-user-admin"
        """)

@step(u'Do all checks to verify nova enviroment')
def do_all_checks_to_verify_nova_enviroment(step):
    step.behave_as("""
        Check user "osth-user-admin" exist
        Check project "osth-test-project" exist for user "osth-user-admin"
        Check network "10.222.0.0/24" exist
        Check novarc function for project "osth-test-project", user "osth-user-admin"
        """)


@step(u'Check if "(.*)" is not installed')
def check_if_group1_is_not_installd(step,group1)
    rpm_check(group1,false)

@step(u'Check if "(.*)" is installed')
def check_if_group1_is_installd(step,group1)
    rpm_check(group1,true)

@step(u'Install "(.*)"')
def install_group1(step,group1)
    rpm_install(group1,false)

@step(u'Remove "(.*)"')
def remove_group1(step,group1)
    rpm_remove(group1,false)




'''
# GENERIC VERSION DOESN'T WORK BECAUSE OF LETTUCE. CHECK IT

@step(u'Do all to set up nova')
def do_all_to_set_up_nova(step):
    step.behave_as("""
        Create admin user {user}
        Create project {project} for user {user}
        Create network {network} with {nets} nets, {ips} ips per network
        Check novarc function for project {project}, user {user}
    """.format(user=test_user, project=test_project, network=test_network, nets=test_nets, ips=test_ips))
    


@step(u'Do all to clean nova')
def do_all_to_clean_nova(step):
    step.behave_as("""
        Delete network {network}
        Delete project {project} for user {user}
        Delete user {user}
        """.format(user=parameter('test-auth','test_user'),
            project=parameter('test-auth','test_project'),
            network=parameter('test-auth','test_network'))
        )

@step(u'Do all checks to verify nova enviroment')
def do_all_checks_to_verify_nova_enviroment(step):
    step.behave_as("""
        Check user {user} exist
        Check project {project} exist for user {user}
        Check network {network} exist
        Check novarc function for project {project}, user {user}
        """.format(user=parameter('test-auth','test_user'),
            project=parameter('test-auth','test_project'),
            network=parameter('test-auth','test_network'))
        )
'''