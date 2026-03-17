class AdminPage:

    def __init__(self, page):
        self.page = page
        self.admin_page = page.get_by_role("link", name="Administración")

    def ir_a_la_pagina_admin(self):
        self.admin_page.click()

    def ver_stock_bajo(self):
        self.get_by_role("link", name="Ver Alertas").click()
    
    def ver_todos_los_pedidos(self):
        self.get_by_role("link", name="Ver Pedidos").click()