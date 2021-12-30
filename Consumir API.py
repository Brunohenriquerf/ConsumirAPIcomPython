import requests

# Acessar e retornar valores
url = "https://jsonplaceholder.typicode.com/todos/15"
response = requests.get(url)
print("Antigo: ", response.json())
# Atualizar valores
minha_lista = {"userId": 13, "title": "Pudim de frango", "completed": True}
response = requests.put(url, json=minha_lista)
print("Código: ", response.status_code) # Documentação, https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
# Visualizar novamente, para checar a atualização
print("Novo: " ,response.json())
