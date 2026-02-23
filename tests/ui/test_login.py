import re
from playwright.sync_api import Playwright, sync_playwright, expect
from utils.config import BASE_UI_URL, ADMIN_USER, CLIENT_USER

#Probar si un usuario ADMIN puede iniciar sesión correctamente y acceder al catálogo de productos.
def test_admin_login(page):
    page.goto(BASE_UI_URL)

    page.locator("#loginEmail").fill(ADMIN_USER["email"])
    page.locator("#loginPassword").fill(ADMIN_USER["password"])
    page.get_by_role("button", name="Iniciar Sesión").click()

    heading = page.locator("h2", has_text="Catálogo de Productos")
    heading.wait_for()
    assert heading.is_visible()

#Probar si un usuario CLIENTE puede iniciar sesión correctamente y acceder al catálogo de productos.
def test_customer_login(page):
    page.goto(BASE_UI_URL)

    page.locator("#loginEmail").fill(CLIENT_USER["email"])
    page.locator("#loginPassword").fill(CLIENT_USER["password"])
    page.get_by_role("button", name="Iniciar Sesión").click()

    heading = page.locator("h2", has_text="Catálogo de Productos")
    heading.wait_for()
    assert heading.is_visible()




    
