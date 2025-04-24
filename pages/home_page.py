from flet import *
from components.menu import Menu
from components.textfield import textfield
class Home(Container):
    def __init__(self,page):
        super().__init__(height=550,bgcolor='blue',width=350,border_radius=8)
        self.page = page
        self.textfield_mesa = textfield('Mesa')
        self.textfield_comanda = textfield('Comanda')
        self.content = Row(
            spacing=0,
            controls=[
                Menu(self.page),
                Container(
                    expand=True,
                    padding=10,
                    bgcolor='white',
                    content=Column(
                        controls=[
                            Row(
                                spacing=3,
                                alignment='start',
                                controls=[
                                    self.textfield_mesa,
                                    self.textfield_comanda,
                                    ElevatedButton(text='Entrar',bgcolor='blue', width=70,height=40,color='white',style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)))
                                ]
                            )
                        ]
                    )
                )
            ]
        )