#!/usr/bin/python3
import cgi
import subprocess as s
import time
    
print("content-type: text/html")
print( )
y = cgi.FieldStorage()
x = y.getvalue("X")
time.sleep(1)
	
z=s.getoutput("sudo "+"kubectl "+x+" --kubeconfig /root/kubetask9/admin.conf")
        
print(z)
