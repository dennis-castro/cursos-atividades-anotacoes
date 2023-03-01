from itertools import count


par = ()
lista = (
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: ')),
    int(input('Digite o quinto valor: ')))

print(f'Você digitou os numeros {lista}')
if 9 in lista:
    print(f'O numero 9 aparece {lista.count(9)}')
else:
    print('O numero 9 não foi encontrado.')

if 3 in lista:
    print(f'o numero 3 aparece na {lista.index(3)+1}* posição.')
else:
    print('O numero 3 não foi encontrado.')

print(f'Os valores PARES encontrados foram: ', end='')
for n in lista:
    if n % 2 == 0:
        par = n
        print(par, end='. ')
if not par:
    print('Não encontrei nenhum numero PAR.')
