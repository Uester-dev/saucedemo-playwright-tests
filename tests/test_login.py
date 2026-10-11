import re
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


def fazer_login(page: Page, usuario: str, senha: str):
    page.goto(URL)
    page.fill("[data-test='username']", usuario)
    page.fill("[data-test='password']", senha)
    page.click("[data-test='login-button']")


def test_login_valido(page: Page):
    fazer_login(page, "standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(r".*/inventory.html"))
    expect(page.locator("[data-test='title']")).to_have_text("Products")


def test_login_com_senha_invalida(page: Page):
    fazer_login(page, "standard_user", "senha_errada")
    erro = page.locator("[data-test='error']")
    expect(erro).to_be_visible()
    expect(erro).to_contain_text("do not match")


def test_usuario_bloqueado(page: Page):
    fazer_login(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")
