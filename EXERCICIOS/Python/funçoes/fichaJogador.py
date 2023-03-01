
def ficha():
    n= str(input('Digite o nome do jogador: ')).strip()
    if n.isalpha():
        nome = n
    else:
        nome = "desconhecido"
    g = str(input('Digite quantos gols marcados: '))
    if g.isnumeric():
        gol = int(g)
    else:
        gol = 0
    print(f'O jogador {nome} fez {gol} gols')



ficha()







