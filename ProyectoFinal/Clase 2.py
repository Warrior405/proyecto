# Condicionales

# Condicional simple --> TRUE

# Los miércoles se paga la entrada a mitad de precio
"""""
precio=int(input("Digite el precio de la entrada: "))
dia=int(input("Digite el día en el que se encuentra: \n1.Lunes \n2.Martes \n3.Miercoles \n4.Jueves \n5.Viernes \n6.Sabado \n7.Domingo:  "))
#igualdad ==
#desigualdad !=
#identación = espacio luego de los :

if (dia == 3):
    precio=precio/2
    print("Se redujo el precio de entrada")

print(f"El precio de la entrada es: {precio}")
""" ""

# Condición Doble ---> True/False
"""
if(condicion):
    accion
else:
    accion
"""

"""""
num=int(input("Digite un número: "))
#>, <, =
if(num>=0):
    mensaje="Positivo"
else:
    mensaje="Negativo"

print(f"El número: {num} es un numero {mensaje} ")

if(num%2!=0):
    mensaje="Impar"
else:
    mensaje="Par"
    
print(f"El número tambien es: {mensaje} ")
""" ""
# Prengunte su nombre y determinen si puede conducir (pedir edad y licencia)
# Mensaje llamandolo por su nombre y diciendo porque si o no puede manejar

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
if edad >= 18:
    edad = "mayor de edad"
else:
    edad = "menor de edad"
print(f"El cliente: {nombre} es {edad} ")

licencia = int(input("¿Tiene licencia de Condusir?: \n1.si tiene \n0.no tiene: "))

if licencia == 1:
    numli = "si tiene"
else:
    numli = "no tiene"
print(f"El cliente: {nombre} {numli} licencia para conducir")


if edad == "Mayor de edad" and licencia == 1:
    permiso = "puede conducir"
else:
    permiso = "no puede conducir"

print(f"El cliente: {nombre} {permiso}.")
