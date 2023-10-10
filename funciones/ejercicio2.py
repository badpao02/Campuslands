import math
def distancia (xt,yt,xs,ys):
    d=math.sqrt((xt-xs)**2+(yt-ys)**2)
    return d

def perimetroTriangulo(xp,yp,xq,yq,xr,yr):
    perimetro = distancia(xp,yp,xr,yr) + distancia (xr,yr,xq,yq) + distancia(xq,yq,xp,yp)
    return perimetro
x1=1
y1=4
x2=3
y2=0
x3=5
y3=3

print(f"el perimetro del triangulo:{perimetroTriangulo(x1,y1,x2,y2,x3,y3):.3f}")


