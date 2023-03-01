jogadores = []
ficha = {}
gols = []
while True:
    ficha.clear()
    gols.clear()
    ficha['nome'] = str(input('Nome do jogador: '))
    totPartidas = int(input(f'Quantas partidas o {ficha["nome"]} atuou: '))
    for p in range(0, totPartidas):
        gols.append(int(input(f'Partida {p+1} quantos gols marcados: ')))
    ficha['gols'] = gols[:]
    ficha['total'] = sum(ficha['gols'])
    jogadores.append(ficha.copy())
    while True:
        res = str(input('Deseja cadastrar outro jogador (s/n): ')
                  ).strip().lower()[0]
        if res in 'sn':
            break
        print('ERRO!somente (s/n)')
    if res == 'n':
        break

print('-'*40)
print(f'{"COD":<4}{"NOME":>5}{"GOLS":>15}{"TOTAL":>21}')
for i, v in enumerate(jogadores):
    print(f'{i:<4} {v["nome"]:<14} {str(v["gols"]):<20}{str(v["total"])} ')
print('-'*40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador   (999 para sair): '))
    if mostrar == 999:
        print('Saindo...')
        break
    if mostrar >= len(jogadores):
        print('Numero invalido')
    else:
        print(
            f'--Levantamento do jogador {jogadores[mostrar]["nome"].upper()}')
        for i, g in enumerate(jogadores[mostrar]["gols"]):
            print(f'...no jogo {i+1} fez {g} gols.')
    print('-'*40)
