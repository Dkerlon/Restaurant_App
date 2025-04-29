from flet import *

class Menu(Container):
    def __init__(self,page):
        super().__init__(bgcolor='blue',width=60,height=550,padding=10)
        
        self.page = page
        self.content = Column(
            horizontal_alignment='center',
            controls=[
                Container(
                    content=
                       Row(
                           alignment='spaceBetween',
                           controls=[
                               IconButton(icon=icons.MENU,icon_color='white',on_click=self.animate_menu),
                               IconButton(icon=icons.PERSON,icon_color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.HOME,icon_color='white',on_click= lambda _: self.change_route('/home')),
                               Text('Início',color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.INVENTORY,icon_color='white'),
                               Text('Gerenciar estoque',color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.TABLE_RESTAURANT,icon_color='white',on_click= lambda _: self.change_route('/gerenciar_mesas')),
                               Text('Gerenciar mesas',color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.FACT_CHECK_OUTLINED,icon_color='white'),
                               Text('Relatórios',color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.UPDATE,icon_color='white',on_click=lambda _: self.page.update()),
                               Text('Atualizar',color='white')
                        ]
                    )
                ),
                Container(
                    content=
                       Row(
                           controls=[
                               IconButton(icon=icons.LOGOUT,icon_color='white',on_click= lambda _: self.page.go('/login')),
                               Text('Sair',color='white')
                        ]
                    )
                )
            ]
        )
    def change_route(self,rota):
        self.page.go(rota)
        self.page.update()
    def animate_menu(self,e):
        if self.width <=60:
            self.width = 250
        else:
            self.width = 60
        self.update()
