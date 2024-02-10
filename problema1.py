import operaciones_basicas as ob 


def fraccion_numero(a,b):
    
    while(True):  
        try:
            resultado=(a/b)
            #4,0
            if a<b:
                if resultado < 0.01:
                    print(" E ")
                    break
                elif resultado >= 0.99:
                    print(" F ")
                    break
                else:
                    print("{} %".format(resultado*100))
                    break
            else:
                print("El numerador debe ser menor al denominador, ingrese otro numero...")
                print(a)
                print(b)
                a=ob.convertir_entero()        
                
        except ZeroDivisionError:
            print("Division entre cero no permitido")
            print("Ingrese otro valor para el denominador porfavor....")
            b=ob.convertir_entero()
            while(True):    
                if b!=0 and b<a:
                        print("Recuerde que el denominador no puede ser cero y debe ser mayor que el numerador...")
                        b=ob.convertir_entero()
                else:
                    break        
            
        except ValueError:
            print("Error. Solo se permite el ingreso de números enteros")


def main():
    print("********** Bienvenido al Programa **********")
    X=ob.convertir_entero()

    Y=ob.convertir_entero()

    print(f'El valor de X es {X}')
    print(f'El vaor de Y es {Y}')
    
    dividir=fraccion_numero(X,Y)
    
    
    
    
    

    
if __name__ == '__main__':
    main()
    