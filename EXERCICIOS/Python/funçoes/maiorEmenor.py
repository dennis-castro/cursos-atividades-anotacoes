def maior(* num):
    print(f'{num} Foram analizados {len(num)} numeros')
    print(f'O maior numero foi {max(num)}')
    print(f'O menor numero foi {min(num)}')
    print('-'*50)


maior(2, 5, 8, 2, 9, 10)
maior(2, 0, 1)
maior(7)
maior(4, 55)
