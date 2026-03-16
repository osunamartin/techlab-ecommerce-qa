class ProductsPage:

    def __init__(self, page):
        #La página 
        self.page = page
        #El elemento que contiene todos los productos.
        self.productos = page.locator("#productos") 

        #Los botones en esa página.
        self.agregar_producto_button = page.get_by_role("button", name="Agregar al carrito")
        self.editar_producto_button = page.get_by_role("button", name="Editar")
        self.eliminar_producto_button = page.get_by_role("button", name="Eliminar")
    
    #Los métodos(acciones) que se pueden realizar en esa página.
    def agregar_producto_al_carrito(self):

        #Click al botón agregar producto al carrito.
        self.agregar_producto_button.click()

    # Sólo admin
    def crear_producto(self):
        
        #Click al botón de crear productos.
        self.agregar_producto_button.click()

    # Sólo admin
    def editar_producto(self, producto):

        #Click al botón de editar productos.
        self.editar_producto_button.click()

        #Los datos a editar del producto.
        self.page.locator("#productoNombre").fill(producto["nombre"])
        self.page.locator("#productoPrecio").fill(str(producto["precio"]))
        self.page.locator("#productoDescripcion").fill(producto["descripcion"])
        self.page.locator("#productoCategoria").select_option(producto["categoria"])
        self.page.locator("#productoImagen").fill(producto["imagen"])
        self.page.locator("#productoStock").fill(str(producto["stock"]))
        
        #El click a guardar cambios en producto.
        self.page.locator("#guardarProducto").click()

    # Sólo admin
    def eliminar_producto(self):

        #Click al botón eliminar producto.
        self.eliminar_producto_button.click()
