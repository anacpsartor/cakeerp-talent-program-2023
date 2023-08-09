nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    situacao = "Aprovado com Distinção"
elif media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Média:", media)
print("Situação:", situacao)
