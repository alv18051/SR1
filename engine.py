#Programa principal
import random
from gl import *
alto = 600  #alto de la pantalla
ancho = 512 #ancho de la pantalla
rende = Renderer(alto,ancho)

#y = mx + b

v0 = V2(ancho/2,alto/2)

#Hexagono 
rende.glLine(V2(275,200), V2(375,200), color(1,0,0))
rende.glLine(V2(275,300), V2(375,300), color(1,0,0))
rende.glLine(V2(375,200), V2(425,250), color(1,0,0))
rende.glLine(V2(225,250), V2(275,200), color(1,0,0))
rende.glLine(V2(225,250), V2(275,300), color(1,0,0))
rende.glLine(V2(375,300), V2(425,250), color(1,0,0))
#triangulo
rende.glLine(V2(100,100), V2(150,150), color(1,0,1))
rende.glLine(V2(150,150), V2(200,100), color(1,0,1))
rende.glLine(V2(100,100), V2(200,100), color(1,0,1))
#Rectangulo
rende.glLine(V2(430,100), V2(430,150), color(0,0,1))
rende.glLine(V2(530,100), V2(530,150), color(0,0,1))
rende.glLine(V2(430,100), V2(530,100), color(0,0,1))
rende.glLine(V2(430,150), V2(530,150), color(0,0,1))
#Paralelogramo
rende.glLine(V2(380,400), V2(430,450), color(0,1,0))
rende.glLine(V2(480,400), V2(530,450), color(0,1,0))
rende.glLine(V2(380,400), V2(480,400), color(0,1,0))
rende.glLine(V2(430,450), V2(530,450), color(0,1,0))
#Trapecio 
rende.glLine(V2(100,400), V2(250,400), color(0,1,1))
rende.glLine(V2(150,450), V2(200,450), color(0,1,1))
rende.glLine(V2(100,400), V2(150,450), color(0,1,1))
rende.glLine(V2(200,450), V2(250,400), color(0,1,1))

# for y in range(0, alto, 50):
#     rende.glLine(v0,V2(ancho,y))

# for x in range(0, ancho, 50):
#     rende.glLine(v0,V2(x,alto),color(1,0,0))

# for x in range(0, ancho, 50):
#     rende.glLine(v0,V2(x,0),color(0,1,0))

# for x  in range(0, ancho, 50):
#     rende.glLine(v0,V2(0,x),color(0,0,1))

# v1 = V2(ancho,alto/2)

# v2 = V2(ancho,350)

# v3 = V2(ancho,alto)

# v4 = V2(350,alto)

#rende.glLine(v0,v1)
# rende.glLine(v0,v2)
# rende.glLine(v0,v3)
# rende.glLine(v0,v4)

# x = 0
# dx = ancho / 100
# dy = alto / 100

# x = 0 
# y = alto
# for i in range(0, 100):
#     rende.glLine(V2(x,0),V2(0,y))
#     rende.glLine(V2(x,alto),V2(ancho,y))
#     rende.glLine(v0,V2(ancho,y))
#     rende.glLine(v0,V2(x,alto),color(1,0,0))
#     rende.glLine(v0,V2(x,0),color(0,1,0))
#     rende.glLine(v0,V2(0,x),color(0,0,1))
#     x += dx
#     y -= dy
    


rende.glFinish("./salida.bmp")