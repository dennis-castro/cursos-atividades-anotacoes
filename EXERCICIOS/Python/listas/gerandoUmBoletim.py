c = 1
lista = []
while True:
    print(f'{f"CADASTRO DE ALUNO n-{c}":^40}')
    try:
        nome = str(input('Nome: '))
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        c += 1
        media = (n1 + n2)/2
        lista.append([nome, [n1, n2], media])
        res = str(input('Deseja cadastrar um novo aluno? S/N: ')
                  ).strip().upper()[0]
        while res not in 'SN':
            print('Valor invalido tentenovamente..')
            res = str(input('Deseja cadastrar um novo aluno? S/N: ')
                      ).strip().upper()[0]
        if res in 'N':
            print('Finalizando o programa..')
            print('-'*40)
            break
        print('-'*40)
    except:
        print('Valor invalido, tente novametente..')
        print('-'*40)
print()
print(f'{"BOLETIM ESCOLAR":.^70}')
for i, a in enumerate(lista):
    print(f'{i+1:<3}nome: {a[0]:<20}  notas: {a[1]} \tmedia: {a[2]:.1f}')
print('.'*70)
