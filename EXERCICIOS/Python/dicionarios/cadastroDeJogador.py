dados = {}
totgols = []
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(0, dados['partidas']):
    gols = int(input(f'Quantos gols na partida {p+1}: '))
    totgols.append(gols)
dados['gols'] = totgols[:]
dados['somaGols'] = sum(totgols)
print('='*40)
print(dados)
print('='*40)
for k, v in dados.items():
    print(f'O item  {k.upper()} tem o valor {v}')
print('='*40)
print(f'O jogador {dados["nome"].upper()} jogou {dados["partidas"]} partidas')

for p, g in enumerate(dados['gols']):
    print(f'    =>Na partida {p+1} jogador fez {g} gols.')
print(f'foi um total de {dados["somaGols"]} gols ')
