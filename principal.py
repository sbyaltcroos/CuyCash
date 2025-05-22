import flet as ft
from flet import icons
from administracion import administracion
from estadisticas import estadisticas
from granja import Granja

class UIcuy(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0

        # Colores
        self.color_blue = "#73b1fc"
        self.color_purple = "#bb7efd"
        self.bg_color = "#3f3965"
        self.container_color = "#362e57"
        self.color_navegation_bt = "#2a2949"
        self.color1_card = "#f46fd8"
        self.color2_card = "#64a4ed"

        self.page.bgcolor = self.bg_color
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)

        # Contenedores de páginas
        self.container_1  = ft.Container(expand=True,
                          bgcolor= self.container_color,
                          offset= ft.transform.Offset(0,0),
                          animate_offset=self.animation_style, 
                          margin=15,
                          content= ft.Row(
                              controls = [
                                  ft.Container(
                                      expand = True,
                                      content=ft.Stack(
                                          alignment= ft.alignment.top_center,
                                          controls =[
                                          ft.Container(expand=True,
                                          bgcolor=self.container_color,
                                          margin= ft.margin.only(left = 0, top = 150, right = 0, bottom = 0),
                                          padding= ft.padding.only(left= 0, top=100, right=0, bottom=0),
                                          border_radius= 20,
                                          content= ft.Column(
                                              horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                              controls=[
                                                  ft.Text("Vender", color= "white", size=20, weight= "bold"),
                                                  ft.Tabs(
                                                      tab_alignment= ft.TabAlignment.CENTER,
                                                      indicator_color= self.color_purple,
                                                      label_color= "white",
                                                      indicator_tab_size= True,
                                                      expand=True,
                                                      tabs=[
                                                          ft.Tab("pedidos",
                                                             content= ft.Container(
                                                                 padding=20,
                                                                 content=ft.Column(
                                                                     spacing=10,
                                                                     controls=[
                                                                         ft.Text("Confirmar venta",color="white", size=15 ),
                                                                         ft.TextField(
                                                                             expand= True,
                                                                             hint_text= ("Granja texel"),
                                                                             hint_style =ft.TextStyle (color= ft.colors.WHITE),
                                                                             border_color="transparent", 
                                                                             border_radius=10,
                                                                             bgcolor=self.bg_color,
                                                                         ),
                                                                         ft.Row(
                                                                             controls=[
                                                                                 ft.Column(expand=True,
                                                                                   controls=[
                                                                                    ft.Text("Cantidad",color="white", size=15),
                                                                                    ft.TextField (hint_text="20 cuyes",
                                                                                                  border_color= "transparent",
                                                                                                  bgcolor= self.bg_color,
                                                                                                  border_radius= 10,
                                                                                                  hint_style=ft.TextStyle(color=ft.colors.WHITE)
                                                                                    ) 
                                                                                    
                                                                                   ]     
                                                                                 ),
                                                                                ft.Column(expand=True,
                                                                                    controls=[
                                                                                    ft.Text("Cliente",color="white", size=15),
                                                                                    ft.TextField (hint_text="Restaurante del sur",
                                                                                                  border_color= "transparent",
                                                                                                  bgcolor= self.bg_color,
                                                                                                  border_radius= 10,
                                                                                                  hint_style=ft.TextStyle(color=ft.colors.WHITE)
                                                                                    ) 
                                                                                    
                                                                                   ]     
                                                                                    
                                                                                 )
                                                                             ]
                                                                         ),
                                                                         ft.Row(expand = True,
                                                                            controls=[
                                                                                 ft.Text("Ganancia: $ 20000",color="white", size=15),
                                                                                 ft.Text("Valor de venta total: $ 100000",color="white", size=15),
                                                                            ]
                                                                             ),
                                                                         ft.Column(
                                                                             controls=[
                                                                                 ft.Container(height= 50,
                                                                                              border_radius=20,
                                                                                              gradient= ft.LinearGradient(
                                                                                                  colors = [
                                                                                                      self.color1_card,
                                                                                                      self.color_purple,
                                                                                                      self.color2_card
                                                                                                  ]
                                                                                              ),
                                                                                              content= ft.Row(
                                                                                                  alignment=ft.MainAxisAlignment.CENTER,
                                                                                                  controls=[
                                                                                                      ft.Icon(ft.Icons.SEND, color= "WHITE")
                                                                                                  ]
                                                                                              )
                                                                                              )
                                                                             ]
                                                                         )
                                                                     ]
                                                                 )
                                                             ) 
                                                          ),
                                                      ft.Tab("enlistar",
                                                          
                                                      )
                                                      ]
                                                  )
                                              ]
                                          )
                                          ),
                                          ft.Container(height=180, width=300,
                                            gradient=ft.LinearGradient(
                                                rotation = 0.5,
                                                colors = [
                                                    self.color1_card,
                                                    self.color2_card,
                                                    self.color_purple
                                                ]
                                            ),   
                                            margin= ft.margin.only(left= 50, top=50, right=50, bottom=0),
                                            border_radius= 20,
                                            padding = 10,
                                            content= ft.Column(
                                                controls=[
                                                    ft.Text("CuyCash",color = "white",size=16),
                                                    ft.Text("tienes 68 cuyes que estan a punto de cumplir su ciclo", color= "white", size=20, weight="bold") #informacion general////////////////////////////////
                                                ]
                                            )
                                                       )
                                          ]
                                      )
                                  ),
                            
                              ]
                          )       
                          )
        self.container_2 = ft.Container(expand=True, bgcolor=self.container_color, content=ft.Container(padding=20, content=administracion()))
        self.container_3 = ft.Container(expand=True, bgcolor=self.container_color, content=ft.Container(padding=20, content=estadisticas()))
        self.container_4 = ft.Container(expand=True, bgcolor=self.container_color)
        self.container_5 = ft.Container(expand=True, bgcolor=self.container_color, content=ft.Container(padding=20, content=Granja()))

        self.frame = ft.Container(
            expand=True,
            content=ft.Stack(
                controls=[
                    self.container_1,
                    self.container_2,
                    self.container_3,
                    self.container_4,
                    self.container_5
                ]
            )
        )

        # Botones de navegación
        self.option_1 = self.create_nav_option("Inicio", icons.DIRECTIONS, lambda e: self.change_page(e, 1), True)
        self.option_2 = self.create_nav_option("Administración", icons.MONETIZATION_ON_SHARP, lambda e: self.change_page(e, 2))
        self.option_3 = self.create_nav_option("Estadísticas", icons.STACKED_LINE_CHART, lambda e: self.change_page(e, 3))
        self.option_4 = self.create_nav_option("Ayuda", icons.SETTINGS_ACCESSIBILITY, lambda e: self.change_page(e, 4))
        self.option_5 = self.create_nav_option("Granja", icons.AGRICULTURE, lambda e: self.change_page(e, 5))

        self.navegation = ft.Container(
            padding=20,
            bgcolor=self.container_color,
            animate_size=self.animation_style,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_1,
                    self.option_2,
                    self.option_3,
                    self.option_4,
                    self.option_5
                ]
            )
        )

        self.swich_control = {
            1: self.container_1,
            2: self.container_2,
            3: self.container_3,
            4: self.container_4,
            5: self.container_5
        }

        self.page.add(
            ft.Row(
                expand=True,
                spacing=20,
                controls=[
                    self.navegation,
                    self.frame
                ]
            )
        )

    def create_nav_option(self, label, icon, on_click, selected=False):
        return ft.Container(
            padding=10,
            bgcolor=self.color_purple if selected else self.color_navegation_bt,
            border_radius=15,
            offset=ft.transform.Offset(0.15 if selected else 0, 0),
            animate_offset=self.animation_style,
            on_click=on_click,
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(icon, color="white"),
                    ft.Text(label, width=120, color="white")
                ]
            )
        )

    def change_page(self, e, n):
        for i in self.swich_control:
            self.swich_control[i].offset = ft.transform.Offset(0, 2)
            self.swich_control[i].update()

        for opt in [self.option_1, self.option_2, self.option_3, self.option_4, self.option_5]:
            opt.bgcolor = self.color_navegation_bt
            opt.offset = ft.transform.Offset(0, 0)
            opt.update()

        getattr(self, f"option_{n}").bgcolor = self.color_purple
        getattr(self, f"option_{n}").offset = ft.transform.Offset(0.15, 0)
        getattr(self, f"option_{n}").update()

        self.swich_control[n].offset = ft.transform.Offset(0, 0)
        self.swich_control[n].update()
        self.page.update()

