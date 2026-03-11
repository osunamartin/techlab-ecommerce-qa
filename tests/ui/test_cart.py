from playwright.sync_api import expect

#Prueba E2E de agregar un producto al carrito, utilizando un producto creado dinámicamente para la prueba, y un usuario admin para evitar problemas de permisos.

def test_agregar_producto_al_carrito(page, login_admin, producto_test):

    producto = page.locator(".product-card", has_text=producto_test["nombre"])
    
    producto.get_by_role("button", name="Agregar").click()
    
    page.get_by_role("button", name="🛒 Carrito").click()

    expect(page.locator("text=Producto Automation")).to_be_visible()


def test_e2e_pedido(page, login_admin, producto_test_automation):

    #producto = page.locator(".product-card", has_text=producto_test_automation["nombre"])
    #producto.wait_for()
    producto = page.locator(".product-card").filter(has_text=producto_test_automation["nombre"]).first

    producto.get_by_role("button", name="Agregar").click()

    page.get_by_role("button", name="🛒 Carrito").click()

    page.get_by_role("button", name="Realizar Pedido").click()

    page.get_by_role("link", name="Mis Pedidos").click()
    
    assert page.get_by_text(producto_test_automation["nombre"]).first.is_visible()



    
    



