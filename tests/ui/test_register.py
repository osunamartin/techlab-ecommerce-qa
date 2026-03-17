#from utils.config import BASE_UI_URL
from playwright.sync_api import expect
from pages.auth_page import AuthPage
from utils.config import BASE_UI_URL

'''
#Registra un nuevo usuario, el fixture test_user genera un email único para evitar conflictos con registros anteriores.
def test_registro_usuario(page, test_user):
    
    page.goto(BASE_UI_URL)
    page.locator("#registroNombre").fill(test_user["nombre"])
    page.locator("#registroApellido").fill(test_user["apellido"])
    page.locator("#registroEmail").fill(test_user["email"])
    page.locator("#registroPassword").fill(test_user["password"])
    page.locator("#registroTelefono").fill(test_user["telefono"])
    page.locator("#registroDireccion").fill(test_user["direccion"])
    page.locator("#formRegistro > button").click()

    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible()
'''
#El test_user es el fixture que genera un usuario único para cada test, ya se encarga de entrar a la página.
def test_registro_usuario(page, test_user):
    register_page = AuthPage(page)
    register_page.abrir()
    register_page.registrar_usuario(test_user) #entrás al método de authpage y lo llamás, pasandole el test_user del conftest como parámetro.
    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible()