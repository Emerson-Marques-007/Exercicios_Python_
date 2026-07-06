tamanho_gb = float(input('Digite o tamanho em GB:'))

mb = tamanho_gb * 1024
kb = tamanho_gb * 1024 * 1024

print(f'O tamanho do arquivo em Megabytes é {mb}MBs - e em Kilobytes {kb}')