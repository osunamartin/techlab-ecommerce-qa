class OrdersPage:

    def __init__(self, page):
        self.page = page
        self.pedidos = page.locator("#pedidos")

    #REVISAR LÓGICA ACÁ PARA QUE LOS TEST NO AGARREN EL PRIMER PEDIDO QUE VEAN.

    def ver_detalle_pedido(self):
        self.pedidos.locator(f"text={"ver detalle"}").click()

    #Sólo admin
    def confirmar_pedido(self):
        self.pedidos.locator(f"text={"Confirmar"}").click()
    
    #Sólo admin
    def cancelar_pedido(self):
        self.pedidos.locator(f"text={"Cancelar"}").click()