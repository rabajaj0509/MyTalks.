import json
import requests

def showpaste(pasteid):
    resp = requests.get("http://paste.fedoraproject.org/api/json/{0}".format(pasteid))
    if resp.status_code == 200:
        get_data = json.loads(resp.text)
        #print(get_data)
        for i in get_data['result']:
            print(i+":"+get_data['result'][i])
    else:
        print(resp.status_code)

if __name__ == '__main__':
    showpaste(430456)
