n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
meio = (n1 + n2 + n3) - (maior + menor)

print("Números em ordem decrescente:", maior, "/", meio, "/", menor)
