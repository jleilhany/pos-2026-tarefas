import xml.etree.ElementTree as ET
import json

# Carregar o XML
tree = ET.parse('imobiliaria.xml')
root = tree.getroot()

dados = {"imoveis": []}

for imovel in root.findall('imovel'):
    imovel_dict = {}

    # descrição
    imovel_dict["descricao"] = imovel.findtext('descricao', '').strip()

    # proprietário
    proprietario = imovel.find('proprietario')
    telefones = [t.text.strip() for t in proprietario.findall('telefone') if t.text]

    imovel_dict["proprietario"] = {
        "nome": proprietario.findtext('nome', '').strip(),
        "email": proprietario.findtext('email', '').strip(),
        "telefones": telefones
    }

    # endereço
    endereco = imovel.find('endereco')
    imovel_dict["endereco"] = {
        "rua": endereco.findtext('rua', '').strip(),
        "bairro": endereco.findtext('bairro', '').strip(),
        "cidade": endereco.findtext('cidade', '').strip(),
        "numero": endereco.findtext('numero', '').strip() if endereco.find('numero') is not None else None
    }

    # características
    carac = imovel.find('caracteristicas')
    imovel_dict["caracteristicas"] = {
        "tamanho": carac.findtext('tamanho', '').strip(),
        "numQuartos": carac.findtext('numQuartos', '').strip(),
        "numBanheiros": carac.findtext('numBanheiros', '').strip()
    }

    # valor
    imovel_dict["valor"] = imovel.findtext('valor', '').strip()

    dados["imoveis"].append(imovel_dict)

# Salvar JSON
with open('imobiliaria.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("Arquivo imobiliaria.json criado com sucesso!")