import random
from random import randint
from time import sleep
print('-='*10, end="")
print('JOGO DO PAR OU ÍMPAR', end="")
print('-='*10)
print('''Escolha PAR ou ÍMPAR: 
      [0] PAR
      [1] ÍMPAR''')
escolha = int(input('PAR ou ÍMPAR: '))
if escolha == 0:
    print('Você é PAR.')
    if escolha == 0:
        print('A Máquina é ÍMPAR.')
else:
    print('Você é ÍMPAR')
if escolha == 1:
    print('A Máquina é PAR')
jogador = int(input('Digite um número de 0 a 10: '))
if jogador%2 == 0:
    print('Você digitou um número PAR.')
else:
   print('Você digitou um número ÍMPAR.') 
maquina = (randint(0, 10))
if maquina%2 == 0:
    print('A máquina digitou o número {}, portanto, PAR.'.format(maquina))
else:
    print('A máquina digitou o número {}, portanto, ÍMPAR.'.format(maquina))
total = jogador + maquina 
print('Placar foi de {}'.format(total))
if total%2 == 0:
    print('Deu PAR') 
else:
    print('Deu ÍMPAR')
if escolha == 0 and total%2 ==0:
    print('Você ganhou!!!!!!!')
elif escolha == 0 and total%2 !=0:
    print('A máquina venceu!!!!!!!')
elif escolha == 1 and total%2 !=0:
    print('Você venceu!!!!!!!')
elif escolha == 1 and total%2 ==0:
    print('A máquina venceu!!!!!!!')
print('-='*30)






