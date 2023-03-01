num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        soma = soma + num
        cont = cont + 1

print('Você digitou, {} numeros e a soma entre eles foi, {}'.format(cont, soma))