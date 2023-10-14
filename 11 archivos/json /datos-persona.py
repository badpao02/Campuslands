import json 
def guardarEmpleado(lstPersonal, ruta):
    try: 
        fd = open(ruta, "w")
    except Exception as e:
        print("error al abrir el archivo para guardar al empleado.\n", e)
        return None
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la informacion del empleado.\n" , e)
        return None

    fd.close()
    return True
    
def existeId(id, lstPersonal):
    for datos in lstPersonal:
        k = int(list(datos.keys()[0]))
        if k == id:
            return True
    return False

def borrarPersonal(lstPersonal, rutaFile):
    print

def agregarPersonal(lstPersonal):
    print("\n\n1. Agregar Personal")

    id = int(input("ingrese el ID: "))
    while existeId(id, lstPersonal):
        print("---> ya exite un empleado con ese ID")
        input()
        id = int(input("\ningrese el ID"))


    nombre = input("nombre: ")
    edad = int(input("edad: "))
    sexo = input("sexo (M/F): ")
    telefono = input("telefono: ")
    
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo,"telefono":telefono}
    lstPersonal.append(dicEmpleado)

    if guardarEmpleado(lstPersonal, ruta) == True:
        input("El empleado ha sido registrado con exito. \n  presione culaquier tecla para continuar.. ")
    else:
        input("error al guardar empleado")

    guardarEmpleado(lstPersonal, rutaFile)

    input("el empleado ha sido registrado con exito.\npresione cualquier tecla para continuar..") 
def menu():
    while True:
        try:
            print("*** REGISTRO DEL PERSONAL ***".center(40))
            print("MENU".center(40))
            print("1. Agregar ")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. ver")
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
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("error al intentar abrir el archivo\n" + d)
            return None
    try:
        linea = fd.readline()
        if linea.strip()!= "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("error al cargar la informacion\n", e)
        return None
        
    print(lstPersonal)
    fd.close()
    return lstPersonal   


#*** programa principal***
rutaFile = "11 archivos/json /datospersona.json"
lstPersonal = []
cargarInfo(lstPersonal, rutaFile)

while True:
    op = menu()
    if op == 1:
        #agregar
        agregarPersonal(lstPersonal, rutaFile)
        pass 
    elif op == 2:
        #modificar
        pass
    elif op ==3:
        #borrar 
        pass
    elif op ==4:
        #ver
        pass
    else:
        #salir
        print("\ngracias por usar el programa")
        break
        
        