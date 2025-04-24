from flet import *
from components.menu import Menu
class Gerenciar_mesa(Container):
    def __init__(self,page):
        super().__init__(height=550,bgcolor='blue',width=350,border_radius=8)
        self.page = page
        self.content = Row(
            spacing=0,
            controls=[
                Menu(self.page),
                Container(bgcolor='white',expand=True,padding=10)
            ]
        )
        
        