from sys import api_version


lista = [[], []]
c = 0
for c in range(1, 8):
    while True:
        try:
            num = int(input(f'Digite o {c} valor: '))
            if num % 2 == 0:
                print('\033[32mValor adicionado a lista PAR!\033[m')
                lista[0].append(num)

            else:
                print('\033[35mValor adicionado a lista IMPAR!\033[m')
                lista[1].append(num)
            print('-'*40)
            c += 1
            break

        except:
            print('\033[31mValor informado esta incorreto!\033[m')

lista[0].sort()
lista[1].sort()
print(f'\033[44mOs valores PARES adicionado a lista foi {lista[0]}')
print(f'Os valores IMPARES adicionado a lista foi {lista[1]}\033[m')
