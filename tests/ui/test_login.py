from playwright.sync_api import expect

#Login con usuario de admin, este primer test valida que el usuario puede iniciar sesión.
def test_admin_ve_panel(page, login_admin):

    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible()

#Login con usuario de cliente, este test valida que el usuario puede iniciar sesión.
def test_cliente_ve_panel(page, login_cliente):

    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible()

#Login con usuario inválido, este test valida que el usuario no puede iniciar sesión.
def test_login_invalido(page, login_invalido):

    error_message = page.locator(".alert-error")
    expect(error_message).to_be_visible()





    
    



    
