import requests

# URL da API
url = "http://localhost:3000/profissionais"

# Dados do profissional para cadastro
payload = {
    "nome": "João Silva",
    "empresa": "Empresa A"
}

# Enviar requisição POST
response = requests.post(url, json=payload)

# Verificar o status da resposta
if response.status_code == 201:
    print("Teste PASS: Status 201 recebido.")
else:
    print(f"Teste FAIL: Status {response.status_code} recebido.")

# Verificar o corpo da resposta
expected_data = {
    "id": 1,
    "nome": "João Silva",
    "empresa": "Empresa A"
}

if response.json() == expected_data:
    print("Teste PASS: Dados do profissional corretos.")
else:
    print("Teste FAIL: Dados do profissionais incorretos.")