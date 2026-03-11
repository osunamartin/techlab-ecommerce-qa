import pytest
from playwright.sync_api import sync_playwright
import uuid
import requests
from utils.config import BASE_UI_URL #Para acceso a API

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

#Fixture para login como ADMIN
@pytest.fixture
def login_admin(page):
    page.goto(f"{BASE_UI_URL}")
    page.fill("#loginEmail", "admin@techlab.com")
    page.fill("#loginPassword", "admin123")
    page.get_by_role("button", name="Iniciar Sesión").click()
    yield page

#Fixture para login como CLIENTE
@pytest.fixture
def login_cliente(page):
    page.goto(f"{BASE_UI_URL}")
    page.fill("#loginEmail", "juan.perez@email.com")
    page.fill("#loginPassword", "cliente123")
    page.get_by_role("button", name="Iniciar Sesión").click()
    yield page

#Fixture para login inválido, para testing negativo.
@pytest.fixture
def login_invalido(page):
    page.goto(f"{BASE_UI_URL}")
    page.fill("#loginEmail", "usuarioinexistente@email.com")    
    page.fill("#loginPassword", "contraseñainvalida")
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

    response = requests.post(f"{BASE_UI_URL}/api/productos", json=producto)
    data = response.json()

    producto_id = data["id"]

    yield data

    # teardown
    requests.delete(f"{BASE_UI_URL}/api/productos/{producto_id}")

#Crea productos dinámicos para pruebas E2E de pedido, sin eliminarlo después, para evitar conflicto con los pedidos
@pytest.fixture
def producto_test_automation():

    nombre_producto = f"QA-AUTO-{uuid.uuid4().hex[:6]}"

    producto = {
        "nombre": nombre_producto,
        "precio": 4000,
        "descripcion": "Prueba E2E de pedido",
        "categoria": "Auriculares",
        "imagen": "https://images.fravega.com/f500/028b76a6de3d5f67848cf0a3943d121f.jpg",
        "stock": 1001
    }

    response = requests.post(f"{BASE_UI_URL}/api/productos", json=producto)
    

    return response.json()
