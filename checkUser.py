import os

def checkUserExist():
    a = os.system("grep -c 'dspace:' /etc/passwd")
    if (a==0):
        createUser()
    else:
      return a

def createUser():
    os.system('useradd -m dspace')

