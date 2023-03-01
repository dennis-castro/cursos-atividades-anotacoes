from time import sleep
par = []
impar = []
lista = []


while True:
    while True:
        try:
            lista.append(int(input('Digite um numero: ')))
            print('\033[32mNumero adicionado com sucesso!!\033[m')
            break
        except:
            print('\033[31mValor invalido tente novamente..\033[m')

    res = str(input('Deseja adicionar outro numero? S/N:')).strip().lower()[0]
    while res not in 'sn':
        print('\033[31mValor invalido tente novamente..\033[m')
        res = str(input('Deseja adicionar outro numero? S/N:')).strip().lower()[0]
    print('='*40)
    if res == 'n':
        print('FINALIZANDO...')
        print('=' * 40)

        sleep(1)
        break

# programaPrincipal

print(f'Os valores declarados são: {lista}')
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Os numeros pares da lista são: {par}')
print(f'Os numeros impares da lista são: {impar} ')
