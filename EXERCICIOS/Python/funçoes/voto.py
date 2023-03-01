def voto():
    from datetime import date
    nasc = int(input('Ano de nascimento xxxx: '))
    atual =  date.today().year
    idade = atual - nasc
    if idade < 16:
        print (f'Voce tem {idade} anos \nVOTO NEGADO')
    elif idade  <18 or idade > 70:
        print (f'Voce tem {idade} anos \nVOTO OPCIONAL')
    else:
        print (f'Voce tem {idade} anos \nVOTO OBRIGATORIO')

voto()
