import datetime
anoAtual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Candidato {} digite o ano de seu nascimento xxxx:  '.format(c)))
    idade = anoAtual - nasc
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('TOTAL DE PESSOAS C/ MAIORIDADE: {}'.format(maior))
print('TOTAL DE PESSOAS C/ MENORIDADE: {}'.format(menor))