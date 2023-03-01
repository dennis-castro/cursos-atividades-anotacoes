lista=[]
cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado com sucesso...')
    else:
        print('Numero duplicado...')
    res = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while res not in 'SN':
        res = str(input('Resposta invalida tente novamente [S/N]: ')).upper().strip()[0]
    print('-='*30)
    if res in 'N':
        break
        print('Finalizando...')
print()
lista.sort(reverse=True)
print(f'Numeros digitados {lista}')
print(f'Foram digitados {len(lista)} numeros.')
if 5 in lista:
    print('O numero 5 consta na lista.')
else:
    print('O numero 5 nao consta na lista.')
