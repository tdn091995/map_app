import requests
import json
def getLocation():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    ip = j['ip']
    latlon = str(lat) + ', ' + str(lon)
    return latlon
print(getLocation())
