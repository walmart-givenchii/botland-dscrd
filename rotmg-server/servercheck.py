import urllib.request, json
import time
def statuscheck(servername)
    with urllib.request.urlopen("http://www.tiffit.net/RealmInfo/api/servers") as url:
        sd = json.loads(url.read().decode())
        
