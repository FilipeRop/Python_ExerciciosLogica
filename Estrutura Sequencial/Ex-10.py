#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Digite uma temperatura em graus Celsius => '))

fahrenheit = (celsius * 9/5) + 32

print(f'Valor em Celsius => {celsius}°C')
print(f'Valor em Fahrenheit => {fahrenheit:.2f}°F')