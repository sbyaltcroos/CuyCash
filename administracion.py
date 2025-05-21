import flet as ft

class administracion(ft.Container):
    def __init__(self):
        super().__init__(expand=True)

        color1_card = ft.colors.BLUE_800
        color2_card = ft.colors.BLUE_900
        color_purple = ft.colors.PURPLE_700
        color_texto = ft.colors.WHITE

        grad_card = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[color1_card, color_purple, color2_card]
        )

        vendidos_table = ft.Container(
            gradient=grad_card,
            border_radius=10,
            padding=10,
            content=ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Fecha", color=color_texto)),
                    ft.DataColumn(ft.Text("Cantidad", color=color_texto)),
                    ft.DataColumn(ft.Text("Comprador", color=color_texto)),
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-01", color=color_texto)),
                        ft.DataCell(ft.Text("12", color=color_texto)),
                        ft.DataCell(ft.Text("Mercado Pasto", color=color_texto)),
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-10", color=color_texto)),
                        ft.DataCell(ft.Text("8", color=color_texto)),
                        ft.DataCell(ft.Text("Juan Pérez", color=color_texto)),
                    ]),
                ]
            )
        )

        muertos_table = ft.Container(
            gradient=grad_card,
            border_radius=10,
            padding=10,
            content=ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Fecha", color=color_texto)),
                    ft.DataColumn(ft.Text("Cantidad", color=color_texto)),
                    ft.DataColumn(ft.Text("Causa", color=color_texto)),
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-03", color=color_texto)),
                        ft.DataCell(ft.Text("2", color=color_texto)),
                        ft.DataCell(ft.Text("Enfermedad respiratoria", color=color_texto)),
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-14", color=color_texto)),
                        ft.DataCell(ft.Text("1", color=color_texto)),
                        ft.DataCell(ft.Text("Ataque de perro", color=color_texto)),
                    ]),
                ]
            )
        )

        comida_table = ft.Container(
            gradient=grad_card,
            border_radius=10,
            padding=10,
            content=ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Fecha", color=color_texto)),
                    ft.DataColumn(ft.Text("Tipo de comida", color=color_texto)),
                    ft.DataColumn(ft.Text("inversión ($cop)", color=color_texto)),
                    ft.DataColumn(ft.Text("Cantidad (kg)", color=color_texto)),
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-01", color=color_texto)),
                        ft.DataCell(ft.Text("Concentrado", color=color_texto)),
                        ft.DataCell(ft.Text("50000", color=color_texto)),
                        ft.DataCell(ft.Text("50", color=color_texto)),
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("2025-05-05", color=color_texto)),
                        ft.DataCell(ft.Text("Concentrado", color=color_texto)),
                        ft.DataCell(ft.Text("20000", color=color_texto)),
                        ft.DataCell(ft.Text("20", color=color_texto)),
                    ]),
                ]
            )
        )

        registro_panel = ft.Container(
            width=400,
            padding=20,
            border_radius=10,
            bgcolor="#4b3c77",
            content=ft.Column([
                ft.Text("Registrar actividad", size=22, weight="bold", color=color_texto),
                ft.TextField(label="Fecha", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.Text("Vender lote de cuyes", color=color_texto),
                ft.TextField(label="Cantidad vendida", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.TextField(label="Comprador", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.Divider(),
                ft.Text("Reportar muerte", color=color_texto),
                ft.TextField(label="Cantidad muerta", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.TextField(label="Causa de muerte", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.Divider(),
                ft.Text("Adjuntar comida", color=color_texto),
                ft.TextField(label="Tipo de comida", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.TextField(label="Inversión ($cop)", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.TextField(label="Cantidad (kg)", border_color=color_purple, label_style=ft.TextStyle(color=color_texto), color=color_texto),
                ft.ElevatedButton("Guardar registro", bgcolor=color_purple, color=color_texto),
            ])
        )

        self.bgcolor = "#362e57"
        self.padding = 20
       
        self.bgcolor = "#362e57"
        self.padding = 20
        self.content = ft.Column(
                    controls=[
                        ft.Text("Administración de los Cuyes", size=30, weight="bold", color=color_texto, text_align="center"),
                        ft.Row([
                            ft.Column([
                                ft.Text("Cuyes Vendidos", size=22, color=color_texto),
                                vendidos_table,
                                ft.Text("Cuyes Muertos", size=22, color=color_texto),
                                muertos_table,
                                ft.Text("Comida Consumida", size=22, color=color_texto),
                                comida_table,
                            ], expand=True),
                            registro_panel
                        ])
                    ],
                    scroll=ft.ScrollMode.AUTO  
                )
