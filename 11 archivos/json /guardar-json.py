import json

fd= open("11 archivos/json", "r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"nombre: {e['nombre']}")
    print(f"edad: {e['edad']}")
    print("-" * 30)

    
    fd.close()
