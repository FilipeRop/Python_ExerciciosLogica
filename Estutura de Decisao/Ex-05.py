"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
-A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
-A mensagem "Reprovado", se a média for menor do que sete;
-A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota_1 = input('Nota 1 -> ')
nota_2 = input('Nota 2 -> ')

if nota_1.isnumeric() and nota_2.isnumeric():
    
    media = (float(nota_1) + float(nota_2))/2

    if media == 10:
        print('Aprovado com Distinção')
    elif media < 7:
        print(f'Reprovado com nota:{media}')
    else:
        print(f'Aprovado como nota: {media}')

else:
    print('Entrada inválida.')
