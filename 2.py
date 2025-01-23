print("Bem-Vindo a central do aluno")

print("\n")

nome = str(input("digite o nome do aluno: "))

print("\n")

nota1 = float(input("Digite a nota do {}: ".format(nome)))

print("\n")

nota2 = float(input("Digite a outra nota do {}: ".format(nome)))

print("\n")

media = nota1 + nota2 /2 

print("A média de notas do aluno {} é: {}".format(nome, media))

print("\n")

if media >= 6:
    print("Aprovado")

else:
    print("reprovado")
