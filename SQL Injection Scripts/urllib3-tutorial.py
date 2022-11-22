import urllib3

print(urllib3.__version__)

http = urllib3.PoolManager()
url = 'http://webcode.me'

# GET request
resp = http.request('GET', url)

print(resp.status)
# print(resp.data.decode('utf-8'))

# HEAD request
resp = http.request('HEAD', url)

print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.headers['Content-Type'])
print(resp.headers['Last-Modified'])

import certifi

print(certifi.where())

url = "https://httpbin.org/anything"

http = urllib3.PoolManager(ca_certs = certifi.where()) 
resp = http.request("GET", url)

# print(resp.status)
import sys
print(sys.version)










