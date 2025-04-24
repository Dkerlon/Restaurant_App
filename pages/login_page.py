from flet import *
from database.queries import select_login
class Login_page(Container):
    def __init__(self,page):
        super().__init__(height=550,bgcolor='blue',width=350,padding=20,border_radius=8)
        self.page = page
        self.user_textfield = TextField(
            hint_text='Usuário/Email',border_width=0,text_size=16,expand=True,bgcolor='white',border_radius=0,color='black'
        )
        self.password_textfield = TextField(
            hint_text='Senha',border_width=0,text_size=16,expand=True,bgcolor='white',border_radius=0,color='black'
        )
        self.input_container = Container(
                bgcolor='white',
                content=Column(
                spacing=0,
                controls=[
                     self.user_textfield,
                     self.password_textfield
                ]
            )
        )
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    margin=margin.only(bottom=20),
                    content=Image(src='assets/logo_login.png',height=220,width=220)
                ),
                self.input_container,
                Container(height=20),
                TextButton('Entrar',
                    style=ButtonStyle(
                    text_style=TextStyle(size=20),
                    color='white'
                    ),
                    on_click=self.login
                )
            ]
        )
    
    def login(self,e):
        user = select_login(self.user_textfield.value,self.password_textfield.value)

        if not user:
            self.user_textfield.error_text = 'Usuário não encontrado'
            self.input_container.padding = padding.only(bottom=5)
            self.password_textfield.error_text = 'Senha incorreta'
            self.update()
        else:      
            self.page.go('/home')