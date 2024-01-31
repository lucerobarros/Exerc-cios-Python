from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for p in range(1, 8):
    ano = int(input('Em que ano a pessoa {}ª nasceu?: '.format(p)))
    idade = atual - ano
    print('Idade: {}'.format(idade))
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Total maior: {}'.format(totalmaior))
print('Total menor: {}'.format(totalmenor))

    

