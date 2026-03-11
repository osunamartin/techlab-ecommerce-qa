from playwright.sync_api import expect

def test_cliente_no_ve_admin(page, login_cliente):
    #Buscar que el enlace de administración no esté en la barra de navegación.
    expect(page.locator("#navLinks").get_by_text("Administración")).not_to_be_visible()

def test_admin_ve_admin(page, login_admin):

    #Buscar el enlace de administración en la barra de navegación, sino no sabe cual elemento es el que tiene que buscar.
    expect(page.locator("#navLinks a", has_text="Administración")).to_be_visible()

