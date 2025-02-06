import random

num = random.randint(1, 10)

print("Bem-Vindo ao jogo da sorte!")

print("\n")

jogo = int(input("Adivinhe um numero de 1 a 10. Boa sorte!: "))

if jogo == num:
    print("Parabens você acertou!")

else:
    print("Perdeu!")



