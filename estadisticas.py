import flet as ft


def main(page: ft.Page):
    page.title = "Estadísticas Visuales"
    page.bgcolor = "#362e57"
    page.padding = 20

    color1 = ft.colors.PURPLE_700
    color2 = ft.colors.PURPLE_400
    color3 = ft.colors.BLUE_600
    color4 = ft.colors.BLUE_300
    color_text = ft.colors.WHITE

  
    ganancias = 120_000
    perdidas_cuyes = 35_000
    inversion_comida = 75_000


    max_valor = max(ganancias, perdidas_cuyes, inversion_comida)
    escala = 200 / max_valor  

    def barra(valor, etiqueta, color_inicio, color_fin, margin_top=0):
        altura = valor * escala
        return ft.Column(
            controls=[
                ft.Text(f"${valor:,}", size=16, color=color_text),
                ft.Container(
                    width=60,
                    height=altura,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[color_inicio, color_fin],
                    ),
                    border_radius=10,
                    margin=ft.margin.only(top=margin_top),
                ),
                ft.Text(etiqueta, size=18, color=color_text),
            ],
            alignment="center",
            spacing=5,
        )

    barras = ft.Row(
        controls=[
            barra(ganancias, "Ganancias", color1, color2),
            barra(perdidas_cuyes, "Pérdidas", color3, color4, margin_top=40), 
            barra(inversion_comida, "Inversión Comida", color1, color4, margin_top=80), 
        ],
        alignment="spaceAround",
        expand=True,
        vertical_alignment="end",  
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Estadísticas Económicas", size=30, weight="bold", color=color_text),
                barras,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=30,
            expand=True,
        )
    )


ft.app(target=main)
