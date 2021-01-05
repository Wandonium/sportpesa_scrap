import requests
url = 'https://api.github.com'

#First Request
results = requests.get(url)
print("Status Code: ", results.status_code)
print("Headers: ", results.headers)

#Second Request
etag = results.headers['ETag']
print("ETag: ", etag)

results = requests.get(url, headers={'If-None-Match': etag})
print("Status Code: ", results.status_code)