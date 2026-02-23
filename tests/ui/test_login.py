import re
from playwright.sync_api import Playwright, sync_playwright, expect
from utils.config import BASE_UI_URL, ADMIN_USER

def test_admin_login(page):
    page.goto(BASE_UI_URL)

    page.locator("#loginEmail").fill(ADMIN_USER["email"])
    page.locator("#loginPassword").fill(ADMIN_USER["password"])
    page.get_by_role("button", name="Iniciar Sesión").click()

    page.wait_for_selector("h2", has_text="Catálogo de Productos") #arreglar esto
    assert page.locator("h2", has_text="Catálogo de Productos").is_visible()
