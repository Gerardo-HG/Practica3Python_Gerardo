import math
class Circulo:
    
    def __init__(self,radio):
        self.radio_circulo=radio
        
    def calcular_area(self):
        area=math.pi*math.pow(self.radio_circulo,2)
        
        return area
    
    

if __name__ == '__main__':
    bandera=True
    while(bandera==True):    
        try:
            radio_c=float(input("Ingrese un valor de radio:  "))
            print("\n")
            circulito=Circulo(radio_c)
            print()
            print(f'Area del circulo es {circulito.calcular_area()}')
            bandera=False
            
        except ValueError:
            print("Ingrese un valor númerico, por favor")
            
            bandera=True