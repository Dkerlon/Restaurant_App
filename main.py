from flet import *
from config.routes import routes

def main(page:Page):
    page.bgcolor = 'black'
    page.title = 'Restaurant App'
    page.window.width = 400
    #page.window.max_width = 400
    page.window.height = 600
    #page.window.max_height = 600
    page.window_resizable = False

    def handle_route(e):
        page.views.clear()
        view = routes(page.route,page)
        page.views.append(view)
        page.update()

    page.on_route_change = handle_route
    page.go('/login')
app(main,assets_dir='assets')