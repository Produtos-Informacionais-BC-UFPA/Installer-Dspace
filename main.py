import os
from javaInstall import *
from ant_mvnInstall import *
from gitInstall_clone import *
from psqlInstall import *
from check_installed import *

os.system('apt update')
#install_java()
#mvn_install()
#ant_install()
verifyAndInstall("java")
verifyAndInstall("ant")
verifyAndInstall("mvn")
verifyAndInstall("git")
verifyAndInstall("postgres")


os.system('useradd -m dspace')
os.system('cd /home/dspace')

gitClone_6_3()