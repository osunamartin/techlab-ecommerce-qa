import pytest
from playwright.sync_api import sync_playwright
import uuid
import requests
from utils.config import BASE_UI_URL, ADMIN_USER, CLIENT_USER 
from pages.auth_page import AuthPage

#POM
@pytest.fixture
def auth_page(page):
    page.goto(BASE_UI_URL)
    return AuthPage(page)

@pytest.fixture
def login_admin(auth_page):
    auth_page.login(ADMIN_USER["email"], ADMIN_USER["password"])
    return auth_page

@pytest.fixture
def login_cliente(auth_page):
    auth_page.login(CLIENT_USER["email"], CLIENT_USER["password"])
    return auth_page

@pytest.fixture
def login_invalido(auth_page):
    auth_page.login("usuario_invalido@email.com", "wrongpass")
    return auth_page


#Para registro dinámico de usuarios
@pytest.fixture
def test_user():
    unique = uuid.uuid4().hex[:8]

    return {
        "nombre": "Prueba",
        "apellido": "Automation",
        "email": f"qaauto_{unique}@email.com",
        "password": "qa123",
        "telefono": "123456789",
        "direccion": "Fake St 123"
    }

#Crear un producto de prueba para las pruebas E2E, y eliminarlo después (estático)
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
