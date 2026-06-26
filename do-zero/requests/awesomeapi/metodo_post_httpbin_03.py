import requests

payload = {'titulo': 'Python', 'status': 'ativo'}
response = requests.post('https://httpbin.org/post', json=payload)
print(response.json())