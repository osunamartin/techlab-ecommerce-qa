class OrdersPage:

    def __init__(self, page):

        #La página (o navegador)
        self.page = page
        #El link a la página.
        self.orders_page = page.get_by_text("Mis Pedidos").first #El enlace a la página de pedidos.
        #Los elementos de la página DENTRO (cada uno de los pedidos, en este caso)
        self.pedidos = page.locator("#pedidos")
        
        
    #El método para clickear e ir a la página de pedidos.
    def ir_a_la_pagina_de_pedidos(self):
        self.orders_page.click()

    def obtener_pedido(self, producto):
        return self.page.locator(f"text={producto['nombre']}").first

    #REVISAR LÓGICA ACÁ PARA QUE LOS TEST NO AGARREN EL PRIMER PEDIDO QUE VEAN.
    #Usa self.pedido y no self.page porque interactúa DENTRO de cada elemento de la página.

    def ver_detalle_pedido(self):
        self.pedidos.locator(f"text={"Ver Detalle"}").click()

    #Sólo admin
    def confirmar_pedido(self):
        self.pedidos.locator(f"text={"Confirmar"}").click()
    
    #Sólo admin
    def cancelar_pedido(self):
        self.pedidos.locator(f"text={"Cancelar"}").click()