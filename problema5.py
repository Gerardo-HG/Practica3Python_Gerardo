class Alumno:
    
    def __init__(self,nombre,numero_registro):
        self.nombre=nombre
        self.numero_registro=numero_registro
        self.edad=None
        self.notas=[]
    def Display(self):
        print("""======Información del estudiante=====
                Nombre ---> {}
                Numero de Registro ---> {}""".format(self.nombre,self.numero_registro))
        if self.edad is not None:
            print("\t\tEdad del estudiante --->{}".format(self.edad)) 
        if self.notas:
            print("\t\tNotas del estudiante:  ")
            for i,n in enumerate(self.notas):
                print(f'\t\tNota {i+1}: {n}')
    
    def setAge(self,edad):
        self.edad=edad
        pass    
    
    def setNota(self,*nota):
        self.notas=list(nota)


if __name__ == '__main__':
    alumno_1=Alumno("Gerardo",106)
    alumno_1.setAge(20)
    alumno_1.setNota(18,15,16,17)
    
    alumno_1.Display()

