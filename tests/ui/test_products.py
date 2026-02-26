import test_login

def test_cart(page, login_admin):
    # Inicia sesión utilizando el fixture test_login
    heading = page.locator("h2", has_text="Catálogo de Productos")
    heading.wait_for()
    assert page.locator("#navAdmin > a").is_visible() 

