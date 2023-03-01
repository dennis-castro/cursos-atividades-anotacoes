import time
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''\033[31;1m
    [1]SOMAR;
    [2]MULTIPLICAR;
    [3]MAIOR;
    [4]NOVOS NUMEROS;
    [5]SAIR DO PROGRAMA; \033[m''')
    opc = int(input('>>>>>>>>Qual é sua opção: '))
    if opc == 1:
        soma = valor2 + valor1
        print('A soma entre {} e {} é:{}'.format(valor1, valor2, soma))
    elif opc == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} e {} é:{}'.format(valor1, valor2, multiplicar))
    elif opc == 3:
        if valor1  >valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior valor digitado foi {}'.format(maior))
    elif opc == 4:
        print('Informe os novos numeros: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opc ==5:
        print('FINALIZANDO...')
    else:
        print('Opção INVALIDA tente novamente!')
    print('-='*20)
    time.sleep(3)
print('Fim do programa! Volte sempre.')