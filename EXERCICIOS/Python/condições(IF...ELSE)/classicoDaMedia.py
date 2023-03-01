n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'\033[31mO ALUNO ESTA REPROVADO COM A MEDIA: {media}')
elif media >= 5 and media < 6.9:
    print('\033[33mO ALUNO ESTA EM RECUPERAÇÃO COM A MEDIA: {}'.format(media))
else:
    print('\033[32mO ALUNO ESTA APROVADO COM A MEDIA: {}'.format(media))
