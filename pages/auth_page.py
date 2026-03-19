from utils.config import BASE_UI_URL

class AuthPage:

    def __init__(self, page):
        self.page = page

        # Iniciar sesión / Login
        self.login_email = page.locator("#loginEmail")
        self.login_password = page.locator("#loginPassword")
        self.login_button = page.get_by_role("button", name="Iniciar Sesión")

        # Registro de usuario
        self.nombre = page.locator("#registroNombre")
        self.apellido = page.locator("#registroApellido")
        self.email = page.locator("#registroEmail")
        self.password = page.locator("#registroPassword")
        self.telefono = page.locator("#registroTelefono")
        self.direccion = page.locator("#registroDireccion")

        self.register_button = page.get_by_role("button", name="Registrarse")
    
    #Abre la página de inicio de sesión/registro
    def abrir(self):
        
        self.page.goto(f"{BASE_UI_URL}")
        
    #Método para iniciar sesión
    def login(self, email, password):

        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        
    #Método para registrar un usuario
    def registrar_usuario(self, user):

        self.nombre.fill(user["nombre"])
        self.apellido.fill(user["apellido"])
        self.email.fill(user["email"])
        self.password.fill(user["password"])
        self.telefono.fill(user["telefono"])
        self.direccion.fill(user["direccion"])

        self.register_button.click()
