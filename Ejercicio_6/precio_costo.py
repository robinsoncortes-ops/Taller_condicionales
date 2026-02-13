# programa en python para calcular el precio costo de un producto

# libreria
import math

#
#input
#

print("                                      ")
print(" calcular precio ventas de un producto")
print("                                      ")

pc=int(input("digite el precio costo del producto: "))

#
#processing
#
if(pc<3000):
    pv=(pc*0.15)+pc
else:
    if(pc<6000):
        pv=(pc*0.25)+25
    else:
        pv=pc+500

#
#output
#

print("                                      ")
print("            resultado                 ")
print("el precio de venta es: " + str(pv))
print("                                      ")