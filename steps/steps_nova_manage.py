import logging
import pdb
from lettuce.decorators import step
from lettuce.registry import world

#from novatests.framework.config import parameter

from framework import nova_manage
#from novatests.util.utils import replace_prefix
#import novatests.log

#_logger = logging.getLogger(__name__)

NovaManager = nova_manage.NovaManage()

exist=1
not_exist=0

## USER

@step(u'Create user "(.*)"')
def create_user_group1(step, group1):
    NovaManager.create_user(group1)

@step(u'Create admin user "(.*)"')
def create_admin_user_group1(step, group1):
    NovaManager.create_admin_user(group1)

@step(u'Check user "(.*)" exist')
def check_user_group1_exist(step, group1):
    NovaManager.check_user(group1, exist)

@step(u'Check user "(.*)" does not exist')
def check_user_group1_not_exist(step, group1):
    NovaManager.check_user(group1, not_exist)

@step(u'Delete user "(.*)"')
def delete_user_group1(step, group1):
    NovaManager.delete_user(group1)

## PROJECT

@step(u'Create project "(.*)" for user "(.*)"')
def create_project_group1_for_user_group2(step, group1, group2):
    NovaManager.create_project(group1, group2)

@step(u'Delete project "(.*)" for user "(.*)"')
def delete_project_group1_for_user_group2(step, group1, group2):
    NovaManager.delete_project(group1)

@step(u'Check project "(.*)" exist for user "(.*)"')
def check_project_group1_exist(step, group1, group2):
    NovaManager.check_project(group1, group2, exist)

@step(u'Check project "(.*)" does not exist for user "(.*)"')
def check_project_group1_not_exist(step, group1, group2):
    NovaManager.check_project(group1, group2, not_exist)

## NETWORK

@step(u'Create network "(.*)" with "(.*)" nets, "(.*)" ips per network')
def create_network_group1_with_group2_nets_group3_ips_per_network(step, group1, group2, group3):
    NovaManager.create_network(group1, group2, group3)

@step(u'Delete network "(.*)"')
def delete_network(step, group1):
    NovaManager.delete_network(group1)

@step(u'Check network "(.*)" exist')
def check_network_exist(step, group1):
    NovaManager.check_network(group1,exist)

@step(u'Check network "(.*)" does not exist')
def check_network_not_exist(step, group1):
    NovaManager.check_network(group1,not_exist)

## NOVARC

@step(u'Check novarc function for project "(.*)", user "(.*)"')
def check_novarc_function_for_project_group1_user_group2(step, group1, group2):
    novacred=NovaManager.zipfile_project(group1,group2)
    NovaManager.check_access(novacred)

## IMAGE
@step(u'Register image "(.*)" using project "(.*)", user "(.*)"')
def register_image_group1_using_project_group2_user_group3(step, group1, group2, group3):
    NovaManager.upload_image(group1,group2,group3)

@step(u'Deregister image "(.*)"')
def deregister_image_group1(step, group1):
    NovaManager.deregister_image(group1)

## SERVICE
@step(u'Start openstack services')
def start_openstack_services(step):
    NovaManager.start_services()

@step(u'Stop openstack services')
def stop_openstack_services(step):
    NovaManager.stop_services()

@step(u'Check openstack services')
def check_openstack_services(step):
    NovaManager.check_services()

@step(u'Check openstack services running')
def check_openstack_services_running(step):
    NovaManager.check_services(1)

@step(u'Check openstack services stoped')
def check_openstack_services_stoped(step):
    NovaManager.check_services(0)
