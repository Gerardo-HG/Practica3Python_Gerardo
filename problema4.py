import operaciones as ope

class Rectangulo:
    
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
        
    
    def calcular_area(self):
        print(f'El área del rectángulo es {self.largo*self.ancho}')
        

def main():
    print("********  BIENVENIDO AL PROGRAMA ********")
    print("\nIngresando valores para el largo y ancho")
    L=ope.ingreso_datos()
    A=ope.ingreso_datos()

    rectangulito=Rectangulo(L,A)
    rectangulito.calcular_area()
    
    
    

if __name__ == '__main__':
    print(main())
    













