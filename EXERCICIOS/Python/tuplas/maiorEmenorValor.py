from random import randint

numeros = (randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros gerados foram {numeros}')
print(f'O maior numero encontrando foi: {max(numeros)}')
print(f'O menor numero encontrado for: {min(numeros)}')
