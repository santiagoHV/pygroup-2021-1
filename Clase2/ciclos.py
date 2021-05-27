a = 5
'''
while a > 0:
    print(f'estoy en un ciclo y a = {a}')
    a -= 1
'''
## rangos
#rango = range(9)
'''
sin primer parametro asume 0 inicial
sin ultimo parametro asume saltos de 1
'''
if 1 == 1:
    pass


for i in range(9):
    if i == 5:
        continue

    print(f'i = {i}')

for i in range(9):
    if i == 5:
        break

    print(f'i = {i}')

