import math
def distancia (xt,yt,xs,ys):
    d=math.sqrt((xt-xs)**2+(yt-ys)**2)
    return d
x1=1
x2=3
y1=2
y2=4

dist= distancia(x1,y1,x2,y2)
print(f"la distancia es {dist:.3f}")




