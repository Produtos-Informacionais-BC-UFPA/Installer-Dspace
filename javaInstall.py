import os

def wget_java():
    os.system("wget http://security.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jdk-headless_8u191-b12-2ubuntu0.18.10.1_amd64.deb")
    os.system("wget http://security.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jdk_8u191-b12-2ubuntu0.18.10.1_amd64.deb")
    os.system("wget http://security.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre_8u191-b12-2ubuntu0.18.10.1_amd64.deb")
    os.system("wget http://security.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre-headless_8u191-b12-2ubuntu0.18.10.1_amd64.deb")

def install_java():
    wget_java()
    os.system("dpkg -i openjdk-8-jre-headless_8u191-b12-2ubuntu0.18.10.1_amd64.deb openjdk-8-jre_8u191-b12-2ubuntu0.18.10.1_amd64.deb openjdk-8-jdk_8u191-b12-2ubuntu0.18.10.1_amd64.deb openjdk-8-jdk-headless_8u191-b12-2ubuntu0.18.10.1_amd64.deb")    

def set_JAVAHOME():
    os.syste("export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java")    