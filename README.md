## 🎯 Objetivo

Este repositorio contiene pruebas automatizadas para una [aplicación web de e-commerce](https://github.com/nnvelez95/techlab-ecommerce), incluyendo:

* ✅ UI Testing (Playwright)
* ✅ API Testing (requests)
* ✅ E2E Tests (UI)
* ✅ Validación de permisos de usuario

El objetivo es validar funcionalidades críticas del sistema de forma reproducible y escalable.

Entre ellas:

* Autenticación de usuarios
* Gestión de productos
* Flujo de carrito de compras
* Creación y gestión de pedidos
* Validación de permisos entre distintos tipos de usuario
* Correcto funcionamiento de la API

---
## 📝 Documentación de Pruebas Manuales
* [Reporte de pruebas manuales](https://docs.google.com/spreadsheets/d/1JcUxSP62PTEFfykYmUItqD45SBqrw0k08UwF4nQGU1Y/edit?usp=sharing)
* [Colección de endpoints en Postman](https://martin-osuna13-5732072.postman.co/workspace/Mart%C3%ADn-Osuna's-Workspace~08e23817-d598-437d-826a-c593229a2adf/collection/52450225-d53af880-86ab-4456-9e61-b29b435c1c0b?action=share&creator=52450225&active-environment=52450225-fb784d9d-1f54-4464-9f08-48cea307ce1c)

---
## 🧰 Tecnologías
* Python
* Pytest
* Playwright (Python)
* Requests
* Postman (para exploración inicial y pruebas manuales)
---

## ⚙️ Requisitos previos

Tener levantada [la aplicación de e-commerce](https://github.com/nnvelez95/techlab-ecommerce):

* Frontend: (según entorno)
* Backend/API: (según entorno)

---

## 🐍 Setup del entorno (Windows)
Crear y activar el entorno virtual:
* python -m venv venv
* .\venv\Scripts\activate

Instalar dependencias:
* pip install -r requirements.txt

Instalar navegadores de Playwright:
* playwright install
---
## ▶️ Ejecutar tests

Correr todos los tests:

* pytest tests\

Correr solo UI:

* pytest tests/ui

Correr solo API:

* pytest tests/api
Modo visible (headed) configurado desde pytest.ini.

---
## 🧪 Estrategia de testing

El proyecto combina pruebas de UI y API para validar tanto la experiencia del usuario como la lógica del backend.

UI Automation:

* Se utiliza el patrón Page Object Model (POM) para encapsular la lógica de interacción con la interfaz.

Flujo E2E implementado:

* Login de usuario
* Agregar producto al carrito
* Crear pedido
* Validar que el pedido aparece en "Mis pedidos"

Archivo principal:

* tests/ui/test_e2e_pedido.py

API Automation

* Se utilizan pruebas con requests para validar directamente endpoints del backend.

Ejemplo de caso:

* Cliente intenta modificar el estado de un pedido usando un endpoint de admin.

Flujo:

* Login de cliente
* Crear pedido
* Intentar modificar estado
* Validar respuesta 403 Forbidden

Archivo:

* tests/api/test_cliente_estado_pedido.py

## 🧩 Fixtures importantes

test_user:

* Crea un usuario dinámico mediante API usando un email único (UUID).
* Permite evitar conflictos entre ejecuciones.

producto_test:

* Crea un producto de prueba para escenarios E2E y lo elimina al finalizar.

login_admin:

* Autentica un usuario administrador antes de ejecutar tests que lo requieren.

## 🧼 Buenas prácticas usadas
* Uso de Page Object Model (POM)
* Fixtures reutilizables
* Tests independientes
* Datos dinámicos para evitar colisiones
* Separación entre UI tests y API tests

## 🚀 Posibles mejoras futuras
* Integración con CI/CD (GitHub Actions)
* Reportes de pruebas (Allure / HTML reports)
* Mayor cobertura de API
* Pruebas de performance básicas

## 👨‍💻 Autor

Proyecto creado por Martin Osuna como práctica de QA Automation utilizando Python, Playwright y testing de APIs.
