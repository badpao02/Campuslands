milista=[] # lista vacia 
milista=list() # lista vacia 

nomCampers=["juan","yulieth","lorenzo","manuel","david"]
print(nomCampers)
print(nomCampers[1])
nomCampers[1] = "julieth"
print(nomCampers[1])

#slices 
print(nomCampers[2:4]) # posicion lorenzo y manuel 
print(nomCampers[::-1]) # invertido ::

nomCampers_juan=["daniela","maria","juliana","sandra","carolina"]
print(nomCampers_juan)
#nomCampers += nomCampers_juan # se juantan las dos listas 
#print(nomCampers) 

pass 

# metodos de listas 
nomCampers.append("kevin")   #queda a final de la lista de nomCampers metodo append
print(nomCampers)

nomCampers.extend(nomCampers_juan) #coge los elementos de la lista al final 
print(nomCampers)
print(nomCampers[-1])  #agrega cada elemento al final  
 

nomCampers.insert(1,"carlos") # poder insertar los elementos de cada posiciones 
print(nomCampers) 

nomCampers.pop() #elimina el ultimo elemento 
print(nomCampers)

nomCampers.pop(-3) #elimina la posicion 3 de la lista si le doy la orden 
print(nomCampers) 

nomCampers.remove("sandra")
print(nomCampers)

nomCampers.sort() # ordenar por orden alfabetico 
print(nomCampers) 

nomCampers.insert(2,"daniel")
nomCampers.sort()
print(nomCampers)

nomCampers.sort(reverse=True)
print(nomCampers)

