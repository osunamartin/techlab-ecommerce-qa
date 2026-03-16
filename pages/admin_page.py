class AdminPage:

    def __init__(self, page):
        self.page = page

    def ver_stock_bajo(self):
        self.get_by_role("link", name="Ver Alertas").click()
    
    def ver_todos_los_pedidos(self):
        self.get_by_role("link", name="Ver Pedidos").click()