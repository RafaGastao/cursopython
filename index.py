# # Conversão de Tipos

# primeiro_valor = int(input("Digite o primeiro valor: "))

# segundo_valor = int(input("Digite o segundo valor: "))

# print(f'A soma dos valores são: {primeiro_valor +segundo_valor}')

# print("Bem vindo à Lanchonete Vai No Lanche")

# lanche_cliente = input("Digite o lanche que você gostaria:")

# bebida_cliente = input("Digite a bebida que você gostaria:")

# valor_lanche = float(input("Digite o valor do lanche:"))

# valor_bebida = float(input("Digite o valor da bebida:"))

# print(f'O valor total que você irá pagar é: {valor_lanche + valor_bebida}')

# Condicionais --> Elas são as responsáveis por executarem um determinado bloco de código, baseado em uma ou mais respostas específicas

# Condicionais Simples
# Pergunta ? executa uma ação do tipo A se não: executa uma ação do tipo b

saldo = False

if saldo == False:
    print("Tá lascado!!")
    print("Faço parte da estrutura do if")

#Condicionais Compostas
idade = 18

if saldo == True and idade >= 18:
    print("Uhuuul, você pode mandar um pix aos seus instrutores!!! ")
else:
    print("Infelizmente você não pode mandar um pix para seus instrutores")

#Condicionais Alinhadas

jantar = "Strogonoff de Frango"
bebida = "Guaraná"

if jantar == "Churrasco acompanhodo de fritas e farofa" and bebida == "Coca-cola":
    print("Partiu Churrascada!!!")
elif jantar == "Strogonoff de Frango" and bebida =="Guaraná":
    print("Partiuuuuu comer Strogonoff")
else: 
    print("Deixo para próxima!")

# Operadoes Lógicos e Operadores de Comparação em Python

# JavaScript -> &, ||, !
# Python -> and, or, not

# and (e) -> retorna True  se uma senteça E outra e  verdadeira (Eu quero Batata Frita e Coca-cola)

# or (ou) -> retorna True se uma das duas setenças for verdadeira (Ou eu quero batatas fritas ou Coca-cola)

# not (negação) -> retorna True se a setença for falsa