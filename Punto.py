#Creamos la clase punto

class Punto:
    #Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #El método str para imprimir por pantalla
    def __str__(self):
        return "{}({}, {})".format(Punto, self.x, self.y)

    #El método cuadrante tiene en cuenta tambien la posición sobre los ejes
    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            return "{} está sobre el eje Y".format(Punto)
        elif self.x != 0 and self.y == 0:
            return "{} está sobre el eje X".format(Punto)
        elif self.x == 0 and self.y == 0:
            return "{} está en el origen de coordenadas".format(Punto)
        elif self.x > 0 and self.y > 0:
            return "{} está en el Primer Cuadrante".format(Punto)
        
#Prueba
p1 = Punto(1, 1)
p2 = Punto(0, 0)
p3 = Punto(0, 3)
p4 = Punto(4, 0)

print(p1.cuadrante())
print(p2.cuadrante())
print(p3.cuadrante())
print(p4.cuadrante())