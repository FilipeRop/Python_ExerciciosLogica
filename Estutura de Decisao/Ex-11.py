"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até R$ 280,00 (incluindo) : aumento de 20%
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.
"""

_20 = 0.2
_15 = 0.15
_10 = 0.1
_5 = 0.05

salario = float(input('Escreva seu salário atual: '))

if salario <= 280:

    aumento = salario * _20
    novo_Salario = salario + aumento

    print(f'Salário antes do reajuste -> R${salario}.')
    print(f'Percentual de aumento aplicado -> {_20*100}%')
    print(f'Valor do aumento -> {aumento}')
    print(f'Novo salário, após o aumento -> R${novo_Salario}')

elif salario > 280 and salario <= 700:

    aumento = salario * _15
    novo_Salario = salario + aumento

    print(f'Salário antes do reajuste -> R${salario}.')
    print(f'Percentual de aumento aplicado -> {_15*100}%')
    print(f'Valor do aumento -> {aumento}')
    print(f'Novo salário, após o aumento -> R${novo_Salario}')

elif salario > 700 and salario <= 1500:

    aumento = salario * _10
    novo_Salario = salario + aumento

    print(f'Salário antes do reajuste -> R${salario}.')
    print(f'Percentual de aumento aplicado -> {_10*100}%')
    print(f'Valor do aumento -> {aumento}')
    print(f'Novo salário, após o aumento -> R${novo_Salario}')

elif salario > 1500:

    aumento = salario * _5
    novo_Salario = salario + aumento

    print(f'Salário antes do reajuste -> R${salario}.')
    print(f'Percentual de aumento aplicado -> {_5*100}%')
    print(f'Valor do aumento -> {aumento}')
    print(f'Novo salário, após o aumento -> R${novo_Salario}')

