numero =  int(input('Digite um numero inteiro: '))

print('_'*30)
print('ESCOLHA SUA CONVERSAO')
print('1 para BINARIO')
print('2 para OCTAL')
print('3 para HEXADECIMAL')
print('_'*30)
escolha = int(input('Em que deseja converter ?'))

if escolha == 1:
    print('NUMERO BINARIO: {}'.format(bin(numero)[2:]))
elif escolha == 2:
    print('NUMERO OCTAL: {}'.format(oct(numero)[2:]))
elif escolha == 3:
    print('NUMERO HEXADECIMAL: {}'.format(hex(numero)[2:]))
else:
    print('Numero invalido')
print('obrigado')
