def suma_numeros(numero1,numero2):
    return numero1+numero2

def resta_numeros(numero1,numero2):
    
    return numero1-numero2

def multiplicacion(numero1,numero2):
    return numero1*numero2
    
def division(n1,n2):
    
        
        try:
            resultado = n1/n2
            print(f'División de números -->{resultado}')
        except ZeroDivisionError:
            print("Error. No es posible dividir entre cero")
                
            


def ingresar_numero(mensaje="Ingrese un número:  "):
    try:
        numero=float(input(mensaje))
        return numero
    
    except ValueError:
        print("Tipo de dato no válido")
        return ingresar_numero(mensaje)
    

