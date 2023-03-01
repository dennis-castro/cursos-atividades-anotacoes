from time import sleep
print('-=' * 20)
print('CADASTRO DE PESSOAS')
print('-=' * 20)
maior = 0
hom = 0
mul = 0
resp = 'S'
sexo = ' '
while resp == 'S':
    idade = int(input('Informe sua idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Qual o sexo [F]feminino ou [M]masculino: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('RESPOSTA INVALIDA>>>>Qual o sexo [F]feminino ou [M]masculino: ')).strip().upper()[0]
    if sexo == 'M':
        hom += 1
    elif sexo == 'F':
        if idade > 18:
            mul += 1
    resp = str(input('Voce deseja cadastrar outra pessoa? [S]SIM ou [N]NAO: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('RESPOSTA INVALIDA>>>Voce deseja cadastrar outra pessoa? [S]SIM ou [N]NAO: ')).strip().upper()[0]
    print('=-' * 20)

print('FINALIZANDO O PROGRAMA...')
sleep(2)
print(f'Constou no cadastro {maior} pessoas maiores de 18 anos, constando {hom} homens e {mul} mulheres acima de 20 anos.')