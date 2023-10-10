# validar el nombre del usuario 
while True:
    try:
        nombre = input("ingrese el nombre del usuario")
        nombre = nombre.strip()
        if len(nombre) == 0 or nombre.isalnum() == False:
            print("Nombre invalido. vuelva a digitarlo.")
            continue
        break
    except Exception as e:
        print("error al ingresar el nombre.\n", e) 

#validar el estrato 
while True:
    try:
        estrato = int(input("ingrese el estrato (1-5): "))
        if estrato < 1 or estrato > 5: 
            print("el estrato no esta en el rango (1-5). intente de nuevo")
            continue
        break 
    except ValueError:
        print("Error. Estrato invalido.")

if estrato ==1:
    tbas = 10000
elif estrato ==2: 
    tbas = 15000
elif estrato ==3:
    tbas=30000
elif estrato ==4:
    tbas = 50000
else:
    tbas = 60000

print ("\n", "=" * 30)
print("nombre:", nombre)
print("tarifa basica:", tbas)

(")")

#ejercicio de Liquidación servicio de matrícula

# Definir la función para calcular el valor neto a pagar de matrícula
def calcular_valor_neto_matricula(codigo, nombre, programa_academico, indicador_beca):

    # Validar el código
    if not isinstance(codigo, int):
        raise ValueError("El código debe ser un número entero.")

    # Validar el nombre
    if not isinstance(nombre, str):
        raise ValueError("El nombre debe ser una cadena de texto.")

    # Validar el programa académico
    if programa_academico not in VALOR_MATRICULA.keys():
        raise ValueError("El programa académico debe ser uno de los siguientes: 1, 2, o 3.")

    # Validar el indicador de beca
    if indicador_beca not in VALOR_DESCUENTO.keys():
        raise ValueError("El indicador de beca debe ser uno de los siguientes: 1, 2, o 3.")

    # Obtener el valor de la matrícula
    valor_matricula = VALOR_MATRICULA[programa_academico]

    # Aplicar el descuento de la beca
    valor_descuento = VALOR_DESCUENTO[indicador_beca]
    valor_matricula_descontada = valor_matricula - valor_descuento

    return valor_matricula_descontada


# Calcular el valor neto a pagar de matrícula
try:
    valor_neto_matricula = calcular_valor_neto_matricula(codigo, nombre, programa_academico, indicador_beca)

# Manejar el error
except ValueError as e:
    print(e)

# Imprimir los resultados
if valor_neto_matricula is not None:
    print("Nombre:", nombre)
    print("Valor a pagar por matrícula:", valor_neto_matricula)
    print("Valor total de matrículas:", valor_neto_matricula)