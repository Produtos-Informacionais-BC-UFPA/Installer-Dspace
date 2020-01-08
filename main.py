import os
from javaInstall import *
from ant_mvnInstall import *
from gitInstall_clone import *
from psqlInstall import *
from check_installed import *
from tomcatInstall import *
from checkUser import *

os.system('apt update')
#install_java()
#mvn_install()
#ant_install()
verifyAndInstall("java")
verifyAndInstall("ant")
verifyAndInstall("mvn")
verifyAndInstall("git")
verifyAndInstall("postgres")

checkUserExist()
os.system('cd /home/dspace')
os.system ('su - dspace')
os.system('cd /home/dspace')
gitClone_6_3()
s = createDB_createUser()
os.system('su')
os.system('chmod -R 777 /home/dspace/DSpace') #revisar esta  etapa. Se eh este o caminho mesmo
os.system('cd DSpace/')


#revisar esses passos
os.system("cp DSpace/dspace/config/local.cfg.EXAMPLE home/dspace/DSpace")
os.system("mv local.cfg.EXAMPLE local.cfg")
cmd = "sed -i 's/db.password=dspace/db.password="+s+"/'"
#cmd2 = "home/ramon/Documentos/teste"
cmd2 = "home/dspace/DSpace"
cmd_final = cmd+cmd2
os.system(cmd_final) #insere senha do banco no local.cfg

# NA LINHA ABAIXO TEM QUE PEGAR O PASSWORD DO BD E PASSAR PARA A VARIAVEL
#os.system("sed 'Ns/.*/db.password=' /home/dspace/Dspace/local.cfg ")
#os.system("sed -i 's/db.password=dspace/db.password=testesenhada/g' /home/dspace/Dspace/local.cfg") #ve se o direitorio ta certo(nome)
os.system("mvn clean")
os.system("mvn -U package")
os.system("cd dspace/target/dspace-installer")
os.system("ant fresh_install")


#configuracao de administradores
os.system("cd /")
os.system("dspace/bin/dspace  create-administrator")
print ("administrador criado")
