from xml.dom import minidom 

doc = minidom.parse("cardapio.xml")

pratos = doc.getElementsByTagName("prato")

for prato in pratos: 
    id_prato = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome") [0].firstChild.data
    print(f"{id_prato}-{nome}")

id_escolhido = input("digite o id do prato para saber mais: ")

for prato in pratos:
    if prato.getAttribute("id") == id_escolhido:
        nome = prato.getElementsByTagName("nome")[0].firstChild.data
        