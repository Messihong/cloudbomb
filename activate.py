import urllib.request
import urllib.parse
import ssl
import sys

from auth import *
from cpuid import *

def activate():
  
   if (len(sys.argv)>1):
        identity=returnid()
        cpuid=identity['cpuid']
        uuid=identity['uuid']

        url="https://api.paloaltonetworks.com/api/license/activate"
        
        authcode=input("Authcode: ")
        values={'authCode':authcode,"cpuid":cpuid,"uuid":uuid}
        headers={'apikey':'6a85f78e5cd9a7eccae9333361f3cbd798ee1e8c70bad9dfeb027f345e562d2d'}
        data=urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data, headers)
        response=urllib.request.urlopen(req)
        res=response.read().decode()
        print(res)
        refresh()
#fetch license and reload the firewall

def refresh():

    reqlic='<request><license><fetch/></license></request>'
    if(len(sys.argv)<2): 
      para['authkey']=returnkey(sys.argv[1]) 
      fullpath('op',reqlic,host)
      url="https://"+sys.argv[1]+"/api/"
      full_url=url+'?'+url_values
      url_values=urllib.parse.urlencode(para)
    
activate()
#<request cmd="op" cookie="8069740939447295" uid="500"><operations><request><license><fetch/></license></request></operations></request>

