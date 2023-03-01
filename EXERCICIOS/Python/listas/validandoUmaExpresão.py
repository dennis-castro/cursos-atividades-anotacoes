expre = str(input('Digite uma expressao: '))
pilha=[]
for item in expre:
    if item == '(':
        pilha.append('(')
    elif item == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressao esta correta')
else:
    print('sua expressao esta incorreta ')
