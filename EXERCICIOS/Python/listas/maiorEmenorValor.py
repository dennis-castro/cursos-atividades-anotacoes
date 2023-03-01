from pickle import EMPTY_DICT


lista = []

for c in range(1, 6):
    lista.append(int(input(f'Digite o {c} valor: ')))

# maior valor da lista e sua posição
print(f'O maior valor da lista é {max(lista)} e sua posição é ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}..', end='')
print()

# menor valor da lista e sua posição
print(f'O menor valor da lista é {min(lista)} e sua posição é ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i+1}..', end='')
print()
