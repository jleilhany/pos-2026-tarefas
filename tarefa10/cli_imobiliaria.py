import json

# carregar o JSON
with open('imobiliaria.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

imoveis = dados["imoveis"]

while True:
    print("\n===== MENU DE IMÓVEIS =====")

    # mostrar lista com IDs
    for i, imovel in enumerate(imoveis):
        print(f"{i} - {imovel['descricao']}")

    print("X - Sair")

    escolha = input("\nDigite o ID do imóvel: ")

    if escolha.lower() == 'x':
        print("Encerrando...")
        break

    if not escolha.isdigit():
        print("Entrada inválida!")
        continue

    escolha = int(escolha)

    if escolha < 0 or escolha >= len(imoveis):
        print("ID inválido!")
        continue

    imovel = imoveis[escolha]

    print("\n===== DETALHES DO IMÓVEL =====")
    print(f"Descrição: {imovel['descricao']}")
    
    print("\n--- Proprietário ---")
    print(f"Nome: {imovel['proprietario']['nome']}")
    print(f"Email: {imovel['proprietario']['email'] or 'Não informado'}")
    print("Telefones:", ", ".join(imovel['proprietario']['telefones']))

    print("\n--- Endereço ---")
    print(f"Rua: {imovel['endereco']['rua']}")
    print(f"Bairro: {imovel['endereco']['bairro']}")
    print(f"Cidade: {imovel['endereco']['cidade']}")
    print(f"Número: {imovel['endereco']['numero'] or 'Não informado'}")

    print("\n--- Características ---")
    print(f"Tamanho: {imovel['caracteristicas']['tamanho']}")
    print(f"Quartos: {imovel['caracteristicas']['numQuartos']}")
    print(f"Banheiros: {imovel['caracteristicas']['numBanheiros']}")

    print(f"\nValor: R$ {imovel['valor']}")