import requests
import json

from setting import API_KEY

def menu_url(lat, lon):
    url = "https://developers.zomato.com/api/v2.1/geocode?lat={0}&lon={1}".format(lat, lon)
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": API_KEY}

    resp = requests.get(url, headers=header)
    #print(resp)
    resp_status = resp.status_code
    if resp_status == 200:
        get_data = json.loads(resp.text)
        for i in get_data['nearby_restaurants']:
            name = i['restaurant']['name']
            print(name)

menu_url(28.6353, 77.225)


