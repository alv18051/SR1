#Programa principal
import random
from gl import *
alto = 1024
ancho = 512
rende = Renderer(alto,ancho)

rende.glClearColor(0,1,0)
rende.glColor(1,1,1)

rende.glClear()

#rende.glPixel(50,75)

#static
#for i in range(alto):
#    for j in range(ancho):
#        if random.randint(0,10) == 5:
#            rende.glPixel(i,j)
#        else:
#            rende.glPixel(i,j,color(1,0,0))
        
#square
#for i in range(alto):
#    for j in range(ancho):
#        if (i > 100 and i < 200) and (j > 100 and j < 200):
#            rende.glPixel(i,j,color(1,0,0))
#        else:
#            rende.glPixel(i,j)


#circle
# for i in range(alto):
#    for j in range(ancho):
#        if (i - 200)**2 + (j - 200)**2 < 100**2:
#            rende.glPixel(i,j,color(1,0,0))
#        else:
#            rende.glPixel(i,j)

#starfield
for i in range(alto):
    for j in range(ancho):
        if random.random() > 0.99:
            size = random.randrange(0,3,1)
            
            if size == 0:
                rende.glPixel(i,j,color(1,0,0))

            elif size == 1:
                rende.glPixel(i,j,color(0,1,0))
                rende.glPixel(i,j+1,color(0,1,0))
                rende.glPixel(i+1,j+1,color(0,1,0))
                rende.glPixel(i+1,j,color(0,1,0))

            elif size == 2:
                rende.glPixel(i,j,color(0,0,1))
                rende.glPixel(i,j+1,color(0,0,1))
                rende.glPixel(i,j-1,color(0,0,1))
                rende.glPixel(i+1,j,color(0,0,1))
                rende.glPixel(i-1,j,color(0,0,1))
            
            
        else:
            rende.glPixel(i,j)




rende.glFinish("./salida.bmp")