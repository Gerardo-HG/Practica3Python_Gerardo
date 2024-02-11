import math
class Circulo:
    def __init__(self,radio):
        self.radio=radio
        
    def __str__(self):
        print(f'Se ha creado un Círculo de radio {self.radio}')
        
    def areaCirculo(self):
        print(f'El área del Círculo es {math.pi*math.pow(self.radio,2)}')
        
        
        
class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
        
    def __str__(self):
        print(f'"Se ha creado un Rectangulo de {self.ancho} m de largo y {self.ancho} m de ancho')
        
    def areaRectangulo(self):
        print(f'El área del Rectángulo es {self.ancho*self.largo}')
        
        
class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
        
    def __str__(self):
        print(f'Se ha creado un Cuadrado de {self.lado} m de lado')
        
    def areaCuadrado(self):
        print(f'El área del Cuadrado es {self.lado*self.lado}')
        
        
if __name__ == '__main__':
    pass