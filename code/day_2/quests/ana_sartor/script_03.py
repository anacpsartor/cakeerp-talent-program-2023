perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = list(input(pergunta + " (sim/não): ") for pergunta in perguntas)
envolvimento = respostas.count("sim")

if envolvimento == 2:
    classificacao = "Suspeita"
elif 3 <= envolvimento <= 4:
    classificacao = "Cúmplice"
elif envolvimento == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("\nClassificação:", classificacao)
