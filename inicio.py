import flet as ft


def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.bgcolor = "#362e57"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window_width = 400
    page.window_height = 400

    color1 = ft.colors.PURPLE_700
    color2 = ft.colors.PURPLE_400
    color3 = ft.colors.BLUE_600
    color4 = ft.colors.BLUE_300
    color_text = ft.colors.WHITE

    def on_login(e):
        # Aquí puedes agregar lógica de autenticación
        page.dialog = ft.AlertDialog(
            title=ft.Text("Intento de Login"),
            content=ft.Text(f"Usuario: {username.value}\nContraseña: {password.value}"),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())],
        )
        page.dialog.open = True
        page.update()

    username = ft.TextField(
        label="Usuario",
        border_color=color2,
        focused_border_color=color1,
        cursor_color=color1,
        text_style=ft.TextStyle(color=color_text),
        width=300,
        autofocus=True,
    )
    password = ft.TextField(
        label="Contraseña",
        border_color=color2,
        focused_border_color=color1,
        cursor_color=color1,
        text_style=ft.TextStyle(color=color_text),
        password=True,
        can_reveal_password=True,
        width=300,
    )

    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        bgcolor=color1,
        color=color_text,
        width=300,
        on_click=on_login,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Bienvenido", size=32, weight="bold", color=color_text),
                ft.Text("Por favor, ingresa tus datos para continuar", size=16, color=color_text),
                username,
                password,
                login_button,
            ],
            alignment="center",
            spacing=20,
            horizontal_alignment="center",
        )
    )


ft.app(target=main)
