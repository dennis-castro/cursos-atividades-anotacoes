palavras = ('aprender', 'programar', 'linguagem','python',
            'curso','gratis','estudar','particar','trabalhar',
            'mercado','programador','futuro')
for p in palavras:
    print(f'\nNa palavra \033[32m{p.upper()}\033[m temos =',end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras,end=' ')
        
