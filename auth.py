#!/usr/local/bin/python3

import urllib.request
import urllib.parse
import ssl
import sys
import getpass

#return response
def resp(host):
  data={}
  data['user']=input('username: ')
  data['password']=getpass.getpass('Password: ')

  data['type']='keygen'

  url_values=urllib.parse.urlencode(data)

  url="https://"+host+"/api/"

  full_url=url+'?'+url_values


  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  response=urllib.request.urlopen(full_url,context=ctx)
  res=response.read().decode()
  return res

#Get authkey
def returnkey(host):
 if (len(sys.argv)>1): 
  return resp(host).split("</key>")[0].split('<key>')[1]
 else:
  print ("Usage: python3 auth.py hostname or IP address of the VM Firewall\n Eg. python3 auth.py 10.129.128.70")

#print(returnkey(sys.argv[1]))
