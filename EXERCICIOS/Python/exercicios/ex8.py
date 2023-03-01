'''8. Faça um algoritmo que leia um valor do tipo inteiro e verifique se esse número é
par ou ímpar. '''

num = int(input('Digite um numero: '))
if num % 2 == 0:
    print(f'O numero digitado foi {num} e ele é PAR')
else:
    print(f'O numero digitado foi {num} e ele é IMPAR')
