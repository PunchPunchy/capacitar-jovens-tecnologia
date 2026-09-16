print("===================================")
print("       QUIZ DE TECNOLOGIA")
print("===================================")

nome = input("Digite seu nome: ")

pontuacao = 0

print("\nOlá,", nome + "!")
print("Vamos começar o quiz.\n")

print("1. Qual linguagem de programação estamos utilizando?")
print("A) Python")
print("B) HTML")
print("C) SQL")
print("D) Java")

resposta = input("Digite sua resposta: ").upper()

if resposta == "A":
    print("Correto!")
    pontuacao += 1
else:
    print("Resposta incorreta. A resposta correta é Python.")

print("\n2. Qual comando é utilizado para mostrar uma mensagem na tela?")
print("A) input()")
print("B) print()")
print("C) if")
print("D) while")

resposta = input("Digite sua resposta: ").upper()

if resposta == "B":
    print("Correto!")
    pontuacao += 1
else:
    print("Resposta incorreta. A resposta correta é print().")

print("\n3. Qual comando permite receber uma informação digitada pelo usuário?")
print("A) print()")
print("B) input()")
print("C) if")
print("D) for")

resposta = input("Digite sua resposta: ").upper()

if resposta == "B":
    print("Correto!")
    pontuacao += 1
else:
    print("Resposta incorreta. A resposta correta é input().")

print("\n===================================")
print("           RESULTADO")
print("===================================")
print(nome, "você acertou", pontuacao, "de 3 perguntas.")

if pontuacao == 3:
    print("Parabéns! Você acertou todas!")
elif pontuacao == 2:
    print("Muito bem! Você teve um bom resultado.")
elif pontuacao == 1:
    print("Continue estudando e praticando!")
else:
    print("Não desista! A prática ajuda no aprendizado.")

print("===================================")