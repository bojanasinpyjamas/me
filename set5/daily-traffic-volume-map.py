import requests
import json

url = (
    "https://data.nsw.gov.au/data/dataset/interactive-average-daily-traffic-volume-map"
)

r = requests.get(url)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print(json.dumps(the_json, indent=4))
else:
    print(r)
