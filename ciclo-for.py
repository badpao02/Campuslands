
# ******
# *    *
# *    *
# *    *
# ******



for i in range(6):
    print("*", end="")

print("")
for i in range(3):
    print("*    *")

for i in range(6):
    print("*", end="")
print("")
#el usuario le dice el tamaño de la piramide:
#ejemplo: 
#input :4 
# output: 
#*
#**
#***
#**** 

cantidadDeFilas = int(input("ingresa la cantidad de filas"))

for i in range (cantidadDeFilas): 
    print("*"* (i +1))



