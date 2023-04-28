"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario_Hora = float(input('Entre com o valor da hora de trabalho: '))
horas_Trabalhadas = float(input('Entre com a quantidade de horas trabalhadas no mês: '))

salario_Bruto = salario_Hora * horas_Trabalhadas

IR = salario_Bruto * 0.11
INSS = salario_Bruto * 0.08
sindicato = salario_Bruto * 0.05

descontos_Totais = IR + INSS + sindicato

salario_Liquido = salario_Bruto - descontos_Totais

print(f'+ Salário Bruto: R${salario_Bruto:.2f}.')
print(f'-IR (11%): R$ {IR:.2f}')
print(f'-INSS(8%): R$ {INSS:.2f}')
print(f'-Sindicato(5%): R$ {sindicato:.2f}')
print(f'Salário Líquido: R$ {salario_Liquido:.2f}')