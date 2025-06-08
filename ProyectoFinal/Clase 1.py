"""Holaa N Lineas
S
S
S"""
#Comentarios de una sola línea
print("Hola Mundo")
#Mostrar al usuario pero para solicitar algo
input("Digite su nombre: ")

#Variables
#Paso 1: Asignarle un Nombre
#Paso 2: Determinar el tipo de dato

"""
Tipos de datos

String ---> '' o "25" .. 'palabra'
Int ---> 25 dato numerico (entero)
float ---> 2,5 (decimal)
boolean ---> True/False (1/0)
"""

nombre = ""
edad = 0
estatura = 0.0
esPar = True
'''
Conversión de tipo de datos

string-> numero entero
'25' --> 25
'ste'--> error
string-->float

int--->bool
bool(1) -->True
bool2(0)-->False

'''
nombre=input('Digite su nombre: ')
#edad=int('30')
edad=int(input("Digite su edad: "))
estatura=float(input("Digite su estatura: "))
esPar=bool(int(input("Digite 1 si es par, 0 si es Impar")))
print('Mi nombre es: ', nombre , 'Tengo', edad, 'años ', 'Mido', estatura, 'metros ')
