"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

-Para homens: (72.7*h) - 58
-Para mulheres: (62.1*h) - 44.7
"""

altura = float(input('Escreva uma altura em metros: '))

peso_ideal_H = (72.7 * altura) - 58
peso_ideal_M = (62.1 * altura) - 44.7

print(f'Para um homem com {altura} metros de altura, seu peso ideal deve ser {peso_ideal_H:.2f} Kg')
print(f'Para uma mulher com {altura} metros de altura, seu peso ideal deve ser {peso_ideal_M:.2f} Kg')