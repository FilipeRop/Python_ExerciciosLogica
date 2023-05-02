"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_Hora = float(input('Valor da hora de trabalho -> '))
horas_Mês = float(input('Quantidade de horas trabalhadas no mês -> '))
print('')

salario_Bruto = valor_Hora * horas_Mês
desconto_Inss = 0.1
desconto_Fgts = 0.11

if salario_Bruto > 900 and salario_Bruto <= 1500:
    desconto_IR = 0.05
    IR = salario_Bruto * desconto_IR
    INSS = salario_Bruto * desconto_Inss
    FGTS = salario_Bruto *desconto_Fgts
    desconto_Total = IR + INSS

elif salario_Bruto >1500 and salario_Bruto <= 2500:
    desconto_IR = 0.1
    IR = salario_Bruto * desconto_IR
    INSS = salario_Bruto * desconto_Inss
    FGTS = salario_Bruto *desconto_Fgts
    desconto_Total = IR + INSS

elif salario_Bruto > 2500:
    desconto_IR = 0.2
    IR = salario_Bruto * desconto_IR
    INSS = salario_Bruto * desconto_Inss
    FGTS = salario_Bruto *desconto_Fgts
    desconto_Total = IR + INSS

else:
    desconto_IR = 0
    IR = 'Isento'
    INSS = salario_Bruto * desconto_Inss
    FGTS = salario_Bruto *desconto_Fgts
    desconto_Total = INSS


print(f'Salário Bruto:({valor_Hora} * {horas_Mês})            : R$ {salario_Bruto}\n',
      f'(-)IR({desconto_IR *100}%)                         : R$ {IR}\n'
      f' (-)INSS({desconto_Inss*100}%)                      : R$ {INSS}\n'
      f' FGTS ({desconto_Fgts*100}%)                        : R$ {FGTS}\n'
      f' Total de descontos                  : R$ {desconto_Total}\n'
      f' Salário Liquido                     : R$ {salario_Bruto - desconto_Total:.2f}'
      )
