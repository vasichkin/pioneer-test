
# TODO excavate this wtf
import commands
import tarfile
import re
import pdb
from config import parameter
#import novatests.log as logging


novarc_parameters = ['EC2_ACCESS_KEY',
                     'EC2_SECRET_KEY',
                     'EC2_URL',
                     'NOVA_API_KEY',
                     'NOVA_USERNAME',
                     'NOVA_URL',
                     'S3_URL']


test_user=parameter('test-auth','test_user')
test_project=parameter('test-auth','test_project')
test_network=parameter('test-auth','test_network')
test_nets=parameter('test-auth','test_nets')
test_ips=parameter('test-auth','test_ips')


class NovaManage(object):
    openstack_services = [#'nova-ajax-console-proxy',
                          'nova-api',
                          'nova-compute',
                          #'nova-direct-api',
                          'nova-network',
                          'nova-objectstore',
                          'nova-scheduler',
                          #'nova-vncproxy',
                          #'nova-volume'
                          ]

    ## common methods
    def __init__(self, executor=None):
        self.executor = executor

    def set_executor(self, executor):
        self.executor = executor

    def _bash(self, cmd):
        #return self.executor("%s" % cmd)
        retcode = commands.getstatusoutput(cmd)
        #print "------------------\n",retcode[1]
        if retcode[0]<0:
            self._raise("\n\n\nCommand '%s' failed with code %s.\n Error: %s\n" % (cmd, retcode[0],retcode[1]))
        elif retcode[0]>0:
            print ("\n\n\nNon fatal: \n Command '%s' failed with code %s.\n Error: %s\n" % (cmd, retcode[0],retcode[1]))
        return retcode[1]

    def _raise(self, msg):
        raise Exception("Got exception: %s" % (msg))

## USER
    ## methods to deal with nova-manage user xxx
    def create_user(self, user):
        out=self._bash("nova-manage user list")
        m=re.match(user, out)
        if m:
            self._raise("Try to crate user %s, but it exist!" % user)
        else:
            self._bash('nova-manage user create %s' % user)

    def create_admin_user(self, user):
        out=self._bash("nova-manage user list")
        m=re.match(user, out)
        if m:
            self._raise("Try to crate user %s, but it exist!" % user)
        else:
            out=self._bash('nova-manage user admin %s' % user)
        return out
        
    def check_user(self, user, exist):
        out=self._bash("nova-manage user list")
        m=re.search(user, out)
        if m and not exist:
            self._raise("Deleted by script network %s  exist, but it must not." % user)
        elif not m and exist:
            self._raise("Created by script network %s does not exist, but it must." % user)

    def delete_user(self, user):
        self._bash('nova-manage user delete %s' % user)


## NETWORK
    ## methods to deal with nova-manage network xxx
    def create_network(self, cidr, quantity, ip_per_network):
        out=self._bash("nova-manage network list")
        m=re.search(cidr, out)
        if m:
            self._raise("Try to crate network, but it exist!")
        else:
            self._bash("nova-manage network create private %s %s %s --bridge_interface=br100" % (cidr, quantity, ip_per_network))


    def check_network(self, cidr, exist):
        out=self._bash("nova-manage network list")
        m=re.search(cidr, out)
        if m and not exist:
            self._raise("Deleted by script network "+cidr+"  exist, but it must not.")
        elif not m and exist:
            self._raise("Created by script network "+cidr+" does not exist, but it must.")

    def delete_network(self, cidr):
        self._bash("nova-manage network delete %s" % cidr)


## PROJECT

    ## methods to deal with nova-manage project xxx
    def create_project(self, project, user):
        out=self._bash("nova-manage project list")
        m=re.search(project, out)
        if m:
            self._raise("Try to crate project, but it exist!")
        else:
            self._bash('nova-manage project create %s %s' % (project, user))

    def try_create_project(self, project, user):
        out = self._bash('nova-manage project list')
        m=re.search(project, out)
        if not m:
            self.create_project(project, user)

    def check_project(self, project, user, exist):
        out = self._bash('nova-manage project list')
        m=re.search(project, out)
        if m and not exist:
            self._raise("Deleted by script project "+project+"  exist, but it must not.")
        elif not m and exist:
            self._raise("Created by script project "+project+" does not exist, but it must")


    def delete_project(self, project):
        self._bash('nova-manage project delete %s' % project)

## IMAGE
    def upload_image(self,imagefile,project,user):
        pathdir=self._bash('mktemp -d')
        tar = tarfile.open(imagefile)
        files = tar.getnames()
        tar.extractall(pathdir)
        tar.close()

        for line in files:
            if 'kernel' in line: kernel=pathdir+'/'+line
            if 'ramdisk' in line: ramdisk=pathdir+'/'+line
            if 'rootfs' in line: rootfs=pathdir+'/'+line

        ''' nova-manage image all_register --image=RS-ubu-10.04LTS.SSH-key.rootfs.raw --kernel=RS-ubu-10.04LTS.SSH-key.kernel --ram=RS-ubu-10.04LTS.SSH-key.ramdisk --name=osth-try --owner=vsk'''
        out=self._bash('nova-manage image all_register \
                    --image={rootfs} \
                    --kernel={kernel} \
                    --ram={ramdisk} \
                    --name={image_name} \
                    --owner={osth_user}'.format(
                    rootfs=rootfs,kernel=kernel,ramdisk=ramdisk,image_name='osth-test-image',osth_user=user))
        out="image_name"
        return out

    def deregister_image(self,imagename):
        assert False, 'This step must be implemented'

## SERVICE
    def start_services(self, service_names=openstack_services):
        for service_name in service_names:
            self._service(service_name,'start')

    def stop_services(self, service_names=openstack_services):
        for service_name in service_names:
            try:
                self._service(service_name,'stop')
            except:
                print ("Service %s already stoped" % service_name)

    def check_services(self, running=1, service_names=openstack_services):
        for service_name in service_names:
            out=self._service(service_name,'status')
            if 'running' in out and not running:
                self._raise("Service %s refused to stop." % service_name)
            elif 'stoped' in out and running:
                self._raise("Service %s refused to start." % service_name)
            #print "Status of service %s - %s" % (service_name,out)

        #out=self._bash('ps ax -o pid,comm|grep "nova"|grep defunc')
        out==self._bash('ps ax -o pid,comm')
        if 'defunc' in out:
            print "Found defunc, killing: ",out
            self._bash('killall '+service_name)


    def _service(self, service_name, action):
        distr =  parameter('os', 'distr')
        if distr == "ubuntu":
            cmd = 'service %s %s'
        else:
            #cmd = '/etc/init.d/openstack-%s %s'
            cmd = 'service openstack-%s %s'
        return self._bash(cmd % (service_name, action))




## OTHER STUFF
    def _grep_parameter(self, pathdir, parameter_name):
        return self._bash('grep %s= %s/novarc | sed \'s/^.*"\(.*\)"$/\\1/\''
                            % (parameter_name,pathdir))

    def _parse_parameters(self,pathdir, parameter_names):
        result = dict()
        for parameter_name in parameter_names:
            result[parameter_name] = self._grep_parameter(pathdir, parameter_name)
        return result

    def _read_file(self, file_name):
        return self._bash('cat %s' % file_name)

    def zipfile_project(self, project, user):
        pathdir=self._bash('mktemp -d')
        path = '%s/nova_%s_creds.zip' % (pathdir,project)
        self._bash('nova-manage project zipfile %s %s %s' % (project, user, path))
        self._bash("unzip %s -d %s" % (path,pathdir))
        novarc_parsed = self._parse_parameters(pathdir, novarc_parameters)
        pk_pem = self._read_file(pathdir+"/pk.pem")
        logging.debug("pk.pem:\n%s" % pk_pem)
        cert_pem = self._read_file(pathdir+"/cert.pem")
        logging.debug("cert.pem:\n%s" % pk_pem)
        cacert_pem = self._read_file(pathdir+"/cacert.pem")
        logging.debug("cacert.pem:\n%s" % pk_pem)
        self._bash('rm -rf %s' % pathdir)
        return novarc_parsed, pk_pem, cert_pem, cacert_pem

    ## db
    def sync_db(self):
        self._bash('nova-manage db sync')

    ## mysqladmin
    def mysql_drop_table(self, user, password, table):
        self._bash("mysqladmin -u%s -p%s -f drop %s" % (user, password, table))

    def mysql_create_table(self, user, password, table):
        self._bash("mysqladmin -u%s -p%s create %s" % (user, password, table))

    ## find_program
    def check_program(self, program):
        path = self._bash("which %s" % program)
        assert path != ""

    def check_package(self, program):
        package = self._bash("rpmquery %s" % program)
        assert package != ""
    def check_access(self, credentials):
        out=self._bash('euca-describe-images -U %s -A %s -S %s' % (credentials[0]['EC2_URL'],credentials[0]['EC2_ACCESS_KEY'],credentials[0]['EC2_SECRET_KEY']))
        print "NOT IMPLEMENTED ",out
        #if out<>0:
        #    self._raise("Wrong credentials")
    def rpm_check(self, package, installed=true)
        pass
    def rpm_install(self, package)
        pass
    def rpm_remove(self, package)
        pass
