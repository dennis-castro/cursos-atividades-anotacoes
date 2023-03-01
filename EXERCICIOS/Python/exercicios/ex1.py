'''1Faça um algoritmo que leia o sexo e a idade de 3 pessoas. Calcule e mostre a
quantidade de mulheres com idade maior que 20 anos. Se o algoritmo não
encontrar nenhuma mulher com idade superior a 20 anos, mostrar a seguinte
mensagem: “Não foram encontradas mulheres > de 20 anos”.'''

mulVinte = []

for n in range(1,4):
        nome = str(input("Nome: ")).strip()
        while True:
            sexo = str(input('Sexo(M/F): ')).strip().upper()[0]
            if sexo in 'FM':
                break
            else:
                print('Valor INVALIDO tente novamente.')
        while True:
            idade = str(input('Idade: '))
            if idade.isnumeric():
                idade = int(idade)
                break
            else:
                print('Valor INVALIDO tente novamente.')
        if sexo == "F" and idade > 20 :
            mulVinte.append([nome,sexo,idade])
        print('_'*50)

for n in (mulVinte):
    print(f'Nome:{n[0]} Sexo:{n[1]} Idade: {n[2]}')
