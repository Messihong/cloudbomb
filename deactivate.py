#!/usr/local/bin/python3

import ssl
import urllib.request
import urllib.parse
import sys
from cpuid import *
from auth import *

para={}
#full_url=""
#url=""
identity={}
host=sys.argv

#'<show><system><info></info></system></show>'
     
def deactivate():

 if(len(host)>1):

  deactivation='<request><license><deactivate><VM-Capacity><mode>auto</mode></VM-Capacity></deactivate></license></request>'

  #No cert validation
  ctx = ssl.create_default_context()
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  response=urllib.request.urlopen(fullpath('op',deactivation,host),context=ctx)

  #Get CPUID and UUID

  res=response.read().decode()
  return res 
 
 else:
  print ("Usage: python3 auth.py hostname or IP address of the VM Firewall\n Eg. python3 auth.py 10.129.128.70")


print(deactivate())
