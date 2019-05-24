#!/usr/local/bin/python3

import ssl
import urllib.request
import urllib.parse
import sys

from auth import *

para={}
#full_url=""
#url=""
identity={}
host=sys.argv

def fullpath(apitype,cmd,host):
  para['key']=returnkey(host[1])
  para['type']=apitype
  para['cmd']=cmd
  url_values=urllib.parse.urlencode(para)
  url="https://"+host[1]+"/api/"
  full_url=url+'?'+url_values
  return full_url


#'<show><system><info></info></system></show>'
     
def cpuid():
 if(len(host)>1):

  systeminfo='<show><system><info></info></system></show>'

  #No cert validation
  ctx = ssl.create_default_context()
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  response=urllib.request.urlopen(fullpath('op',systeminfo,host),context=ctx)

  #Get CPUID and UUID

  res=response.read().decode()
  identity['uuid']=res.split('</vm-uuid>')[0].split('<vm-uuid>')[1]
  identity['cpuid']=res.split('</vm-cpuid>')[0].split('<vm-cpuid>')[1]
  return identity 
 
 else:
  print ("Usage: python3 auth.py hostname or IP address of the VM Firewall\n Eg. python3 auth.py 10.129.128.70")

def returnid():
    return cpuid()

#print(returnid())
