'''2. Elabore um algoritmo que leia o sexo de uma pessoa. Se o sexo digitado for “M” ou
“F”, imprimir “Sexo válido”, caso contrário imprima “Sexo inválido! ”. '''

while True:
    sexo = str(input('Informe seu sexo: (F/M)  ')).strip().upper()[0]
    if sexo in 'FM':
        print('Sexo válido')
        break
    else:
        print('Sexo inválido...tente novamente')

print(f'Sexo <{sexo}> adicionado com sucesso!')