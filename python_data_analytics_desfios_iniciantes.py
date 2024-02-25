# Desafio: A Aventura do Explorador

quantidade_passos = int(input())

if quantidade_passos > 0:
     for i in range (1, quantidade_passos + 1):
         if i == 1:
              print('explorador: 1 passo')
         else:
              print('Explorador: {} passos'.format(i))
        
elif quantidade_passos == 0:
         print('Nenhum passo dado na floresta.')
    
# Lista para armazenar os itens

item1 = str(input())
item2 = str(input())
item3 = str(input())
itens = [item1, item2, item3]
print("Lista de itens:")
print('- {}'.format(item1))
print('- {}'.format(item2))
print('- {}'.format(item3))

#Armazenamento de Dados é Vida!


a, b = map(int, input().split())
c = int(a + (a * (b/100)))
print(c)