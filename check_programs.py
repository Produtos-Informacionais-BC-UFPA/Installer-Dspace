import os

def check_java():
   jv = os.system('java -version')

def check_ant():
    ant_c = os.system('ant -version')

def check_mvn():
    mvn_c = os.system('mvn -version')


def check_git():
    git_c = os.system('git --version')