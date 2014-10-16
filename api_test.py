import requests

url = "http://api.asg.northwestern.edu/terms/"
params = { "key": "UpUSvz66ynDAYYTy" }

request = requests.get(url, params=params)

print request.json()
