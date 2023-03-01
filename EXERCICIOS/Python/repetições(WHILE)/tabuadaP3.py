while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        break
    for c in range (1, 11):
        res = c * num
        print(f'{c:2} x {num} = {res}')
    print('-='*15)
print('Finalizando o programa.....')