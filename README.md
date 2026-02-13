# Taller_condicionales
repositorio de los 6 ejercicios 

## Analisis

## variables de entrada
1  x: digite un numero 
2 min = digite la duracion de la llamada
3 x = digite el numero
4 x = digite el numero
5 A=int(input("digite el valor de A: "))
   B=int(input("digite el valor de B: "))
   C=int(input("digite el valor de C: "))
6 pc = digite el precio costo del producto

### procedimiento
-1 if (X>0): 
    rta = "positivo"
else:
    rta = "negativo o cero"

2 if (min <= 3): 
    costo_llamada = 500
else:
    rta = costo_llamada = 500 + (min - 3)*100

3 mod = X%2
if (mod == 0):
    rta = "par"
else:
    rta = "impar"

4 ultimo_digito = X % 10
penultimo_digito = (X//10)%10
if (ultimo_digito == penultimo_digito):
    rta = "igual"
else:
    rta = "diferentes"

5 if(A>C):
    if(A>C):
        rta=A
    else:
        rta=C
else:
    if(B>C):
        rta=B
    else:
        rta=C


6if(pc<3000):
    pv=(pc*0.15)+pc
else:
    if(pc<6000):
        pv=(pc*0.25)+25
    else:
        pv=pc+500

## Diseños 1

![alt text](image.png)
## Diseños 2

![alt text](image-1.png)
## Diseños 3

![alt text](image-2.png)
## Diseños 4

![alt text](image-4.png)
## Diseños 5

![alt text](image-3.png)
## Diseños 6

![alt text](image-5.png)
