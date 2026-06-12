import requests
from xml.dom import minidom

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

while True:
    print("\n=== MENU ===")
    print("1 - Moeda do País")
    print("2 - Nome do País")
    print("3 - Capital do País")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    codigo = input(
        "Digite o código do país (BR, US, AR, FR e etc): "
    ).upper()

    if opcao == "1":

        payload = f"""
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{codigo}</sCountryISOCode>
                </CountryCurrency>
            </soap:Body>
        </soap:Envelope>
        """

        response = requests.post(
            url,
            headers={"Content-Type": "text/xml; charset=utf-8"},
            data=payload
        )

        xml = minidom.parseString(response.text)

        moeda_codigo = xml.getElementsByTagName("m:sISOCode")[0].firstChild.nodeValue
        moeda_nome = xml.getElementsByTagName("m:sName")[0].firstChild.nodeValue

        print("Código da moeda:", moeda_codigo)
        print("Nome da moeda:", moeda_nome)

    elif opcao == "2":

        payload = f"""
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{codigo}</sCountryISOCode>
                </CountryName>
            </soap:Body>
        </soap:Envelope>
        """

        response = requests.post(
            url,
            headers={"Content-Type": "text/xml; charset=utf-8"},
            data=payload
        )

        xml = minidom.parseString(response.text)

        pais = xml.getElementsByTagName(
            "m:CountryNameResult"
        )[0].firstChild.nodeValue

        print("Nome do país:", pais)

    elif opcao == "3":

        payload = f"""
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{codigo}</sCountryISOCode>
                </CapitalCity>
            </soap:Body>
        </soap:Envelope>
        """

        response = requests.post(
            url,
            headers={"Content-Type": "text/xml; charset=utf-8"},
            data=payload
        )

        xml = minidom.parseString(response.text)

        capital = xml.getElementsByTagName(
            "m:CapitalCityResult"
        )[0].firstChild.nodeValue

        print("Capital:", capital)

    else:
        print("Opção inválida!")