import subprocess
from javaInstall import *
from ant_mvnInstall import *
from gitInstall_clone import *
from psqlInstall import *
from check_installed import *

def is_installed(name):
    rc = subprocess.call(['which', name])
    if rc == 0:
        #print (name+' installed!')
        return True
    else:
        #print (name+' missing in path!')
        return False


#a = is_installed('git')
#print (a)

def verifyAndInstall(name)
    a = is_installed(name)
    if (a==False):
        if(name=="java"):
            install_java()
        if(name=="ant"):
            ant_install()
        if(name=="mvn"):
            mvn_install
        if(name=="postgres"):
            psql_install()
        if(name=="git"):
            install_git()

