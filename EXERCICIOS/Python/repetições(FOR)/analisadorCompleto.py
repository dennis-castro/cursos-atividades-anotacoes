mediaIdade = 0
totalIdade = 0
nomeHomem = ''
homemVelho = 0
totMulheres = 0
for pessoa in range(1, 5):
    print('--------{} PESSOA---------'.format(pessoa))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo M / F: ')).strip().lower()
    print('=-'*30)
    totalIdade = totalIdade+idade
    mediaIdade = totalIdade / 4
    if pessoa == 1 and sexo == 'm':
        nomeHomem = nome
        homemVelho = idade
    if idade > homemVelho and sexo == 'm':
        nomeHomem = nome
        homemVelho = idade
    if sexo in 'Ff' and idade < 20:
        totMulheres = totMulheres + 1

print('A media de idade do grupo é {:.2f}'.format(mediaIdade))
print('O homem mais velho tem {} anos e o nome dele é {}:'.format(homemVelho, nomeHomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulheres))
