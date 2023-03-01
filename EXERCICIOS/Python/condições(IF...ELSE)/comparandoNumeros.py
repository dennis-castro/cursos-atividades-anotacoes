n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segunto numero inteiro: '))
if n1 > n2:
    print('\033[32;1mO primeiro valor é maior! ')
elif n2 > n1:
    print('\033[32;1mO segundo valor é maior! ')
else:
    print('\033[32;1mOs valores tem medidas equivalentes! ')