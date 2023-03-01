peso = float(input('Qual seu peso atual(kg) : '))
altura = float(input('Qual é sua altura(m) : '))
imc = peso / altura**2
print('IMC = {:.1f}'.format(imc),end='  ')
if imc <= 18.5:
    print('VOCE ESTA ABAIXO DO PESO')
elif imc <= 25:
    print('VOCE ESTA COM O PESO IDEAL')
elif imc <= 30:
    print('VOCE ESTA COM SOBREPESO, CUIDE-SE')
elif imc <= 40:
    print('VOCE ESTA COM OBESIDADE, CUIDADO!')
else:
    print('VOCE ESTA COM OBESIDADE, PROCURE UM MEDICO')