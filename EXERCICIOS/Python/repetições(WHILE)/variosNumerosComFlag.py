c = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    c += 1
    soma += num
print(f'O usuario digitou {c} numeros e a soma entre eles foi {soma}.')