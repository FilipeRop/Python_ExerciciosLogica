#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.#

import math #introduzindo a função import usando o mósdulo math

raio = float(input('Valor do raio do circulo => '))

area = math.pi * (pow(raio,2)) #math. chama uma função do módulo. Função pow realiza operação de potenciação 

print(f'Área da circunferência = {area:.2f}')
