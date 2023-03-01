def text(msg):
    tam = len(msg)+4
    print('\033[32m~\033[m'*tam)
    print(f'\033[31m  {msg}\033[m')
    print('\033[32m~\033[m'*tam)
    

text('Dennis Castro')

