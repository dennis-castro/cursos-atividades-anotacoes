n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[1;32mÉ possivel formar um triangulo\033[m')
    if n1 == n2 == n3:
        print('Triangulo Equilatero todos os lados iguais')
    elif n1 ==  n2 or n2 == n3 or n3 == n1:
        print('Triangulo Isosceles dois lados iguais ')
    else:
        print('Triangulo Escaleno todos os lados diferentes ')
else:
    print('\033[1;31mNão e possivel formal um triangulo\033[m')
