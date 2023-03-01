'''10. Faça um algoritmo que leia: número da conta do cliente, saldo, total de débitos e
total de créditos. Em seguida, calcule e imprima o saldo atual do cliente. Uilize a
seguinte fórmula: saldo atual = saldo - débito + crédito. Verifique se saldo atual é
maior ou igual a zero e escreva a mensagem 'Saldo Positivo', senão escreva a
mensagem 'Saldo Negativo'''

while True:
    try:
        conta = int(input('N* ContaC: '))
        saldo = float(input('Saldo: '))
        totDeb = float(input('Debitos: '))
        totCre = float(input('Creditos: '))
        break
    except:
        print('Erro ao valor informado!')

totDis = totCre
creDis = 0
if totCre + saldo < totDeb:
    totDis = 0
if saldo <= totDeb:
    creDis = totDeb - saldo
    if totCre >= creDis:
        totDis = totCre - creDis


print()
print('-----Extrato Bancario------')
print()
print(f'Conta: {conta}\nSaldo: R${saldo} \nCredito Aprov: R${totCre}'
      f', Credito Dispo: R${totDis}\nDebitos: R$-{totDeb}\nSaldo Final:  ', end='')

saldoAtual = saldo - totDeb + totCre
if saldoAtual >= 0:
    print(f'$+{saldoAtual}')
else:
    print(f'R${saldoAtual}')
