from clases import Rectangulo,Circulo,Cuadrado


def main():
    print("******* BIENVENIDOS AL PROGRAMA *******")
    print("\n")
    print("""--------------MENÚ ITERATIVO ---------------
                    
                    1.Calcular el área de un Círuclo
                    2.Calcular el área de un Rectángulo
                    3.Calcular el área de un Cuadrado
                    4.Salir""")
    
    
    while(True):
        opcion=int(input("Ingrese una opción:   "))
        
        if opcion == 1:
            print("Creando un objeto de la clase Círculo......")
            radius=float(input("Ingrese un valor para el radio:   "))
            circu=Circulo(radius)
            circu.__str__()
            circu.areaCirculo()
            print("\n")
            continue
        
        
        elif opcion == 2:
            print("Creando un objeto de la clase Rectángulo......")
            anchor=float(input("Ingrese un valor para el ancho:   "))
            large=float(input("Ingrese un valor para el largo:  "))
            recta=Rectangulo(anchor,large)
            recta.__str__()
            recta.areaRectangulo()
            print("\n")
            continue
        
        elif opcion == 3:
            print("Creando un objeto de la clase Cuadrado......")
            side=float(input("Ingrese un valor para el lado:  "))
            cuadra=Cuadrado(side)
            cuadra.__str__()
            cuadra.areaCuadrado()
            print("\n")
            continue
        
        elif opcion == 4:
            print("!Hasta Luego!")
            break
        
        
if __name__ == '__main__':
        main()