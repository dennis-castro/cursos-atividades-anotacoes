from time import sleep


def contador(ini, fim, pas):
    if pas == 0:
        pas = 1
    print(f'Contagem de {ini} até {fim} pulando de {pas} em {pas}')
    sleep(2)
    if ini < fim:
        cont = ini
        while cont <= fim:

            print(f'{cont}', end=' ')
            cont += pas
            sleep(0.5)
        print('...Fim')
    else:
        cont = ini
        while cont >= fim:

            print(f'{cont}', end=' ')
            cont -= pas
            sleep(0.5)
        print('...Fim')
    print('-'*50)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!!!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
