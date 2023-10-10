# ejemplos de formatear la salida 

# CON FORMAT 
sueldo = 5600000
print("sueldo: ${:,}".format(sueldo))

interes = 2568.568954112568
print("valor del interes: {:,.3f}".format(interes))

# f-string
print(f"sueldo: ${sueldo:,}")