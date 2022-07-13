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

        self.glClear()

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor (self, r, g, b): 
       
        self.currentColor = color(r,g,b)


    #funcion para borrar todos los pixeles y crear el array de pixeles.
    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]
        
    def glPixel(self, x, y, clr = None):
         if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor 
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
    def glViewport(self, x, y, width, height):
        self.viewport = (x, y, width, height)


    
        
    
