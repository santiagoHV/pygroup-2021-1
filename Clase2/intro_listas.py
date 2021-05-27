# lista = [2,3,5,3]
# frutas = ['manzana', 'pera', 'uva']
# for fruta in frutas:
#     print(fruta)


counter = 0
print(counter)
def aumentar_contador(n):
  print(counter)
  for _ in range(n):
    print(counter)
    counter += 2

 
######################################
aumentar_contador(8)
# print('paso 1')
# assert counter == 16
# counter = 0
# aumentar_contador(5)
# assert counter == 10
# print('Reto 1 completado 👌')