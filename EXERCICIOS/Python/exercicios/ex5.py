'''5. Construa um algoritmo que leia 2 números reais e mostre o maior entre eles. '''

while True:
    try:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        break
    except:
        print('ERRO! valor invalido')

if n1 > n2:
    print(f'O maior numero digitado foi {n1}')
else:
    print(f'O maior numero digitado foi {n2}')