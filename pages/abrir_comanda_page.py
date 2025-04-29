from flet import *
from components.menu import Menu
from database.queries import insert_comanda,save_comanda
from components.comandas import comandas
from components.categorias_produto import categorias_produto
class Abrir_comanda(Container):
    def __init__(self,page):
        super().__init__(height=550,bgcolor='blue',width=350,border_radius=8)
        self.page = page
        self.categorias_produto = Column()
        self.produtos = Column()
        self.produtos_page = Container(
            expand=True,
            width=290,
            height=550,
            padding=10,
            bgcolor='white',
            visible=False,
            content=Column(
                controls=[
                    self.categorias_produto,
                    self.produtos
                ]
            )
        )
        self.comandas = comandas(self.produtos_page_visible)
        self.content = Row(
            spacing=0,
            controls=[
                Menu(self.page),
                Stack(
                    controls=[
                        Container(
                            expand=True,
                            padding=10,
                            bgcolor='white',
                            content=Column(
                                horizontal_alignment='center',
                                controls=[
                                    Row(
                                        spacing=3,
                                        controls=[
                                            ElevatedButton(
                                                text='Abrir nova comanda',
                                                bgcolor='blue', 
                                                width=180,
                                                height=40,
                                                color='white',
                                                style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)),
                                                on_click=self.nova_comanda),
                                            ElevatedButton(text='Imprimir',bgcolor='blue', width=90,height=40,color='white',style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)))
                                        ]
                                    ),
                                    self.comandas
                                    #Comandas
                                ]
                            )
                        ),
                        self.produtos_page
                    ]
                )
            ]
        )
    def nova_comanda(self,e):
        insert_comanda()
        self.content.controls[1].controls[0].content.controls[1] = comandas()
        self.update()
    def produtos_page_visible(self,id):
        produtos_page_container = self.content.controls[1].controls[1]
        self.categorias_produto = categorias_produto()
        produtos_page_container.content.controls[0] = self.categorias_produto
        produtos_page_container.visible = True
        save_comanda(id)
        self.update()