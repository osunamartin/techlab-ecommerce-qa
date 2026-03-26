from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.orders_page import OrdersPage

def test_cliente_no_ve_admin(page, login_cliente):
    #Buscar que el enlace de administración no esté en la barra de navegación.
    expect(page.locator("#navLinks").get_by_text("Administración")).not_to_be_visible()

def test_admin_ve_admin(page, login_admin):

    #Buscar el enlace de administración en la barra de navegación, sino no sabe cual elemento es el que tiene que buscar.
    expect(page.locator("#navLinks a", has_text="Administración")).to_be_visible()

#Verifica que el cliente no puede cambiar el estado de un pedido, ya que no es admin.

def test_cliente_no_puede_cambiar_estado_pedido(page, login_cliente, producto_test_automation):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    orders_page = OrdersPage(page)

    page.reload()
    products_page.agregar_producto_al_carrito(producto_test_automation)

    cart_page.ir_a_la_pagina_carrito()

    cart_page.realizar_pedido()

    orders_page.ir_a_la_pagina_de_pedidos()

    pedido = orders_page.obtener_pedido(producto_test_automation)
    
    #Verifica que el pedido no tiene ninguna opción de cambiar el estado.
    expect(pedido.get_by_text("Confirmar")).to_have_count(0)

