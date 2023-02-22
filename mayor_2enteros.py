# Programa para verificar cual de dos numeros enteros es el mayor 

print("-------------------------")
print("-----mayor 2 enteros-----")
print("-------------------------")

# input 
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

# procesing
if x == y:
    print("Los numeros son iguales...")
     
else:
     if x > y:
    mayor = x
    else:
        mayor = y
# output
print("El mayor entre " + str(x) + " y " + str(y) + " es " + str(mayor))