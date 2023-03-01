'''6. Escreva um algoritmo que leia três notas de um aluno, calcule e mostre a média
aritmética e a mensagem que segue na tabela abaixo:
Média Aritmética Mensagem
0.0 (inclusive) até 3.0 Reprovado
3.0 (inclusive) até 7.0 Exame
7.0 (inclusive) até 10.0 (inclusive) Aprovado'''

def nota():
    n1 = float(input('Valor da 1 nota: '))
    n2 = float(input('Valor da 2 nota: '))
    n3 = float(input('Valor da 3 nota: '))
    media = (n1+n2+n3)/3
    print('-'*40)
    if media <= 3:
        print(f'Media final {media} Status: REPROVADO')
    elif media <= 7:
        print(f'Media final {media} Status: EXAME')
    else:
        print(f'Media final {media} Status: APROVADO    ')



nota()