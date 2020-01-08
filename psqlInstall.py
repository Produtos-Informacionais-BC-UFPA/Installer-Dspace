import os
import pwd
from getpass import getpass

#DEPOIS RENOMEAR ESTE ARQUIVO

def psql_install():
    os.system('apt install postgresql postgresql-contrib')


def createDB_createUser():
    uid_ps = pwd.getpwnam('postgres')[2]
    os.setuid(uid_ps)

    print(" criando banco de dados ...")
    os.system('createuser --username=postgres --no-superuser --pwprompt dspace')
    pw_psql = getpass("Repetir senha: ")
    os.system('createdb --username=postgres --owner=dspace --encoding=UNICODE dspace')
    os.system('psql --username=postgres dspace -c "CREATE EXTENSION pgcrypto;"')
    print("Banco de Dados criado com Sucesso! -----------***")

    '''
    os.system('su - postgres')
    os.system('createuser --username=postgres --no-superuser --pwprompt dspace')
    os.system('createdb --username=postgres --owner=dspace --encoding=UNICODE dspace')
    a = input("digite novamente a senha*")
    os.system('psql --username=postgres dspace -c "CREATE EXTENSION pgcrypto;"')
    return a
    '''