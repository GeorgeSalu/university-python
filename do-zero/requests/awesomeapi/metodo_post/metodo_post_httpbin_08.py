import requests

sessao = requests.Session()
sessao.headers.update({'x-app-id': '12345'})
response = sessao.post('https://httpbin.org/post', data={'chave': 'valor'})
print(response.json())
