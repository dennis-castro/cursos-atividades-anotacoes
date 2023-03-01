compras = float(input('Valor total das compras  r$:'))


print('''Selecione a opção desejada:
 [1]dinheiro/cheque
 [2]cartão debito
 [3]2x credito
 [4]3x ou mais credito''')
op = int(input())
print('Opção selecionada: {}'.format(op))
avista = compras - (compras*10/100)
debito = compras - (compras*5/100)
parcela2x = compras / 2
parJuros = compras+ (compras*20/100)

if op == 1:
    print('Total de sua compra foi de r${:.2f} com 10% de desconto r${:.2f}'.format(compras, avista))
elif op == 2:
    print('Total de sua compra foi de r${:.2f} com 5% de desconto r${:.2f}'.format(compras, debito ))
elif op == 3:
    print('Total de sua compra foi de {:.2f} parcelado em 2x s/ juros r${:.2f}'.format(compras, parcela2x))
elif op == 4:
    quaPar = int(input('Em quantas parcelas deseja fazer :'))
    total = parJuros / quaPar
    print('Total de sua compra foi de r${:.2f}'.format(compras))
    if quaPar >= 3:
            print('O valor das parcelas ficou em {:.0f} x {:.2f} c/ juros'.format(quaPar, total ))
    else:
            print('Opção invalida')
else:
    print('Opção invalida')

