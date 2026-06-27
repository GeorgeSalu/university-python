import requests

# enviando cookies
cookies = {'session_id': 'xyz123'}
response = requests.post('https://httpbin.org/post', cookies=cookies)
print(response.json())
