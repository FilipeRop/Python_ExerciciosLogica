"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num_1 = float(input('Escreva um número: '))
num_2 = float(input('Escreva outro número: '))

if num_1 > num_2:
    print(f'{num_1} é maior que {num_2}')
else:
    print(f'{num_2} é maior que {num_1}')
