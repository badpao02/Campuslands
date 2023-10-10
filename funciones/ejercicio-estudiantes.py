def resultadoEstudiante(n1,n2,n3,n4,n5):
    promedio = (n1+n2+n3+n4+n5) /5 
    if promedio > 3.5:
        return True
    else: 
        return False
    
nota1=float(input("ingrese la nota 1:"))
nota2=float(input("ingrese la nota 2"))
nota3=float(input("ingrese la nota 3"))
nota4=float(input("ingrese la nota 4"))
nota5=float(input("ingrese la nota 5"))

if resultadoEstudiante(nota1,nota2,nota3,nota4,nota5):

    print("gano el año")
else:
    print("perdio el año")
    
    

