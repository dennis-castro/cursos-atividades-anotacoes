from re import I
import re
from tkinter import CENTER
from turtle import pensize
from attr import asdict


lista=(
    'caneta',4.50,
    'lapis',2,
    'caderno',25.50,
    'mochila',100,
    'borracha',1.30,
)


print('='*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*40)

for i in range(len(lista)):
    if i % 2==0:
        print(f'{lista[i]:.<30}',end='R$:')
    else:
        print(f'{lista[i]:>7.2f}')
