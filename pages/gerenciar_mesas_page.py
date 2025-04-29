from flet import *
from components.menu import Menu
from database.queries import insert_mesa
from components.gerar_mesas import gerar_mesas

class Gerenciar_mesa(Container):
    def __init__(self, page):
        super().__init__(height=550, bgcolor='blue', width=350, border_radius=8)
        self.page = page
        self.mesas = gerar_mesas('gerenciar_mesa', self.carregar_mesa)
        self.button_add_mesa = IconButton(
            icon=icons.ADD,
            bgcolor='blue',
            icon_color='white',
            style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)),
            on_click=self.adcionar_mesa
        )
        self.container_mesas = Column(
            horizontal_alignment='center',
            scroll='auto',
            controls=[
                self.mesas,
                self.button_add_mesa
            ]
        )
        self.content = Row(
            spacing=0,
            controls=[
                Menu(self.page),
                Container(
                    bgcolor='white',
                    height=550,
                    expand=True,
                    content=self.container_mesas
                )
            ]
        )

    def adcionar_mesa(self, e):
        insert_mesa()
        self.carregar_mesa(e)

    def carregar_mesa(self, e):
        mesas = gerar_mesas('gerenciar_mesa', self.carregar_mesa)
        mesas.controls.append(self.button_add_mesa)
        self.container_mesas = mesas
        self.content.controls[1].content = mesas
        self.update()
