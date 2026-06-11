import requests
from xml.dom import minidom

URL = "https://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"


def country_name(codigo):
    soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{codigo}</sCountryISOCode>
        </CountryName>
      </soap:Body>
    </soap:Envelope>"""

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CountryName"
    }

    try:
        resposta = requests.post(URL, data=soap_body, headers=headers, timeout=10)

        print("\nStatus:", resposta.status_code)

        xml = minidom.parseString(resposta.text)
        resultado = xml.getElementsByTagName("m:CountryNameResult")

        if resultado and resultado[0].firstChild:
            print("Nome do país:", resultado[0].firstChild.nodeValue)
        else:
            print("Não foi possível encontrar o país.")

    except Exception as e:
        print("Erro ao conectar à API:")
        print(e)


def capital_city(codigo):
    soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{codigo}</sCountryISOCode>
        </CapitalCity>
      </soap:Body>
    </soap:Envelope>"""

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CapitalCity"
    }

    try:
        resposta = requests.post(URL, data=soap_body, headers=headers, timeout=10)

        print("\nStatus:", resposta.status_code)

        xml = minidom.parseString(resposta.text)
        resultado = xml.getElementsByTagName("m:CapitalCityResult")

        if resultado and resultado[0].firstChild:
            print("Capital:", resultado[0].firstChild.nodeValue)
        else:
            print("Não foi possível encontrar a capital.")

    except Exception as e:
        print("Erro ao conectar à API:")
        print(e)


def country_currency(codigo):
    soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{codigo}</sCountryISOCode>
        </CountryCurrency>
      </soap:Body>
    </soap:Envelope>"""

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CountryCurrency"
    }

    try:
        resposta = requests.post(URL, data=soap_body, headers=headers, timeout=10)

        print("\nStatus:", resposta.status_code)

        xml = minidom.parseString(resposta.text)

        nome = xml.getElementsByTagName("m:sName")
        codigo_moeda = xml.getElementsByTagName("m:sISOCode")

        if nome and codigo_moeda:
            print("Moeda:", nome[0].firstChild.nodeValue)
            print("Código da moeda:", codigo_moeda[0].firstChild.nodeValue)
        else:
            print("Não foi possível encontrar a moeda.")

    except Exception as e:
        print("Erro ao conectar à API:")
        print(e)


while True:
    print("\n=== MENU ===")
    print("1 - Nome do País")
    print("2 - Capital")
    print("3 - Moeda")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    codigo = input(
        "Digite o código ISO do país (BR, US, AR, FR...): "
    ).upper()

    if opcao == "1":
        country_name(codigo)

    elif opcao == "2":
        capital_city(codigo)

    elif opcao == "3":
        country_currency(codigo)

    else:
        print("Opção inválida!")