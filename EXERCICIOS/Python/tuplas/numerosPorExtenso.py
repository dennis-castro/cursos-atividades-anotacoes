cont = (
    'zero', 'um', 'dois', 'tres', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez'
)
while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if num > 0 and num <= 10:
        break
    print('Valor invalido tente novamente...')

print(f'O numero digitado por extenso foi {cont[num]}')
