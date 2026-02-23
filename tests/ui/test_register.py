from conftest import page
from utils.config import BASE_UI_URL


#Registra un nuevo usuario, el fixture test_user genera un email único para evitar conflictos con registros anteriores.
def test_registration(page, test_user):
    page.goto(BASE_UI_URL)
    page.locator("#registroNombre").fill(test_user["nombre"])
    page.locator("#registroApellido").fill(test_user["apellido"])
    page.locator("#registroEmail").fill(test_user["email"])
    page.locator("#registroPassword").fill(test_user["password"])
    page.locator("#registroTelefono").fill(test_user["telefono"])
    page.locator("#registroDireccion").fill(test_user["direccion"])

    page.get_by_role("button", name="Registrarse").click()

    heading = page.locator("h2", has_text="Catálogo de Productos")
    heading.wait_for()
    assert heading.is_visible()
