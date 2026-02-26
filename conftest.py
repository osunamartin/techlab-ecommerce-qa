import pytest
from playwright.sync_api import sync_playwright
import uuid

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

#Para registro dinámico de usuarios
@pytest.fixture
def test_user():
    unique = uuid.uuid4().hex[:8] #Crea un identificador único, para no repetir.

    return {
        "nombre": "Prueba",
        "apellido": "Automation",
        "email": f"qaauto_{unique}@email.com", #Al estar el unique, el fixture no necesita eliminar el usuario después de la prueba.
        "password": "qa123",
        "telefono": "123456789",
        "direccion": "Fake St 123"
    }

@pytest.fixture
def login_admin(page):
    page.goto("http://localhost:8080/")
    page.fill("#loginEmail", "admin@techlab.com")
    page.fill("#loginPassword", "admin123")
    page.get_by_role("button", name="Iniciar Sesión").click()
    yield page