"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

  """

nota_1 = float(input('Nota 1 -> '))
nota_2 = float(input('Nota 2 -> '))

media = (nota_1 + nota_2)/2

if media >= 9 and media <= 10:
    conceito = 'A'
    print(f'\nNota 1 - > {nota_1}\n'
          f'Nota 2 - > {nota_2}\n'
          f'Média - > {media}\n'
          f'Conceito - > {conceito}\n'
          f'Aprovado')
    
elif media >= 7.5 and media < 9:
    conceito = 'B'
    print(f'\nNota 1 - > {nota_1}\n'
          f'Nota 2 - > {nota_2}\n'
          f'Média - > {media}\n'
          f'Conceito - > {conceito}\n'
          f'Aprovado')
    
elif media >= 6 and media < 7.5:
    conceito = 'C'
    print(f'\nNota 1 - > {nota_1}\n'
          f'Nota 2 - > {nota_2}\n'
          f'Média - > {media}\n'
          f'Conceito - > {conceito}\n'
          f'Aprovado')

elif media >= 4 and media < 6:
    conceito = 'D'
    print(f'\nNota 1 - > {nota_1}\n'
          f'Nota 2 - > {nota_2}\n'
          f'Média - > {media}\n'
          f'Conceito - > {conceito}\n'
          f'Reprovado')

elif media >= 0 and media < 4:
    conceito = 'E'
    print(f'\nNota 1 - > {nota_1}\n'
          f'Nota 2 - > {nota_2}\n'
          f'Média - > {media}\n'
          f'Conceito - > {conceito}\n'
          f'Reprovado')