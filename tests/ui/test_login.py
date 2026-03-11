import re
from playwright.sync_api import Playwright, sync_playwright, expect
from utils.config import BASE_UI_URL, ADMIN_USER, CLIENT_USER

#Probar si un usuario ADMIN puede iniciar sesión correctamente y acceder al catálogo de productos.
def test_admin_ve_panel(page, login_admin):
    
    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible() #El catálogo de productos debería ser visible para un admin.
   
#Probar si un usuario CLIENTE puede iniciar sesión correctamente y acceder al catálogo de productos.
def test_cliente_ve_panel(page, login_cliente):
    
    heading = page.locator("h2", has_text="Catálogo de Productos")
    expect(heading).to_be_visible() #El catálogo de productos debería ser visible para un cliente.

def test_login_invalido(page, login_invalido):

    #Buscar el mensaje de error que aparece al intentar iniciar sesión con credenciales inválidas.
    error_message = page.locator(".error-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Credenciales inválidas")


    
    



    
