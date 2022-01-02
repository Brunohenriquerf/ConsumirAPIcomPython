import requests

# Acessar e retornar valores
url = "https://jsonplaceholder.typicode.com/todos/15"
response = requests.get(url)
print("Antigo: ", response.json())
# Atualizar valores
minha_lista = {"userId": 13, "id": 13, "title": "Pudim de frango com barbecue", "completed": True}
response = requests.put(url, json=minha_lista)
# Documentação https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
print("Deu certo, segue abaixo a informação atualizada:") if response.status_code == 200 else print("Algo deu errado, a informação não foi alterada:")
# Visualizar novamente, para checar a atualização
print("Novo: " ,response.json())
