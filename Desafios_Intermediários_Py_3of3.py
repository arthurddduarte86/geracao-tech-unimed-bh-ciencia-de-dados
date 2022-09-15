'''
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 600.00
600.01 - 900.00
900.01 - 1500.00
1500.01 - 2000.00
Acima de 2000.00

17%
13%
12%
10%
5%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

Exemplo 1

Entrada	Saída
1000	Novo salario: 1120,00 Reajuste ganho: 120,00 Em percentual: 12 %
'''
#
#
#
salario = int(input()) 

tabela_Reajuste = (17, 13, 12, 10, 5)

if salario <= 600: reajuste_Percentual = tabela_Reajuste[0]

if (salario > 600 and salario <= 900) : reajuste_Percentual = tabela_Reajuste[1]

if (salario > 900 and salario <= 1500): reajuste_Percentual = tabela_Reajuste[2]

if (salario > 1500 and salario <= 2000): reajuste_Percentual = tabela_Reajuste[3]

if (salario > 2000): reajuste_Percentual = (tabela_Reajuste[4] / 100) + 1

def folha_pagamento ():
    global novo_Salario
    global reajuste_Ganho
    novo_Salario = salario * (reajuste_Percentual/100 + 1 )
    reajuste_Ganho = (novo_Salario - salario)
    return novo_Salario, reajuste_Ganho

folha_pagamento()
print(f"Novo salario: {novo_Salario:.2f} Reajuste ganho: {reajuste_Ganho:.2f} Em percentual: {reajuste_Percentual} %".replace('.',','))





