# Funções --> Organizar melhor o código, reutilizar o códigos, esperar uma ação, executar blocos de códigos

# def nome_da_função():
#     ação_a_ser_executada

# def lista_compras():
#     print("Comprar leite em pó")
# lista_compras()

# login = input("Digite seu e-mail: ")
# senha = int(input("Digite sua senha: "))

# def boas_vidas():
#     print(f"Boas vindas, {login} aproveite que nosos site está em promoçaõ de 50% do valor, do frete")

# def login_invalido():
#     print("Tente novamente, suas credenciais estão invalidas!")

# if login == "rafaelgastao14@gmail.com" and senha == 123:
#     boas_vidas()
# else:
#     login_invalido()

# Dicionários em Python

# () -> Utiliza quando queremos guardar informações que não podem ser modificadas (quartinho com corrente e cadeado)

# [] -> Quando queremos guardar uma quantidade quase infinita de informação, porém não organizada (quartinho da bagunça)

# {} -> Quando queremos guardar uma quantidade quase infinita de informação, de forma organizada (quartinho organizado em prateleiras)

nomes_cliente = {
    'cliente_rj':'Kauã',
    'cliente_mg':['Alisson'],
    'cliente_pa':'Haydee',
    'cliente_pe':'Nat',
    'cliente_ba':'Jeferson',
    'cliente_sp':'Leandra',
    'cliente_df':'Karyne',
    'cliente_al':'Camila',
    'cliente_ce':'Renato',
    'cliente_se':'Évila'
}

# Cada chave deve ser única, não pode ter chaves repetidas

print(nomes_cliente)

# Alterar uma informação de um dicionário

nomes_cliente['cliente_sp'] = "Rafael"

print(nomes_cliente)

# Adicionar uma nova chave de valor

nomes_cliente.update({'cliente_são_gonçalo': 'Mariana'})

print(nomes_cliente)

# deleta uma informação do dicionário

del nomes_cliente['cliente_rj']

print(nomes_cliente)

# adicionando informação em uma chave que contém uma lista

nomes_cliente['cliente_mg'].append("Mônica")

print(nomes_cliente)

# for fofoqueiro in local:

for clientes in nomes_cliente.values():
    print(clientes)