import argparse
import users_wrapper as users


parser = argparse.ArgumentParser(description="CLI para CRUD de usuários")

parser.add_argument("acao", choices=[
    "list",
    "create",
    "read",
    "update",
    "delete"
])

parser.add_argument("--id", type=int)
parser.add_argument("--name")
parser.add_argument("--email")

args = parser.parse_args()


if args.acao == "list":
    resultado = users.list()
    print(resultado)

elif args.acao == "create":
    dados = {
        "name": args.name,
        "email": args.email
    }

    resultado = users.create(dados)
    print(resultado)

elif args.acao == "read":
    resultado = users.read(args.id)
    print(resultado)

elif args.acao == "update":
    dados = {
        "name": args.name,
        "email": args.email
    }

    resultado = users.update(args.id, dados)
    print(resultado)

elif args.acao == "delete":
    resultado = users.delete(args.id)
    print(resultado)