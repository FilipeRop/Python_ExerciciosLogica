"""

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - o produto do dobro do primeiro com metade do segundo .
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.

"""

num1 = int(input('Escreva um número inteiro: '))
num2 = int(input('Escreva outro número inteiro: '))
num3 = float(input('Escreva um número real: '))

caso1 = (num1 * 2) * (num2/2)
caso2 = (num1 * 3) + num3
caso3 = pow(num3,3)

print(f'Primeiro caso = {caso1}')
print(f'Segundo caso = {caso2}')
print(f'Terceiro caso = {caso3:.2f}')
