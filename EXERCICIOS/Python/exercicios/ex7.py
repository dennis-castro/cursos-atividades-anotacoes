'''7. A nota final de um estudante é calculada a partir de três notas atribuídas
respectivamente: um trabalho de laboratório, uma avaliação semestral e um
exame final. A média das três notas mencionadas obedece aos pesos a seguir:
Nota Peso
Trabalho de laboratório 2
Avaliação semestral 3
Exame final 5
Faça um algoritmo que leia as três notas, calcule e mostre a média ponderada e o
conceito que segue a tabela abaixo:
Média ponderada Conceito
8.0  10.0 A
7.0  8.0 B
6.0  7.0 C
5.0  6.0 D
0.0  5.0 E'''

while True:
    try:
        trabLab = float(input('Trabalho de laboratório: '))
        avalSem = float(input('Avaliação semestral: '))
        examFin = float(input('Exame final: '))
        med = ((trabLab*2)+(avalSem*3)+(examFin*5))/10
        if med < 5:
            print(f"Média: {med:.2f} nota: E")
        elif med < 6:
            print(f"Média: {med:.2f} nota: D")
        elif med < 7:
            print(f"Média: {med:.2f} nota: C")
        elif med < 8:
            print(f"Média: {med:.2f} nota: B")
        else:
            print(f"Média: {med:.2f} nota: A")
        break
    except:
        print("Erro! valor invalido")



