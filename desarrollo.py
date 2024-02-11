import random

def generar_aleatorio():
    lista=[]
    for i in range(20):
            #print(random.randrange(0,101),end='  ')
            numero=random.randrange(0,101)
            lista.append(numero)
    return lista
            


print("\n")
def ordenar_lista(lista):
    return sorted(lista)
    





