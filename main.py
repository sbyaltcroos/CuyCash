import flet as ft
from inicio import inicio
from principal import UIcuy

def main(page: ft.Page):
    page.title = "Sistema de Cuyes"
    page.theme_mode = ft.ThemeMode.DARK

    def on_login_success():
        page.clean()
        UIcuy(page)  

    # Mostrar vista de inicio de sesión
    page.add(inicio(on_login_success))

ft.app(target=main)
