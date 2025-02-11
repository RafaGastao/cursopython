# Loops -> São estruturas de código que repetem determinada ação, enquanto um condição não for concluída.

# while

pessoas = 2

while pessoas < 100:
    print(f"A instrutorissima Fernanda deve {pessoas} pessoas")
    pessoas +=1

alunos = int(input("Quantos alunos a fernanda já pagou?"))

while alunos < 30:
    print(f"A Fernanda pagou {alunos} alunos")
    alunos +=1


# for in

# for fofoqueiro in local:
#      print(fofoquei)

nome_que_fernanda_deve = ["Otavio", "Jade", "Isabella", "Ana Clara", "Rafael", "Julia", "Mariana"]

for item in nome_que_fernanda_deve:
    print(f"Extra, extra, nomes que a fernanda deve: {item}")


airfrayer = ["Brastemp", "Polishop", "Samunsg", "Britania", "Mondial", "Electrolux"]

for item in airfrayer:
    print(f"Aqui usúario estão as marcas que temos de Airfayer: {item}")


# Manipulação de Strings

nome = "fernanda barbie"

print(nome.upper()) # Transforma toda a nossa string em maiúsculo
print(nome.capitalize()) # Transforma a priemira letra da nossa string em maiúsculo
print(nome.lower()) # Transforma todas as letras em minúsculo
print(nome.title()) # Transforma a primeira letra do nome e sobrenome em maiúsculo
