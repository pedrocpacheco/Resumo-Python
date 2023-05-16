def crete_account():
    name = input("Digite o seu nome:")
    cpf = input("Digite o seu CPF:")
    account = {
        "name": name,
        "cpf": cpf
    }
    return account