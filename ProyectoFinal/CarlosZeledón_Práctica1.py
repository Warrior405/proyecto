input("¡Adivina el número secreto!")
edad=int(input("¿Que edad tienes?: "))
nombre=input("¿Como te llamas?: ")
apellido=input("¿Cuál es tu apellido?: ")
secretnum=int(7)
input("¿Cuál crees sea el número secreto?")
input("Pista: Es un número del 1 al 10")
numusu=int(input("Digita un número aquí: "))
if(numusu==secretnum):
    input(f"Felicidades {nombre} {apellido} de {edad} años, el número secreto es {secretnum},")
else:
    input(f"¡¡¡OH NOOOO!!! {nombre} {apellido} de {edad} años, {numusu} no es el número secreto, suerte la próxima, gracias por tu participación")