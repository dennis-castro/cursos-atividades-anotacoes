resp = str(input('Informe seu sexo [M]masculino ou [F]feminino:  ')).strip().upper()[0]
while resp not in 'F,M':
    resp = str(input('Dados invalidos. Por favor, informe seu sexo [M]masculino ou [F]feminino: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(resp))