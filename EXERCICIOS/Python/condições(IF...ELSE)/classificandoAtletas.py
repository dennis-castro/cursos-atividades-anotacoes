import datetime

nasc = int(input('Digite o ano de seu nascimeto: xxxx  '))
anoAtual = datetime.date.today().year
idade = anoAtual - nasc
if idade <= 9:
    print('O atleta esta com {} anos de idade  na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta esta com {} anos de idade na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta esta com {} anos de idade na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta esta com {} anos de idade na categoria  SENIOR'.format(idade))
else:
    print('O atleta esta com {} anos de idade na categoria MASTER'.format(idade))
