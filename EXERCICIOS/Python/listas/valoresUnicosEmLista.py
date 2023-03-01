num = []

while True:
    n = int(input('Digite um numero: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado...')
    res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = (input('Resposta invalida...Deseja continuar [S/N]: ')).strip().upper()[0]
    if res in 'N':
        print('Finalizando...')
        break
print(f'Numeros Digitados {sorted(num)}')