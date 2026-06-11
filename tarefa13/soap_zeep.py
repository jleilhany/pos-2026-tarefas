from zeep import Client

# URL do WSDL
wsdl = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# Cria o cliente SOAP
client = Client(wsdl)

# Solicita o número ao usuário
numero = int(input("Digite um número inteiro: "))

# Chama o método NumberToWords
resultado = client.service.NumberToWords(numero)

# Exibe o resultado
print(f"Número digitado: {numero}")
print(f"Por extenso em inglês: {resultado}")