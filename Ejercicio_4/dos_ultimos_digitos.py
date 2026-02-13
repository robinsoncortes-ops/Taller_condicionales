#programa para verificar si los dos ultimos digitos son iguales

#input
print("                            ")
print("    ultimo digito iguales   ")
print("                            ")
X = int(input("digite un numero: "))

#processing 
ultimo_digito = X % 10
penultimo_digito = (X//10)%10
if (ultimo_digito == penultimo_digito):
    rta = "igual"
else:
    rta = "diferentes"

#output
print("                 ")
print("    resultado"    )
print("                 ")
print("el numero ingresado fue: " + str(X))
print("su ultimo digitos: " + str(ultimo_digito))
print("su penultimo digito es: " + str(penultimo_digito)) 
print("los dos ultimos digitos son " + rta)