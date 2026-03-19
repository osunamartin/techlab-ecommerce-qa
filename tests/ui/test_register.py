#from utils.config import BASE_UI_URL
from playwright.sync_api import expect
from pages.auth_page import AuthPage
from utils.config import BASE_UI_URL

#El test_user es el fixture que genera un usuario único para cada test, ya se encarga de entrar a la página.
def test_registro_usuario(page, test_user):
    page_registro = AuthPage(page)
    page_registro.abrir()
    page_registro.registrar_usuario(test_user) #entrás al método de authpage y lo llamás, pasandole el test_user del conftest como parámetro.
    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible()