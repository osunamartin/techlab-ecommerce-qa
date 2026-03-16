class CartPage:

    def __init__(self, page):

        self.page = page
        self.productos = page.locator("#productos")

    def aumentar_cantidad_del_producto(self, nombre_producto, cantidad):
        
        #Busca el producto en el carrito del fixture producto_test y lo aumenta la cantidad.
        producto = self.page.locator(f"text={nombre_producto}")
        
        producto.locator("..").locator("#aumentarCantidad(1,1)").click()

    def reducir_cantidad_del_producto(self, nombre_producto, cantidad):

        #Busca el producto en el carrito del fixture producto_test y lo reducira la cantidad.
        producto = self.page.locator(f"text={nombre_producto}")

        producto.locator("..").locator("#aumentarCantidad(1,-1)").click()
    
    def eliminar_producto_del_carrito(self, nombre_producto):

        #Busca el producto en el carrito del fixture producto_test y lo elimina.
        producto = self.page.locator(f"text={nombre_producto}")

        producto.locator("..").locator("#eliminarDelCarrito").click()

    def realizar_pedido(self):

        self.page.locator("#realizarPedido").click()


