"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produto_1 = float(input('Escreva o preço de um produto: '))
produto_2 = float(input('Escreva o preço de um produto: '))
produto_3 = float(input('Escreva o preço de um produto: '))


if produto_1 <= produto_2 and produto_1 <= produto_3:
    print(f'O produto de R${produto_1} é o maior barato e deve ser comprado.')
elif produto_2 <= produto_1 and produto_2 <= produto_3:
    print(f'O produto de R${produto_2} é o maior barato e deve ser comprado.')
else:
    print(f'O produto de R${produto_3} é o maior barato e deve ser comprado.')