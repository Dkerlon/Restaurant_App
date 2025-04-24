from flet import *
from pages.login_page import Login_page
from pages.home_page import Home
from pages.gerenciar_mesas_page import Gerenciar_mesa
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
        )
    }
    return view[route]