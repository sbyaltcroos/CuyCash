import flet as ft
import httpx

class inicio(ft.Container):
    def __init__(self, on_login_success):
        super().__init__(expand=True)
        self.on_login_success = on_login_success

        self.bgcolor = "#3f3965"
        self.xcolor = "#000000"

        self.color1 = ft.colors.PURPLE_700
        self.color2 = ft.colors.PURPLE_400
        self.color_text = self.xcolor

        self.username = ft.TextField(
            label="Usuario", width=300,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )
        self.password = ft.TextField(
            label="Contraseña", width=300, password=True, can_reveal_password=True,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )

        login_btn = ft.ElevatedButton(
            text="Iniciar Sesión", width=300,
            bgcolor=self.color1, color=self.color_text,
            on_click=self.on_login
        )

        linea_gradiante = ft.Container(
            height=3, width=300, border_radius=20,
            gradient=ft.SweepGradient(
                center=ft.alignment.center,
                colors=[
                    ft.colors.RED, ft.colors.ORANGE, ft.colors.YELLOW, ft.colors.GREEN,
                    ft.colors.CYAN, ft.colors.BLUE, ft.colors.PURPLE, ft.colors.RED,
                ]
            )
        )

        crear_usuario_btn = ft.Container(
            content=ft.TextButton(
                text="Crear usuario",
                on_click=lambda _: self.mostrar_crear_usuario(),
                style=ft.ButtonStyle(color=self.color_text),
            ),
            width=300,
            padding=ft.padding.all(2),
            border_radius=10,
            gradient=linea_gradiante.gradient,
        )

        self.login_ui = ft.Container(
            bgcolor=self.bgcolor,
            content=ft.Column(
                controls=[
                    ft.Text("Bienvenido", size=32, weight="bold", color=self.color_text),
                    ft.Text("Por favor, ingresa tus datos", size=16, color=self.color_text),
                    self.username,
                    self.password,
                    login_btn,
                    ft.Text("o", color=self.color_text, size=20),
                    linea_gradiante,
                    crear_usuario_btn,
                ],
                alignment="center",
                spacing=20,
                horizontal_alignment="center"
            ),
            expand=True,
            alignment=ft.alignment.center
        )

        self.crear_usuario_ui = self.vista_crear_usuario()

        self.content = self.login_ui  

    def on_login(self, e):
        def mostrar_alerta(mensaje, color):
            dialogo = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text(mensaje),
                actions=[ft.TextButton("Cerrar", on_click=lambda _: self.page.close(dialogo))],
                actions_alignment="end",
                bgcolor=color
            )
            self.page.open(dialogo)
            self.page.update()

        usuario = self.username.value.strip()
        contraseña = self.password.value.strip()

        # Validaciones locales
        if not usuario or not contraseña:
            mostrar_alerta("Todos los campos son obligatorios", ft.colors.RED_400)
            return

        data = {
            "usuario": usuario,
            "contraseña": contraseña
        }

        try:
            response = httpx.post("http://localhost:8000/login", json=data)
            if response.status_code == 200:
                self.on_login_success()
            else:
                try:
                    error_detail = response.json().get("detail", "Error desconocido")
                except Exception:
                    error_detail = response.text or "Respuesta no válida del servidor"
                mostrar_alerta(f"Error: {error_detail}", ft.colors.RED_400)
        except Exception as ex:
            mostrar_alerta(f"Error al conectar con el backend: {ex}", ft.colors.RED_400)



    def mostrar_crear_usuario(self):
        self.content = self.crear_usuario_ui
        self.update()

    def volver_al_login(self, e=None):
        self.content = self.login_ui
        self.update()

    def guardar_usuario(self, e):
        def mostrar_alerta(mensaje, color):
            dialogo = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text(mensaje),
                actions=[ft.TextButton("Cerrar", on_click=lambda _: self.page.close(dialogo))],
                actions_alignment="end",
                bgcolor=color
            )
            self.page.open(dialogo)
            self.page.update()

        # Obtener valores
        correo = self.email.value.strip()
        usuario = self.new_username.value.strip()
        contraseña = self.new_password.value.strip()
        finca = self.finca_name.value.strip()

        # Validaciones locales
        if not all([correo, usuario, contraseña, finca]):
            mostrar_alerta("Todos los campos son obligatorios", ft.colors.RED_400)
            return

        if "@" not in correo or "." not in correo:
            mostrar_alerta("Correo electrónico inválido", ft.colors.RED_400)
            return

        if len(contraseña) <= 6:
            mostrar_alerta("La contraseña debe tener más de 6 caracteres", ft.colors.RED_400)
            return

        # Preparar datos
        data = {
            "correo": correo,
            "usuario": usuario,
            "contraseña": contraseña,
            "finca": finca
        }

        # Enviar al backend
        try:
            response = httpx.post("http://localhost:8000/registro", json=data)
            if response.status_code == 200:
                mostrar_alerta("Usuario creado con éxito", ft.colors.GREEN_400)
                self.volver_al_login()
            else:
                try:
                    error_detail = response.json().get("detail", "Error desconocido")
                except Exception:
                    error_detail = response.text or "Respuesta no válida del servidor"
                mostrar_alerta(f"Error: {error_detail}", ft.colors.RED_400)
        except Exception as ex:
            mostrar_alerta(f"Error al conectar con el backend: {ex}", ft.colors.RED_400)



    def vista_crear_usuario(self):
        self.email = ft.TextField(
            label="Correo electrónico", width=300,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )
        self.new_username = ft.TextField(
            label="Nombre de usuario", width=300,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )
        self.new_password = ft.TextField(
            label="Contraseña", width=300, password=True, can_reveal_password=True,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )
        self.finca_name = ft.TextField(
            label="Nombre de la finca", width=300,
            text_style=ft.TextStyle(color=self.color_text),
            border_color=self.color2, focused_border_color=self.color1, cursor_color=self.color1
        )

        guardar_btn = ft.ElevatedButton(
            text="Guardar", width=300,
            bgcolor=self.color1, color=self.color_text,
            on_click=self.guardar_usuario
        )

        volver_btn = ft.TextButton(
            text="Volver", on_click=self.volver_al_login,
            style=ft.ButtonStyle(color=self.color_text)
        )

        return ft.Container(
            bgcolor=self.bgcolor,
            content=ft.Column(
                controls=[
                    ft.Text("Crear nuevo usuario", size=28, weight="bold", color=self.color_text),
                    self.email,
                    self.new_username,
                    self.new_password,
                    self.finca_name,
                    guardar_btn,
                    volver_btn
                ],
                alignment="center",
                spacing=20,
                horizontal_alignment="center"
            ),
            expand=True,
            alignment=ft.alignment.center
        )
