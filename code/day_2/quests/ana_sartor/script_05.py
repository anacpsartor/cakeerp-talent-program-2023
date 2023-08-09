taxaImposto = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o custo do item antes do imposto: "))

custo_com_imposto = custo * (1 + taxaImposto / 100)

print("O custo do item após aplicar o imposto é:", custo_com_imposto)
