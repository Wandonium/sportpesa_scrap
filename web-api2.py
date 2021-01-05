import requests
import json
from collections import Counter
dataSet = []

url = 'https://api.github.com/'


def readUrl(search):
    results = requests.get(url+search)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    return results.json()

if __name__ == "__main__":
    eventTypes = []
    for page in range(1, 4):    #First 3 pages
        events = readUrl('events?page=' + str(page))

        for event in events:
            id = event['id']
            type = event['type']
            actor = event['actor']['display_login']
            repoUrl = event['repo']['url']
            createdAt = event['created_at']
            eventTypes.append(type)
            dataSet.append([id, type, createdAt, repoUrl, actor])
        
    eventInfo = dict(Counter(eventTypes))

    print("Individual Event Counts: ", eventInfo)
    print("CreateEvent counts: ", eventInfo['CreateEvent'])
    print("PushEvent counts: ", eventInfo['PushEvent'])

print("Total Events Found: ", len(dataSet))
print(dataSet)