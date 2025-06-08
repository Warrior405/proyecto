num1=int(input("Digite un número: "))
num2=int(input("Digite otro número: "))
print(f"{num1} + {num2}={num1+num2}")
print(f"{num1} * {num2}={num1*num2}")
resultsum=num1+num2
resultpor=num1*num2
resultSP=resultsum*resultpor
print(f"{resultsum} * {resultpor}={resultsum*resultpor}")

print(f"{num1} / {num2}={num1/num2}")
resultdiv=num1/num2
resultdivT=resultdiv/resultSP
print(f"{resultdiv} / {resultSP}={resultdiv/resultSP}")

print(f"{num1} - {num2}={num1-num2}")
resultrest=num1-num2
resultT1=resultrest-resultdivT
print(f"{resultrest} - {resultdivT}={resultrest-resultdivT}")

print(f"{num1} % {num2}={num1%num2}")
resultmod=num1%num2
resultT2=resultmod%resultT1
print(f"{resultmod} % {resultT1}={resultmod%resultT1}")

print(f"{num1} ** {num2}={num1**num2}")
resultesp=num1**num2
resultT3=resultesp**resultT2
print(f"{resultesp} ** {resultT2}={resultesp**resultT2}")



