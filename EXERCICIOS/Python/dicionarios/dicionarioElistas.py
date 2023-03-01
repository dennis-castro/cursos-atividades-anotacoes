ficha = {}
galera = []
soma = media = acimaMedia = 0
mulheres = []
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo (F / M): ')).strip().lower()[0]
        if ficha['sexo'] == 'f':
            mulheres.append(ficha['nome'])
        if ficha['sexo'] in 'fm':
            break
        print('ERRO! somente (F / M)')
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    galera.append(ficha.copy())
    while True:
        res = str(input('Deseja cadastrar outra pessoa? (S / N ) ')
                  ).strip().lower()[0]
        if res in 'sn':
            break
        print('ERRO! somente (S / N)')
    print('-' * 40)
    if res == 'n':
        print('Finalizando...')
        break
print()
print(f'{"Ficha de cadastramento":.^40}')
print(f'- Total de {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'- Media de idade das pessoas cadastradas {media:5.2f} anos.')
print(f'- Lista das mulheres cadastradas: {mulheres}')
print(f'- Lista com pessoas  acima da idade media: ')
for p in galera:
    if p['idade'] >= media:
        print(f'     -nome: {p["nome"]}, idade: {p["idade"]}anos ')
