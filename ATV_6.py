ganho_por_hora = float(input('Qual valor que você ganha por hora ? '))
numero_de_horas = float(input('Quantas horas trabalhadas você tem ? '))

salario = ganho_por_hora * numero_de_horas

print(f'O salário deste mês será: R${salario:.2f}')