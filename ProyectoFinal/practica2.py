"Práactica 2"

print("¡Descubra su nota en el promedio!")
nombre = input("¿Como te llamas?: ")
examsrea = int(input("Cuantos exámenes realizó en el periodo: "))
if examsrea == 3:
    exam1 = int(input("Nota obtenda en el primer examen: "))
    exam2 = int(input("Nota obtenda en el segundo examen: "))
    exam3 = int(input("Nota obtenda en el tercer examen: "))
else:
    print(" Evaluación incompleta :( ")

notafinal = (exam1 + exam2 + exam3) / 3

if notafinal >= 70:
    input(f"¡Felicidades {nombre}, has aprovado con la nota de {notafinal}!")
if notafinal >= 60 and notafinal < 70:
    input(f"Bueno {nombre}, tendrás que realizar amplicación, tu nota fue {notafinal}")
if notafinal < 60:
    input(f"Lo lamento {nombre}, no lograste aprobar, esta fue tu nota {notafinal}")
