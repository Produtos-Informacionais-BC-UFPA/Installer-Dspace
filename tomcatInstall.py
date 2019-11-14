import os


def tomcat_install():
    os.system("mkdir /var/www/")
    os.system("wget http://mirror.nbtelecom.com.br/apache/tomcat/tomcat-9/v9.0.27/bin/apache-tomcat-9.0.27.tar.gz")
    os.system("cd /var/www")
    os.system("zxvf apache-tomcat-9.0.27 ")