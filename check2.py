import subprocess
import os
import logging
import traceback
import sys

def is_tool(name):
    try:
        #devnull = open(os.devnull)
        #subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
        jv = os.system(name+' -version')
        print ("isto e: "+jv)
        #jv = jv.lower()
        if name in jv:
            return True
    except: #OSError as e:
        #loggin.error("Not FOUND!")
        return False
        #return False
        #if e.errno: #=="sh: 1: "+ name + ":" + " not found": 
        #os.errno.ENOENT:
        #    return False
    return True

