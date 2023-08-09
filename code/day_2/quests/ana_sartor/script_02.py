idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    
    idades.append(idade)
    alturas.append(altura)

print("\nIdades e alturas na ordem inversa:")
contador = 4
while contador >= 0:
    print("Idade:", idades[contador], "anos, Altura:", alturas[contador], "metros")
    contador -= 1
