import datetime
nasc = int(input('Digite o ano de seu nascimeto: xxxx: '))
ano = datetime.date.today().year
idade = ano - nasc
if idade < 18:
    print('\033[32;1mNao é ncessario se apresentar ao exercito!')
elif idade == 18:
    print('\033[31;1mVoce precisa se apresentar no exercito!')
else:
    print('\033[32;1mVoce ja atingiu a maioridade !')
