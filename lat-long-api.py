import requests
url = 'https://api.sunrise-sunset.org/json?lat=-1.2841&lng=36.8155&date=2020-11-09'

results = requests.get(url)
print("Status Code: ", results.status_code)
print("Headers-ContentType: ", results.headers['Content-Type'])
print("Headers: ", results.headers)

jsonResult = results.json()
print("Type JSON results", type(jsonResult))
print(jsonResult)
print("SunRise & Sunset: ", jsonResult['results']['sunrise'], " & ", jsonResult['results']['sunset'])