'''
lista = ['python', 'java', 'js']

if 'js' not/in lista:
    print('oba')
else:
    print('não foi dessa vez')
'''

'''
print('trabalhando com listas')
l1 = ['banana', 'laranja', 'manga']
print(l1)
print(len(l1))

l1.append('uva')
print(l1)
print(len(l1))

for elemento in l1:
    print(elemento)

print('tuplas')
t1 = ('joão', 'maria', 'jose')
print(type(t1))
print(len(t1))

#t1[0] = 'john'

for elemento in l1:
    print(elemento)

print('Dicionarios')

profissoes2 = dict({
    'programador': 5000,
    'design': 4000,
    'engenheiro': 6000,}
)
print(type(profissoes2))
print(profissoes2)

print(profissoes2.get('limpeza'))
print('chegou nessa linha')

def diz_ola(nome):
    print('ola' + nome)

diz_ola('haniel')

#print(profissoes2['limpeza'])
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

print('try')
a = 1
b = '2'
soma = 0
try:
    soma = a + b
except:
    print('aconteceu algum erro')