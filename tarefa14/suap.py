import requests
from getpass import getpass


api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {
    "username": user,
    "password": password
}

response = requests.post(
    api_url + "token/pair",
    json=data
)

token = response.json()["access"]

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    api_url + "ensino/meu-boletim/2025/1/",
    headers=headers
)

print(response.json())

dados = response.json()

print(f"{'DISCIPLINA':60} {'MÉDIA':>6} {'FALTAS':>6} {'SITUAÇÃO':>12}")
print("-" * 90)

for item in dados["results"]:
    disciplina = item["disciplina"][:60]
    media = item["media_disciplina"]
    faltas = item["numero_faltas"]
    situacao = item["situacao"]

    print(f"{disciplina:60} {media:>6} {faltas:>6} {situacao:>12}")

