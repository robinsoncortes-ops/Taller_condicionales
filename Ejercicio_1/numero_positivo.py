# programa para calcular si un numero es pocitivo

#input
print("                 ")
print("  numero positivo")
print("                 ")
X = int(input("digite un numero: "))

#processing
if (X>0): 
    rta = "positivo"
else:
    rta = "negativo o cero"

#output
print("                 ")
print("    resultado"    )
print("                 ")
print("El numero " + str(X) + " es " + rta)
