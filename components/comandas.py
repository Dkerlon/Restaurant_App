from flet import *
from database.queries import select_comanda
def comandas(produtos_page_visible):
    comandas = select_comanda()
    comadas_container = Column(
        controls=[

        ]
    )

    contador = 1
    for c in comandas:
        comadas_container.controls.append(
            Container(
                width=250,
                content=Row(
                height=40,
                expand=True,
                alignment='spaceBetween',
                controls=[
                    Text(f'COMANDA:{c[0]}({contador})',color='black',size=10,weight=FontWeight.BOLD),
                    Row(
                        controls=[
                            ElevatedButton(text='Imprimir',bgcolor='blue', width=75,height=40,color='white',style=ButtonStyle(shape=RoundedRectangleBorder(radius=4))),
                            ElevatedButton(text='entrar',bgcolor='blue', width=60,height=40,color='white',style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)),on_click=lambda _,id=c[0]:produtos_page_visible(id))
                        ]
                    )
                ]
            )
            )
        )
        contador+=1
    return comadas_container