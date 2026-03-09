
#Prueba E2E de agregar un producto al carrito, utilizando un producto creado dinámicamente para la prueba, y un usuario admin para evitar problemas de permisos.

def test_agregar_producto_al_carrito(page, login_admin, producto_test):

    producto = page.locator(".product-card", has_text=producto_test["nombre"])

    producto.wait_for()

    producto.get_by_role("button", name="Agregar").click()

    page.get_by_role("button", name="🛒 Carrito").click()

    #Hardcodeado el nombre del producto creado, pero se podría mejorar guardando el nombre del producto creado en el fixture producto_test

    assert page.locator("text=Producto Automation").first.is_visible()



