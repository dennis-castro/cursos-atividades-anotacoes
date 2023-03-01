valorCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salario: '))
quantidadeAnos = int(input('Em quantos anos sera o financiamento: '))

quantidadeParcelas = quantidadeAnos * 12
valorPrestacao =  valorCasa / quantidadeParcelas
salarioPermitido = salario*30/100

if valorPrestacao <= salarioPermitido:
    print('\033[1;32mFINANCIAMENTO APROVADO\033[m')
    print('VALOR FINANCIADO: R${:.2f} \nQUANTIDADE DE PARCELAS: {} \nVALOR DAS PARCELAS: R${:3.2f}'.format(valorCasa, quantidadeParcelas, valorPrestacao))
else:
    print('\033[31;1mFINANCIAMENTO NEGADO\033[m')