import pytest
from playwright.sync_api import sync_playwright
import uuid
import requests #Para acceso a API

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

#Crear un producto de prueba para las pruebas E2E, y eliminarlo después.
@pytest.fixture
def producto_test():
    producto = {
    "nombre": "Producto Automation",
    "precio": 12345,
    "descripcion": "Descripción del producto de prueba para automatización",
    "categoria": "Auriculares",
    "imagen": "https://images.fravega.com/f500/028b76a6de3d5f67848cf0a3943d121f.jpg",
    "stock": 1001

}

    response = requests.post(f"http://localhost:8080/api/productos", json=producto)
    data = response.json()

    producto_id = data["id"]

    yield data

    # teardown
    requests.delete(f"http://localhost:8080/api/productos/{producto_id}")
