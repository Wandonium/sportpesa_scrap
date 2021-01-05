import requests
import json
dataSet = []

def readUrl(search):
    results = requests.get(url+search)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    return results.json()

url = 'http://universities.hipolabs.com/search?name='
jsonResult = readUrl('Wales')

for university in jsonResult:
    name = university['name']
    url = university['web_pages'][0]
    dataSet.append([name, url])

print("Total Universities found: ", len(dataSet))
print(dataSet)