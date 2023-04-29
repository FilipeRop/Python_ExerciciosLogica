"""
Faça um Programa que leia três números e mostre o maior deles.
"""

num1 = float(input('Escreva um número: '))
num2 = float(input('Escreva um número: '))
num3 = float(input('Escreva um número: '))

if num1 >= num2 and num1 >= num3:
    print(f'{num1} é maior.')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} é maior.')
else:
    print(f'{num3} é maior.')