from math import sqrt


#Creamos la clase punto

class Punto:
    #Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #El método str para imprimir por pantalla
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    #El método cuadrante tiene en cuenta tambien la posición sobre los ejes
    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            return "({}, {}) está sobre el eje Y".format(self.x, self.y)
        elif self.x != 0 and self.y == 0:
            return "({}, {}) está sobre el eje X".format(self.x, self.y)
        elif self.x == 0 and self.y == 0:
            return "({}, {}) está en el origen de coordenadas".format(self.x, self.y)
        elif self.x > 0 and self.y > 0:
            return "({}, {}) está en el Primer Cuadrante".format(self.x, self.y)
        elif self.x < 0 and self.y > 0:
            return "({}, {}) está en el Segundo Cuadrante".format(self.x, self.y)
        elif self.x < 0 and self.y < 0:
            return "({}, {}) está en el Tercer Cuadrante".format(self.x, self.y)
        elif self.x > 0 and self.y < 0:
            return "({}, {}) está en el Cuarto Cuadrante".format(self.x, self.y)
    
    #Formamos el método vector
    def vector(self, P):
        return "V=({}, {})".format((P.x-self.x), (P.y - self.y))
    
    #Método de distancia entre puntos
    def distancia(self, P):
        return "distancia={}".format(sqrt((P.x-self.x)**2+(P.y-self.y)**2))
        

#El rectangulo

class Rectangulo:
    #Constructor y str
    def __init__(self, P=Punto(), Q=Punto()):
        self.P = P
        self.Q = Q
    
    def __str__(self):
        return "Punto 1: {}, Punto 2: {}".format(self.P, self.Q)
    
    #La base del rectángulo y su altura
    def base(self):
        print("La base del rectángulo es: {}u".format(abs(self.Q.x-self.P.x)))
        return abs(self.Q.x-self.P.x)

    def altura(self):
        print("La altura del rectángulo es: {}u".format(abs(self.Q.y-self.P.y)))
        return abs(self.Q.y-self.P.y)
    
    #El área
    def area(self):
        return "El área del rectángulo es: {}u^2".format(Rectangulo.base(self) * Rectangulo.altura(self))


p1 = Punto(-8, 5)
p2 = Punto(1, 1)
J = Rectangulo(P=p1, Q=p2)
print(J)
print(J.area())