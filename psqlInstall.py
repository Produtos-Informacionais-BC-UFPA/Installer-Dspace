import os

#DEPOIS RENOMEAR ESTE ARQUIVO

def psql_install():
    os.system('apt install postgresql postgresql-contrib')


def createDB_createUser():
    os.system('sudo su - postgres')
    os.system('createuser --username=postgres --no-superuser --pwprompt dspace')
    os.system('createdb --username=postgres --owner=dspace --encoding=UNICODE dspace')
    a = input("digite novamente a senha*")
    os.system('psql --username=postgres dspace -c "CREATE EXTENSION pgcrypto;"')
    return a