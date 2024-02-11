import desarrollo


def main():
    print("======BIENVENIDO AL PROGRAMA=======")
    print("\n\tMostrando números aleatorios entre 0 y 100")
    b=desarrollo.generar_aleatorio()
    print(b)
    print("\n\tOrdenando la lista y mostrandola por pantalla")
    print(desarrollo.ordenar_lista(b))

    
main()