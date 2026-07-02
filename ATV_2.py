acumulador = 0

for i in range(4):
    notas = float(input(f'Digite sua nota do {i+1}º: '))
    acumulador += notas

media = acumulador / 4

print(f'Sua média {media}')