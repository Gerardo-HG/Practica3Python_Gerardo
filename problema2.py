def devolver_calificaciones():
    while True:
        try:
            
            calificaciones_cadena = input("Ingrese las calificaciones separadas por comas: ")
            

            calificaciones_lista = calificaciones_cadena.split(',')
            
            
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            
            return calificaciones_enteros  
        except ValueError:
            
            print("Error: Las calificaciones deben ser números enteros. Inténtalo de nuevo.")


calificaciones = devolver_calificaciones()


print("Calificaciones ingresadas:", calificaciones)