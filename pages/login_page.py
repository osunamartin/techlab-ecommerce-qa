class LoginPage:

    def __init__(self, page):
        self.page = page
        #locators
        self.email_input = page.locator("#loginEmail")
        self.password_input = page.locator("#loginPassword")
        self.login_button = page.get_by_role("button", name="Iniciar Sesión")
    
    #Método para iniciar sesión
    def login(self, email, password):
        
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()