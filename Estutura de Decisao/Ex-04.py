"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Escreva uma letra: ')
letra = letra.upper()

if letra.isalpha():
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print(f'{letra} é vogal.')
    else:
        print(f'{letra} é consoante.')
else:
    print('Entrada incorreta!')