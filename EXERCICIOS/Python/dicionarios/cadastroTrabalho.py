import datetime
cadastro = {}
anoAtual = datetime.date.today().year

cadastro['nome']=str(input('Nome: '))
cadastro['nasc']=int(input('ano de nascimento(xxxx): '))
cadastro['cpts']=int(input('Numero da carteira (responda 0 caso nao tenha): '))
if cadastro["cpts"]>0:
    cadastro["anoContrato"]=int(input('Ano de contratação(xxxx): '))
    cadastro["salario"]=float(input(('Salario: ')))
    cadastro["contribuicao"]= anoAtual - cadastro["anoContrato"]

print(f'-Nome: {cadastro["nome"]}\n'
      f'-Idade: {anoAtual - cadastro["nasc"]} anos\n'
      f'-Cpts: {cadastro["cpts"]}')
if cadastro['cpts'] > 0:
    print(f'-Ano de contratação: {cadastro["anoContrato"]}\n'
          f'-Salario Base R${cadastro["salario"]:.2f}\n'
          f'-Tempo de contribuição: {cadastro["contribuicao"]} anos')