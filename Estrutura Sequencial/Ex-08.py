#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#

valor_Hora = float(input('Digite o valor da hora trabalhada => R$'))

qnt_Horas = float(input('Digite a quantidade de horas trabalhadas no mês => '))

salario_Total = valor_Hora * qnt_Horas

print(f'Salário total no mês => R${salario_Total}')