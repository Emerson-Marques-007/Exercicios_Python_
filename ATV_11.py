peso_peixe = float(input('Diigite o peso dos peixes em KG: '))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f'Você ultrapassou {excesso}Kg a mais, deve ser pago de multa  R${multa:.2f}')
else:
    print(f'sem multas')