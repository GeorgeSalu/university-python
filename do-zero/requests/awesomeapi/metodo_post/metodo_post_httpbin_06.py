import requests

payload = {'dados': 'teste'}
try:
    response = requests.post('https://httpbin.org/post', json=payload, timeout=5)
    print(response.status_code)
except requests.exceptions.Timeout:
    print('A requisição excedeu o tempo limite.')