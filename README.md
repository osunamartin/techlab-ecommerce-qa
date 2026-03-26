# Techlab Ecommerce QA

Este proyecto contiene pruebas automatizadas para una [aplicación web de e‑commerce](https://github.com/nnvelez95/techlab-ecommerce) utilizando **Playwright + Pytest** para pruebas automatizadas de UI y **Python Requests** para pruebas de API.

El objetivo del proyecto es validar funcionalidades críticas del sistema como:

* Autenticación de usuarios
* Gestión de productos
* Flujo de carrito de compras
* Creación y gestión de pedidos
* Validación de permisos entre distintos tipos de usuario
* Correcto funcionamiento de API
---

# Tecnologías utilizadas

* Python
* Pytest
* Playwright
* Requests
* Postman (para exploración inicial de endpoints y pruebas manuales de los mismos)

---

# Pruebas Manuales

* [Link al reporte de pruebas manuales](https://docs.google.com/spreadsheets/d/1JcUxSP62PTEFfykYmUItqD45SBqrw0k08UwF4nQGU1Y/edit?usp=sharing)
* [Link a la colección de endpoints en Postman](https://martin-osuna13-5732072.postman.co/workspace/Mart%C3%ADn-Osuna's-Workspace~08e23817-d598-437d-826a-c593229a2adf/collection/52450225-d53af880-86ab-4456-9e61-b29b435c1c0b?action=share&creator=52627682&active-environment=52450225-fb784d9d-1f54-4464-9f08-48cea307ce1c)

---

# Estructura del proyecto de automatización

```
TECHLAB-ECOMMERCE-QA/

pages/
    admin_page
    auth_page.py
    cart_page.py
    products_page.py
    cart_page.py
    orders_page.py

tests/
    ui/
        test_cart.py
        test_login.py
        test_permisos_usuarios.py
        test_register.py

    api/
        test_cliente_estado_pedido.py
utils/
    __init__.py
    config.py

conftest.py
requirements.txt
pytest.ini
README.md
```
---

# Algunas pruebas implementadas

## 1. UI Automation

Se utilizan **Page Objects** para encapsular la lógica de interacción con la interfaz.

Ejemplo de flujo automatizado:

1. Login de usuario
2. Agregar producto al carrito
3. Crear pedido
4. Validar que el pedido aparece en "Mis pedidos"

Archivo principal:

```
tests/ui/test_e2e_pedido.py
```

---

## 2. API Automation

Se implementan pruebas utilizando **requests** para validar directamente la lógica del backend.

Ejemplo de prueba:

**Cliente no puede cambiar el estado de un pedido (endpoint de admin).**

Flujo del test:

1. Login de cliente
2. Crear pedido
3. Intentar cambiar estado utilizando endpoint admin
4. Validar que la API responde **403 Forbidden**

Archivo:

```
tests/api/test_cliente_estado_pedido.py
```
---

# Instalación

Clonar el repositorio:

```
git clone https://github.com/osunamartin/techlab-ecommerce-qa.git
```

Entrar al proyecto:

```
cd TECHLAB-ECCOMERCE-QA
```

Instalar y ejecutar entorno virtual:
* python3 -m venv .venv
* techlab-ecommerce-qa\venv\Scripts\Activate.ps1

Instalar dependencias:

```
pip install -r requirements.txt
```

Instalar navegadores de Playwright:

```
playwright install
```

---

# Ejecución de pruebas

Ejecutar todos los tests:

```
pytest tests\
```

Ejecutar solo pruebas de UI:

```
pytest tests/ui
```

Ejecutar solo pruebas de API:

```
pytest tests/api
```

Modo visible (headed) ya activado desde pytest.ini 

---

# Algunos fixtures importantes

## test_user

Crea un usuario dinámico mediante API antes del test.

Utiliza un email único con UUID para evitar conflictos entre ejecuciones.

---

## producto_test

Crea un producto de prueba para las pruebas E2E y lo elimina al final de la prueba para limpiar la base de datos.

---

## login_admin

Loguea al usuario admin usando sus credenciales antes de los tests correspondientes.

---

# Buenas prácticas aplicadas

* Uso de **Page Object Model** para separar lógica de UI
* Uso de **fixtures reutilizables**
* Tests independientes
* Datos dinámicos para evitar colisiones
* Separación entre **UI tests** y **API tests**

---

# Posibles mejoras futuras

* Integración con CI/CD (GitHub Actions)
* Reportes de pruebas (Allure / HTML reports)
* Mayor cobertura de API tests
* Pruebas de performance básicas

---

# Autor

Proyecto creado por Martin Osuna como práctica de **QA Automation** utilizando Python y Playwright.
