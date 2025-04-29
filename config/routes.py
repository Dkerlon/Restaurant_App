from flet import *
from pages.login_page import Login_page
from pages.home_page import Home
from pages.gerenciar_mesas_page import Gerenciar_mesa
from pages.abrir_comanda_page import Abrir_comanda
def routes(route,page):

    view = {
        '/home':View(
            '/home',[
                Home(page)
            ]
        ),
        '/login':View(
            '/login',[
                Login_page(page)
            ],
        ),
        '/gerenciar_mesas':View(
            '/gerenciar_mesas',[
                Gerenciar_mesa(page)
            ],
        ),
        '/abrir_comanda':View(
            '/abrir_comanda',[
                Abrir_comanda(page)
            ]
        )
    }
    return view[route]