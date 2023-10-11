def calcProdMaxIngresosSem(matVtas,matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f] 

       #Print(lstTotVtas)
        maxVtas = max(lstTotVtas)
        prodMaxVtas = lstTotVtas.index(maxVtas) + 1
        return prodMaxVtas



matPrecios = [1500,5000,6500,2500,22500]
matVtas = [[100,88,92,94,85,110,118],[30,42,31,32,38,40,37], [23,35,39,45,55,60,61],[45,50,56,65,47,57,68],[18,25,33,21,22,28,32]]


pass
print("") 

def calcProdMaxIngresosSem(matVtas,matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f] 

       #Print(lstTotVtas)
        maxVtas = max(lstTotVtas)
        prodMaxVtas = lstTotVtas.index(maxVtas) + 1
        return prodMaxVtas

matPrecios = [1500,5000,6500,2500,22500]
matVtas = [[100,30,23,45,18], [88,42,35,50,25], [92,31,39,56,33], [94,32,45,65,21], [85,38,55,47,22], [110,40,60,57,28], [118,37,61,68,32]]


prodMaxIngeDia = calcProdMaxIngresosSem(matVtas,matPrecios)
print("el producto que mas genera ingresos en la semana es ", prodMaxIngeDia)

 # el otro codigo de la actividad parte 2   
def prodMayVtasSem(mat):
    vsumprod = []
    for f in range(len(mat)):
        sum = 0
        for c in range(len(mat[f])):
            sum += mat[f][c]
        vsumprod.append(sum)
    print(vsumprod)
    return vsumprod.index(max(vsumprod)) + 1

    pmyVtasSem = prodMayVtasSem2(mventas)
    print("El producto que mas vende a la semana es:", pmyVtasSem)