import requests

response = requests.post('https://httpbin.org/post', auth=('user', 'pass'))
print(response.status_code)