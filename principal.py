import flet as ft
from flet import icons 
from administracion import administracion
from estadisticas import estadisticas
class UIcuy (ft.Container):
    def __init__ (self, page: ft.Page):
        super(). __init__ (expand = True)
        self.page =page
        self.page.padding = 0
        
        
        
        ###colores a utilizar
        self.color_blue = "#73b1fc"
        self.color_purple = "#bb7efd"
        self.bg_color = "#3f3965"
        self.container_color = "#362e57"
        self.color_navegation_bt = "#2a2949"
        self.color1_card = "#f46fd8"
        self.color2_card = "#64a4ed"
        #####
        self.page.bgcolor = self.bg_color
        #animacion
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)
        
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

        self.container_2  = ft.Container(expand=True,
                          bgcolor= self.container_color,
                          offset= ft.transform.Offset(0,2),
                          animate_offset=self.animation_style,
                          content=ft.Container(
                              padding=20,
                              content=administracion()
                          )            
                          )
        self.container_3 = ft.Container(expand=True,
                          bgcolor= self.container_color,
                          offset= ft.transform.Offset(0,3),
                          animate_offset=self.animation_style,   
                          content=ft.Container(
                              padding = 20, 
                              content= estadisticas() 
                          )           
                          )
        self.container_4 = ft.Container(expand=True,
                          bgcolor= self.container_color,
                          offset= ft.transform.Offset(2,0),
                          animate_offset=self.animation_style              
                          )
        
        self.frame =ft.Container(
            expand = True,
            content = ft.Stack(
                controls = (
                self.container_1,
                self.container_2, 
                self.container_3,
                self.container_4
                )
             )
        ) 
        self.option_1=ft.Container(padding=10,
                                   bgcolor = self.color_purple,
                                   border_radius= 15,
                                   offset = ft.transform.Offset(0,0),
                                   animate_offset=self.animation_style,
                                   on_click=lambda e: self.change_page (e, 1),
                                   height= 40, 
                                   content = ft.Row(
                                       alignment= ft.MainAxisAlignment.CENTER,
                                       controls= [
                                           ft.Icon( ft.icons.DIRECTIONS, color="white"),
                                           ft.Text("Inicio", width = 120)
                                       ]
                                   )
                             )
        self.option_2=ft.Container(padding=10,
                                   bgcolor = self.color_navegation_bt,
                                   border_radius= 15,
                                   offset = ft.transform.Offset(0,0),
                                   animate_offset=self.animation_style,
                                   on_click=lambda e: self.change_page (e, 2),
                                   height= 40, 
                                   content = ft.Row(
                                       alignment= ft.MainAxisAlignment.CENTER,
                                       controls= [
                                           ft.Icon( ft.icons.MONETIZATION_ON_SHARP, color="white"),
                                           ft.Text("Administración", width = 120)
                                       ]
                                   )
                             )
        self.option_3=ft.Container(padding=10,
                                   bgcolor = self.color_navegation_bt,
                                   border_radius= 15,
                                   offset = ft.transform.Offset(0,0),
                                   animate_offset=self.animation_style,
                                   on_click=lambda e: self.change_page (e, 3),
                                   height= 40, 
                                   content = ft.Row(
                                       alignment= ft.MainAxisAlignment.CENTER,
                                       controls= [
                                           ft.Icon( ft.icons.STACKED_LINE_CHART, color="white"),
                                           ft.Text("Estadisticas", width = 120)
                                       ]
                                   )
                             )
        self.option_4=ft.Container(padding=10,
                                   bgcolor = self.color_navegation_bt,
                                   border_radius= 15,
                                   offset = ft.transform.Offset(0,0),
                                   animate_offset=self.animation_style,
                                   on_click=lambda e: self.change_page (e, 4),
                                   height= 40, 
                                   content = ft.Row(
                                       alignment= ft.MainAxisAlignment.CENTER,
                                       controls= [
                                           ft.Icon( ft.icons.SETTINGS_ACCESSIBILITY, color="white"),
                                           ft.Text("Ayuda", width = 120)
                                       ]
                                   )
                             )
        self.navegation = ft.Container(
            padding=20,
            bgcolor= self.container_color,
            animate_size= self.animation_style,
            content= ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_1,
                    self.option_2,
                    self.option_3,
                    self.option_4 
                ]
                
            )
        )
        self.swich_control= {
            1: self.container_1,
            2: self.container_2,
            3: self.container_3,
            4: self.container_4,
        }
        self.page.add(
            ft.Row(
                expand = True,
                spacing = 20,
                controls = [
                    self.navegation, 
                    self.frame,
                ]
            )
            
        ) 
    def change_page(self,e,n):
        for page in self.swich_control:
            self.swich_control[page].offset.y = 2
            self.swich_control[page].update() 
            self.option_1.bgcolor = self.color_navegation_bt
            self.option_2.bgcolor = self.color_navegation_bt
            self.option_3.bgcolor = self.color_navegation_bt
            self.option_4.bgcolor = self.color_navegation_bt
        if n == 1:
            self.option_1.offset.x = 0.15
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
            self.option_1.bgcolor = self.color_purple
            self.option_1.update()
            
        elif n == 2:
            self.option_1.offset.x = 0.
            self.option_2.offset.x = 0.15
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
            self.option_2.bgcolor = self.color_purple
            self.option_2.update()
            
        elif n == 3:
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0.15
            self.option_4.offset.x = 0
            self.option_3.bgcolor = self.color_purple
            self.option_3.update()
            
        elif n == 4:
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0.14
            self.option_4.bgcolor = self.color_purple
            self.option_4.update()
        self.swich_control[n].offset.y = 0
        self.swich_control[n].update() 
        self.page.update()
            


