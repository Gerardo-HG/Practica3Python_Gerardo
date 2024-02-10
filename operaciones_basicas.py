
def ingreso_datos(mensaje="Ingrese un numero: "):
    try:
        number=int(input(mensaje))
        return number
    except ValueError:
        print("Número invalido, vuelve a ingresar el dato")
        return ingreso_datos(mensaje)
    

def convertir_entero(mensaje="Ingrese un número entero:  "):
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Número inválido, vuelve a ingresar el dato........")
            return convertir_entero(mensaje)


    
    
    
    
    
    
if __name__ == '__main__':
    print(ingreso_datos())
    print(convertir_entero())
    