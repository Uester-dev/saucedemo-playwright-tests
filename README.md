# SauceDemo Playwright Tests

Testes automatizados de interface em Python (pytest + Playwright) para o
site de demonstração https://www.saucedemo.com.

## Cenários cobertos
- Login com credenciais válidas
- Login com senha inválida
- Login com usuário bloqueado

## Como rodar
    python -m venv venv
    source venv/Scripts/activate   # Windows (Git Bash)
    pip install -r requirements.txt
    playwright install chromium
    pytest

Para ver o navegador abrindo: `pytest --headed`

## Tecnologias
Python, pytest, Playwright
