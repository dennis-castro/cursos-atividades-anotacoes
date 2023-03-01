frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ('').join(palavras)
inverso = ''

print(' A frase que voce escreveu foi {}'.format(junto))
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso, junto)
if inverso == junto:
    print('\nEsta é uma frase PALINDROMO')
else:
    print('\nNÃO é uma frase PALINDROMO')
print(junto)