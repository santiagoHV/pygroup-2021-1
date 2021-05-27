# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))

def verificar_edad(nombre, edad):
    notificacion = ''

    if edad > 18:
        notificacion = f'{nombre} es mayor de edad'
        #saludo(nombre)
    elif edad == 18:
        notificacion = f'{nombre} es mayor de edad, ya puedes ir por tu cedula'
        #saludo(nombre)
    else:
        notificacion = f'{nombre} es menor de edad'

    return notificacion


def saludo(nombre_en_funcion):
    print(f'{nombre_en_funcion} bienvenido a PYGROUP')
    print('Revisa tu correo')
    print('Registrate en whatsapp')


def elevar(base,exponente):
    return base ** exponente

#print(verificar_edad('santiago',20))
#texto = verificar_edad('',3)
#print(elevar(2,5))

a = 5
b = 6

def sumar(a, b):
    return a + b

def restar(a, b):
    return a-b

def multiplicar(multiplicando,multiplicador):
    return multiplicando*multiplicador

def division_entera(dividendo,divisor):
    return 'hola'


print(sumar(a,b))
print(restar(a,b))
print(multiplicar(a,b))
print(division_entera(a,b))
print(elevar(a,b))

