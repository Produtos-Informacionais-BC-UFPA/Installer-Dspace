import os

def checkUserExist():
    a = os.system("grep -c 'dspace:' /etc/passwd")
    #print "valor de: "+a
    if (a==0):
        createUser()
    else:
      return a

def createUser():
    os.system('useradd -m dspace')
    
