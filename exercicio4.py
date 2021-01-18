#  Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Qual o valor do salário? ')) #pede um valor qualquer, tipo float, referente ao salário;
aumento = salario * 0.25 #calcula um percentual de aumento qualquer. no caso, 25%;

print(f'O valor do salário somado ao percentual de aumento, será de R$ {salario + aumento:.3f}') #imprime o valor líquido do salário, somado o percentual de aumento. 
