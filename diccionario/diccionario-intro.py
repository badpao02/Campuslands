# los diciconarios permiten almacenar valores indexados, atraves de claves lo cual permite realizar una busqueda mas eficiente 

empleado = {}  #diccionario vacio 
empleado = dict() # otra opcion de diccionario vacio  
empleado = {"nombre": "sergio medina", "cargo": "programador", "salario":4000000}
print(empleado["cargo"]) 
print(empleado.get("cargo")) #Python, get() es un método de diccionario que se utiliza para obtener el valor de una clave del diccionario. Si la clave no existe en el diccionario, get() devolverá None.
#print(empleado["apellido"]) no esta la variable 
print(empleado.get("apellido", "llave no existe")) #imprime none

empleado ["sexo"] = "M"
print(empleado) 

#modificar un valor 
empleado["salario"] = 4500000

# borrar una llave y su valor 
del empleado ["sexo"] 
print(empleado)

#borrar todo el diccionario 
empleado = {}
empleado.clear() # limpia los elementos 
del empleado 

oficina = empleado.copy()
print(oficina) 
oficina["salario"] = 5000000
print(oficina)
print (empleado)

#fromkeys # es para añadir o actualizar datos  
x = () #falta agregar 


#items  es una lista de tuplas y casa una hace llave y valor 
print(empleado.items())


#keys 
print(empleado.keys())

# valius devuelve un listado para tener todos los valores del diccionario 
print(empleado.values())

#pop remueve la ultima en ser intertada  
print(empleado.pop("salario"))
print(empleado)

#popitem 
print(empleado.popitem())
print(empleado)

#setdefault agrega una variable  
print(empleado.setdefault("nombre", "carlos")) 
print(empleado.setdefault("ciudad", "bucaramanga"))
