from playwright.sync_api import expect
#from utils.config import BASE_UI_URL
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.orders_page import OrdersPage

#Prueba E2E de agregar un producto al carrito, utilizando un producto creado dinámicamente para la prueba, y un usuario admin para evitar problemas de permisos.

'''

def test_e2e_pedido(page, login_admin, producto_test_automation):

    producto = page.locator(".product-card", has_text=producto_test_automation["nombre"]) 

    expect(producto).to_be_visible() #Se asegura que esté el producto creado por el fixture.

    producto.get_by_role("button", name="Agregar").click()

    page.get_by_role("button", name="🛒 Carrito").click()

    page.get_by_role("button", name="Realizar Pedido").click()

    page.get_by_role("link", name="Mis Pedidos").click()

    expect(page.get_by_text(producto_test_automation["nombre"])).to_be_visible()
'''

def test_agregar_producto_al_carrito(page, login_admin, producto_test):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    #Para que el producto que se está probando aparezca en la lista de productos.
    page.reload() 

    products_page.agregar_producto_al_carrito(producto_test)
    cart_page.ir_a_la_pagina_carrito()
    expect(cart_page.obtener_producto_en_carrito(producto_test)).to_be_visible()

def test_e2e_pedido(page, login_admin, producto_test_automation):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    orders_page = OrdersPage(page)

    page.reload()
    products_page.agregar_producto_al_carrito(producto_test_automation)

    cart_page.ir_a_la_pagina_carrito()

    cart_page.realizar_pedido()

    orders_page.ir_a_la_pagina_de_pedidos()
    
    #print("llega")
    expect(orders_page.obtener_pedido(producto_test_automation)).to_be_visible()







    
    



