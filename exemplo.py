
'''
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

taxa = '2.5'

valor_fixo = 10
total = 0
if isinstance(taxa, float):
    total = valor_fixo + taxa

if isinstance(taxa, str):
    _taxa = float(taxa)
    total = valor_fixo + _taxa

print(total)

#comentario de uma linha 

----------------------------------------
linguagem = 'python eh vida'
lista = linguagem.split(' ')

print(linguagem.replace('a', '@'))
print(linguagem[0:2])
print(linguagem.lower())
print(linguagem.upper())
print(linguagem.title())
''' 

soma = 1 + 1
sub = 2 + 2
mult = 2 * 2
div = 5 / 2

print(soma)
print(sub)
print(mult)
print(div)

print('soma é maior que sub', soma > sub)
print('sub é maior que mult', sub > mult)
print(mult <= div)

print('operadores lógicos')
a =1
b = 2

if isinstance(a, int) and/or isinstance(b, int):
    print('a e/ou b são inteiros')

print ('operadores de identidade')
if (a + b == 3) is True:
    print ('a expressão eh verdadeira')
else:
    print('deu ruim')