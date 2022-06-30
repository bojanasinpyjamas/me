import requests
import json

url = "https://data.nsw.gov.au/data/api/3/action/package_show?id=2f7ce69d-e82e-4a2d-b6bd-d94b47d7cd66"

r = requests.get(url)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print(json.dumps(the_json, indent=4))
else:
    print(r)
