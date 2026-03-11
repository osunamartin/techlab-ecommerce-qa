from playwright.sync_api import expect
from utils.config import BASE_UI_URL

#Prueba E2E de agregar un producto al carrito, utilizando un producto creado dinámicamente para la prueba, y un usuario admin para evitar problemas de permisos.

def test_agregar_producto_al_carrito(page, login_admin, producto_test):
    
    page.reload() #Para que el producto que se está probando aparezca en la lista de productos.
    producto = page.locator(".product-card", has_text=producto_test["nombre"])
    
    producto.get_by_role("button", name="Agregar").click()
    
    page.get_by_role("button", name="🛒 Carrito").click()

    expect(page.locator("text=Producto Automation").first).to_be_visible() #El .first es para que sepa cuál es el producto que se está probando.


def test_e2e_pedido(page, login_admin, producto_test_automation):

    producto = page.locator(".product-card", has_text=producto_test_automation["nombre"]) 

    expect(producto).to_be_visible() #Se asegura que esté el producto creado por el fixture.

    producto.get_by_role("button", name="Agregar").click()

    page.get_by_role("button", name="🛒 Carrito").click()

    page.get_by_role("button", name="Realizar Pedido").click()

    page.get_by_role("link", name="Mis Pedidos").click()

    expect(page.get_by_text(producto_test_automation["nombre"])).to_be_visible()




    
    



