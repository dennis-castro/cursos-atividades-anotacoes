aluno = {}
while True:
    try:
        aluno['nome'] = str(input('Nome: '))
        n2 = float(input('Nota 1: '))
        n1 = float(input('Nota 2: '))
        media = (n1+n2)/2
        aluno['media'] = media
        break
    except:
        print('\033[31mValor invalido tente novamente!\033[m')

if aluno['media'] <= 4:
    aluno['situação'] = '\033[31mReprovado\033[m'
elif aluno['media'] <= 6:
    aluno['situação'] = '\033[34mRecupeção\033[m'
else:
    aluno['situação'] = '\033[32mAprovado\033[m'

print('-='*20)
for k, v in aluno.items():
    print(f'{k:.<12}{v}')
print('-='*20)
