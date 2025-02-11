# 2015 -> Relatório IDC -> International Data Corporation patrocinado pela Seagate, 2015 eles informaram que cada pessoa na terra, que possui acesso a internet,seja por rede sociais,mecanismos de pesquisa,interações na web,ligações via internet... produzia 1,3 GB por dia.

#Arrays --> São estruturas que conseguem guardar uma quantidade imensa de informação, porém de forma desergozinada.

lista_dos_sonhos = ["Subitamente receber uma quantia inigulável de papel moeda na conta.", "PC Gamer com luzinha e tudo.", "Um emprego Google", "Marka Zuckeberga","Trabalhar para o Elon Musk","Meu sonho e aposentar sem calvície"]

print(lista_dos_sonhos)
print(lista_dos_sonhos[0],lista_dos_sonhos[4])
print(type(lista_dos_sonhos))
print(type(lista_dos_sonhos[0]))

# Indexação Negativa
print(lista_dos_sonhos[-1])
print(lista_dos_sonhos[-2])


# Métodos de Listas

# insert -> Adiciona uma informação em nossa lista no local especifico que a gente quiser

lista_dos_sonhos.insert(0,"Que a Fernanda pague todo mundo que deve")

#append -> Adiciona uma informação ao final da nossa lista

lista_dos_sonhos.append("Viajar o mundo")
lista_dos_sonhos.append("Dodge Ram")

print(lista_dos_sonhos)

# sort -> Ordena as informações da nossa lista em formato alfanúmerica, alfabetica, crescente e decrescente

nomes= ["Plinio", "Camila", "Julia","Alisson", "Luis Otavio", "George", "Évila", "Rafael"]

nomes.sort()
nomes.sort(reverse=True)

print(nomes)

# remove --> Retira a informação que definirmos do nossa lista

nomes.remove("Plinio")
nomes.remove("Évila")

print(nomes)

# pop --> Retira a informação baseado no índice que colocarmos

nomes.pop(0)
nomes.pop(-1)

print(nomes)


#---------------
print("Bem Vindo ao Vai no Lanche")

senha_correta = "1234"

senha = ""
while senha != senha_correta:
    senha = input("Por favor, digite a senha para fazer seu pedido: ")
    if senha != senha_correta:
        print("Senha incorreta, tente novamente")
print("Senha Correta, pode fazer seu pedido.")





pedidos = []
qntd_pedidos = int(input("Boa noite, caro(a) cliente quantos pedidos deseja fazer: "))

while len(pedidos) < qntd_pedidos:
    pedidos.append(input(f"Digite o seu {len(pedidos)+1} pedido: "))

print(f'O seus pedidos foram{pedidos} em até 1 hora chegarão a sua residência')
