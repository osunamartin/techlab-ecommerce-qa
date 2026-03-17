class CartPage:

    def __init__(self, page):

        self.page = page
        #self.productos = page.locator("#productos")
        self.cart_page = page.get_by_role("link", name="Carrito")

    def ir_a_la_pagina_carrito(self):
        self.cart_page.click()

    def aumentar_cantidad_del_producto(self, nombre_producto, cantidad):
        
        #Busca el producto en el carrito del fixture producto_test y lo aumenta la cantidad.
        producto = self.page.locator(f"text={nombre_producto}")
    
        producto.locator("..").get_by_role("button", name="+").click()

    def reducir_cantidad_del_producto(self, nombre_producto, cantidad):

        #Busca el producto en el carrito del fixture producto_test y lo reducira la cantidad.
        producto = self.page.locator(f"text={nombre_producto}")

        producto.locator("..").get_by_role("button", name="-").click()
    
    def eliminar_producto_del_carrito(self, nombre_producto):

        #Busca el producto en el carrito del fixture producto_test y lo elimina.
        producto = self.page.locator(f"text={nombre_producto}")

        producto.locator("..").locator("#eliminarDelCarrito").click()

    def realizar_pedido(self):

        self.page.locator("#realizarPedido").click()


    #producto = self.page.locator(f"text={nombre_producto}") --> puede ser encapsulado para no repetirlo en cada método.


