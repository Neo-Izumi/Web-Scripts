import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080' , 'https': 'http://127.0.0.1:8080'}

#problem: there is a crfs token is created whenever we send a request so that 400 code is returned 

def main():
    url = 'https://0ab900e004afe953c089d96b008b0022.web-security-academy.net/login'
    data = {'username': 'carlos', 'password': 'montoya'}
    r = requests.post(url = url, data = data)
    print(r.status_code)

if __name__ == '__main__':
    main()

