import time

print('=-' * 20)
print('MERCADAO DO BARATÃO')
print('=-' * 20)
print(' ')
total = mil = menor = cont = 0
produtoBarato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Qual o valor do produto: '))
    total += preco
    cont += 1
    if preco >= 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        produtoBarato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar SIM ou NAO: ')).strip().upper()[0]
    print('--' * 20)
    if resp == 'N':
        print('{:.^40}'.format('FINALIZANDO SUAS COMPRAS'))
        time.sleep(2)
        break
print(f'Total de suas compras: R$:{total:.2f}')
print(f'Quantidade de produtos acima de R$1.000.00 foi {mil}')
print(f'O produto mais barato foi ({produtoBarato}) no valor de R$:{menor:.2f}')