# teste_env.py
from dotenv import load_dotenv
import os

print("=== TESTE DO .env ===\n")

# Carrega o .env com override
load_dotenv(override=True)

# Verifica se carregou
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

print(f"CLIENT_ID: {client_id}")
print(f"CLIENT_SECRET: {client_secret[:10] if client_secret else 'Não encontrado'}...")

# Tenta ler o arquivo diretamente
print("\n--- LENDO ARQUIVO DIRETAMENTE ---")
try:
    with open('.env', 'r') as f:
        conteudo = f.read()
        print(f"Conteúdo do .env:\n{conteudo}")
except Exception as e:
    print(f"Erro ao ler: {e}")

# Verifica o caminho atual
print(f"\nPasta atual: {os.getcwd()}")
print(f"Arquivo .env existe? {os.path.exists('.env')}")