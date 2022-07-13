#Libreria de graficos
 

import struct #esta libreria si se puede usar

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Renderer(object):
    #INICIALIZADOR
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.clearColor = color(0,0,0)
        self.currentColor = color(1,1,1)

        self.glViewport(0,0,self.width,self.height)

        self.glClear()

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor (self, r, g, b): 
       
        self.currentColor = color(r,g,b)


    #funcion para borrar todos los pixeles y crear el array de pixeles.
    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]

    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPixel(x, y, clr)

    #funcion para dibujar una linea
    def glLine(self, x0, y0, x1, y1):
        #dibujamos la linea
        self.glLineAux(x0, y0, x1, y1)
        #dibujamos el pixel en el centro de la linea
        self.glVertex(x0, y0)
        self.glVertex(x1, y1)

        
    def glPixel(self, x, y, clr = None):
         if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor 

    def glPixelViewport(self, x, y, clr = None):
        x = (x + 1) * (self.vpWidth / 2) + self.vpX
        y = (y + 1) * (self.vpHeight / 2) + self.vpY
        x = int(x)
        y = int(y)
        self.glPixel(x , y , clr)
    #funcion para poder abrir el archivo con un visualizador o crear la imagen. 
    def glFinish(self, filename):
        with open(filename, "wb") as file: 
            #header o encabezado de la imagen
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14+40+(self.width * self.height*3)))
            file.write(dword(0))
            file.write(dword(14+40))

            #infoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.height*self.width*3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #colortable
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
    
    #viewport
    def glViewport(self, posX,posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

        self.viewport = (posX, posY, width, height)


    
        
    
