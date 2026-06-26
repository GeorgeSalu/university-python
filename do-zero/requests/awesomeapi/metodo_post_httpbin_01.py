import requests

response = requests.post('https://httpbin.org/post')
print(response.json())