lista = []
for c in range(1, 6):
    while True:
        num = int(input(f'Digite o primeiro {c} valor: '))
        if num not in lista:
            lista.append(num)
            print(f'Numero {num} adicionado com sucesso.')
            break
        else:
            print('Numero já adicionado, tente novamete.')
print(f'\033[32mOs valores adcionados a lista são {sorted(lista)}\033[m')
