somaPares = 0
somaColuna = 0
maiorvalor = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da {l}x{c}: '))

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print(f'Os valores pares digitados foram {somaPares}')
for l in range(0, 3):
    somaColuna += matriz[l][2]
print(f'A soma da coluna 3 é : {somaColuna}')
for c in range(0, 3):
    if c == 0:
        maiorvalor = matriz[1][c]
    elif matriz[1][c] > maiorvalor:
        maiorvalor = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorvalor}')
