from operaciones import ingresar_numero,suma_numeros,resta_numeros,multiplicacion,division
def main():
    print("******BIENVENIDO AL PROGRAMA******")
    print("\n")
    
    
    print(""" ---------  Menú iterativo del programa -------------
                    1.Realizar la suma de los números
                    2.Realizar la resta de los números
                    3.Realizar el producto de los números
                    4.Realizar la división de los números
                    5.Salir del programa""")
    
    
    
    while(True):
        
        a=ingresar_numero()
        b=ingresar_numero()
        
        print("\n")
        opcion=int(input("Ingrese una opción:   "))

        if opcion == 1:
            print("Suma de los numeros -> ",suma_numeros(a,b))
            break
        elif opcion == 2:
            print("Resta de los numeros -> ",resta_numeros(a,b))
            break            
        elif opcion == 3:
            print("Producto de los numeros -> ",multiplicacion(a,b))
            break
        elif opcion == 4:
            print("Division de los numeros -> ",division(a,b))
            break
        elif opcion == 5:
            break
        else:
            print("Opción no válida....")
    
    
    
if __name__ == '__main__':
    main()