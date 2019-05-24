#!/usr/local/bin/python3

import urllib.request
import urllib.parse
import sys

if (len(sys.argv)>1):
  headers={'apikey':'6a85f78e5cd9a7eccae9333361f3cbd798ee1e8c70bad9dfeb027f345e562d2d'}

  url="https://api.paloaltonetworks.com/api/license/get"

  values={'authCode':'I7900710'}

  data=urllib.parse.urlencode(values)
  data = data.encode('ascii')

  req = urllib.request.Request(url, data, headers)
  response=urllib.request.urlopen(req)
  res=str(response.read())


#Get Status
for i in res.split(','): 
   print (i) 
