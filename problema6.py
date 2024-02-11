class Producto:
    
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        
    def mostrar_producto(self):
        print("""\t\tProducto --> {}
                Precio --> {} soles""".format(self.nombre,self.precio))
        

class Catalogo:
    catalogo_productos=[]
    
    def __init__(self,catalogo_productos=[]):
        self.catalogo_productos=catalogo_productos
        
    def agregarProducto(self,product):
        self.catalogo_productos.append(product)
        
    def mostrarListaProductos(self):
        for p in self.catalogo_productos:
            print(p.mostrar_producto())
            
            
producto1=Producto("Aceite",3.5)
producto2=Producto("Gelatina",2)
producto3=Producto("Tallarines",6)
producto4=Producto("Gaseosa",3)

catalogo=[]

c=Catalogo(catalogo)
c.agregarProducto(producto1)
c.agregarProducto(producto2)
c.agregarProducto(producto3)
c.agregarProducto(producto4)
c.mostrarListaProductos()