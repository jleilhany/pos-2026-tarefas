import requests

BASE_URL = "http://localhost:8000/users/"

def list():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        return response.json()

    return {"erro": response.status_code}


def create(data):
    response = requests.post(BASE_URL, json=data)

    if response.status_code in [200, 201]:
        return response.json()

    return {"erro": response.status_code}


def read(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")

    if response.status_code == 200:
        return response.json()

    return {"erro": response.status_code}


def update(user_id, data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=data)

    if response.status_code == 200:
        return response.json()

    return {"erro": response.status_code}


def delete(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")

    if response.status_code == 200:
        return {"mensagem": "Usuário deletado com sucesso"}

    return {"erro": response.status_code}