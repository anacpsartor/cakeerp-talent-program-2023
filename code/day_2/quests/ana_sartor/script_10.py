salarioAtual = float(input("Digite o salário atual do colaborador: "))

if salarioAtual <= 280:
    percentualAumento = 20
elif salarioAtual <= 700:
    percentualAumento = 15
elif salarioAtual <= 1500:
    percentualAumento = 10
else:
    percentualAumento = 5

valorAumento = salarioAtual * (percentualAumento / 100)
novoSalario = salarioAtual + valorAumento

print("Salário antes do reajuste: R$", salarioAtual)
print("Percentual de aumento aplicado:", percentualAumento, "%")
print("Valor do aumento: R$", valorAumento)
print("Novo salário após o aumento: R$", novoSalario)
