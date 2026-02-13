#programa para calcular costo de una llamada

#input
print("                 ")
print("  costo llamada  ")
print("                 ")
min = int(input("digite la duracion de una llamada en minutos: "))

#processing
if (min <= 3): 
    costo_llamada = 500
else:
    rta = costo_llamada = 500 + (min - 3)*100

#output
print("                 ")
print("    resultado"    )
print("                 ")
print("costo de la llamada: " + str(costo_llamada))
