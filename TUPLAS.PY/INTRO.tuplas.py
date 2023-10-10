# las tuplas son estructuras inmutables  osea no se pueden cambiar se crean con parentesis 
 #para crear un conjunto es con llaves , para crear una lista en corchete cuadrado...
# add , es agregar 
# la diferencian entre una lista y , un conjunto es una lista sin elemnetos repetidos
#interseccion es elementos comunes en ambos 

#ejercicio de datos 

n= int(input("english newspaper: "))
lstEng =[]
for i in range(n):
    lstEng.append(input())

n= int(input("fresh newspaper: "))
lstFresh = []
for i in range (n):
    lstFresh.append(input())

result= set(lstEng) - set(lstFresh) 
print("student only english newspaper", len(result))
