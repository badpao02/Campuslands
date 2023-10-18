import json

def guardarEmpleado(lstPersonal, ruta):
    # Función que guarda los datos de la lista de personal en un archivo JSON
    try:
        with open(ruta, "w") as fd:
            json.dump(lstPersonal, fd)
        return True
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False

def existeId(id, lstPersonal):
    # Función que verifica si un ID existe en la lista de empleados
    for i, datos in enumerate(lstPersonal):
        k = int(list(datos.keys())[0])
        if k == id:
            return i
    return -1

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\n3. Borrar Personal")
    
    id = int(input("Ingrese el ID: "))
    empleado_idx = existeId(id, lstPersonal)
    
    if empleado_idx == -1:
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return
    
    lstPersonal.pop(empleado_idx)  # Elimina el empleado de la lista
    
    if guardarEmpleado(lstPersonal, rutaFile):
        print("El empleado ha sido borrado con éxito")
    else:
        print("Ocurrió un error al borrar el empleado")
    
    input("Presione cualquier tecla para continuar\n")

def modificarPersonal(lstPersonal, rutaFile):
    print("\n\n2. Modificar Personal")
    
    id = int(input("Ingrese el ID del empleado a modificar: "))
    empleado_idx = existeId(id, lstPersonal)
    
    if empleado_idx == -1:
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return
    
    empleado_actual = lstPersonal[empleado_idx][id]
    print("Datos actuales del empleado:")
    print("ID:", id)
    print("Nombre:", empleado_actual["nombre"])
    print("Edad:", empleado_actual["edad"])
    print("Sexo:", empleado_actual["sexo"])
    print("Teléfono:", empleado_actual["telefono"])
    
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_edad = int(input("Nueva edad: "))
    nuevo_sexo = input("Nuevo sexo (M/F): ")
    nuevo_telefono = input("Nuevo teléfono: ")
    
    lstPersonal[empleado_idx][id] = {
        "nombre": nuevo_nombre,
        "edad": nuevo_edad,
        "sexo": nuevo_sexo,
        "telefono": nuevo_telefono
    }
    
    if guardarEmpleado(lstPersonal, rutaFile):
        print("Los datos del empleado han sido modificados con éxito")
    else:
        print("Ocurrió un error al modificar los datos del empleado")
    
    input("Presione cualquier tecla para continuar\n")

def verPersonal(lstPersonal):
    print("\n\n4. Ver Personal")
    print("Lista de empleados:")
    for empleado in lstPersonal:
        empleado_id = list(empleado.keys())[0]
        empleado_data = empleado[empleado_id]
        print(f"ID: {empleado_id}")
        print(f"Nombre: {empleado_data['nombre']}")
        print(f"Edad: {empleado_data['edad']}")
        print(f"Sexo: {empleado_data['sexo']}")
        print(f"Teléfono: {empleado_data['telefono']}")
        print()
    input("Presione cualquier tecla para continuar\n")


def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")
    
    id = int(input("Ingrese el ID: "))
    while existeId(id, lstPersonal) != -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        # si es diferente a -1, entonces el id y existe.
        print("--> Ya existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        id = int(input("\nIngrese el ID: "))
        
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    telefono = input("Teléfono: ")
    
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)
    
    if guardarEmpleado(lstPersonal, ruta) == True:
        input("El empleado ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el empleado.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** REGISTRO DEL PERSONAL ***".center(40))
            print("MENU".center(40))
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Ver")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargarInfo(lstPersonal, ruta):
    try:
        with open(ruta, "r") as fd:
            lstPersonal = json.load(fd)
    except Exception as e:
        lstPersonal = []
    
    return lstPersonal

# *** PROGRAMA PRINCIPAL ***
rutaFile = "datpersonal.json"
lstPersonal = []
lstPersonal = cargarInfo(lstPersonal, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstPersonal, rutaFile)
    elif op == 2:
        modificarPersonal(lstPersonal, rutaFile)
    elif op == 3:
        borrarPersonal(lstPersonal, rutaFile)
    elif op == 4:
        verPersonal(lstPersonal)
    else:
        print("\nGracias por usar el programa")
        break