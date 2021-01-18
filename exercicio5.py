# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preço_mercadoria = float(input('Qual o valor da mercadoria, em reais (R$)? ')) #pergunta o valor, em reais, de uma mercadoria qualquer;
desconto = (20*preço_mercadoria)/100 #define um percentual qualquer de desconto sobre a mercadoria;

print(f'O valor da mercadoria, com um desconto de 20%, será de R$ {preço_mercadoria - desconto:.2f}') #imprime o valor final da mercadoria, subtraído o desconto;
