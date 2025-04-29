from flet import *
from database.queries import select_mesa
from database.queries import delete_mesa
from database.queries import alter_status_mesa
import json
def gerar_mesas(control, carregar_mesa=None,page=None):
    def deletar_mesa(id):
        delete_mesa(id)
        carregar_mesa(None)

    def estado_mesa(status, id):
        estado = None
        if status == 'Fechada':
            estado = 'Aberta'
        else:
            estado = 'Fechada'
        alter_status_mesa(estado, id)
        carregar_mesa(None)
    def change_route(id):
        page.go('/abrir_comanda')
        with open('utils/mesa_load.json','w') as f:
            json.dump(id,f) 
    if control == 'gerenciar_mesa':
        mesas = select_mesa()
        main = Column(
            horizontal_alignment='center',
            scroll='auto',
            controls=[
                Container(
                    bgcolor='blue',
                    height=65,
                    width=350,
                    padding=10,
                    content=Row(
                        alignment='left',
                        controls=[
                            Text('Gerenciar Mesas', color='white', size=23, weight=FontWeight.BOLD)
                        ]
                    )
                ),
                # Mesas
            ]
        )

        for mesa in mesas:
            numero_mesa = Text(f'Mesa: {mesa[1]}', size=19, weight=FontWeight.BOLD, color='black')
            status_mesa = Text(f'Status: {mesa[2]}', size=10, color='black')

            main.controls.append(
                Container(
                    padding=10,
                    content=Container(
                        padding=padding.only(10, 5, 10, 10),
                        width=300,
                        height=90,
                        border=border.all(1, 'grey'),
                        content=Column(
                            controls=[
                                Row(
                                    expand=True,
                                    alignment='spaceBetween',
                                    vertical_alignment='center',
                                    controls=[
                                        Column(
                                            alignment='center',
                                            expand=True,
                                            spacing=2,
                                            controls=[
                                                numero_mesa,
                                                status_mesa,
                                            ]
                                        ),
                                        Row(
                                            spacing=7,
                                            controls=[
                                                IconButton(
                                                    icon=icons.CLOSE if mesa[2] == 'Aberta' else icons.OPEN_IN_FULL,
                                                    bgcolor='blue',
                                                    icon_color='white',
                                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)),
                                                    on_click=lambda _, status=mesa[2], id=mesa[0]: estado_mesa(status, id)
                                                ),
                                                IconButton(
                                                    icon=icons.DELETE,
                                                    bgcolor='blue',
                                                    icon_color='white',
                                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=4)),
                                                    on_click=lambda _, id=mesa[0]: deletar_mesa(id)
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                )
            )
    elif control == 'abrir_comanda':
        mesas = select_mesa()
        main = Row(
            wrap=True
        )
        for mesa in mesas:
            main.controls.append(Container(
                width=80,
                height=80,
                bgcolor='green' if mesa[2] == 'Fechada' else 'blue',
                on_click=lambda _,id=mesa[0]:change_route(id),
                content=Column(
                    horizontal_alignment='center',
                    alignment='center',
                    controls=[
                        Text(f'{mesa[1]}',size=18,weight=FontWeight.BOLD)
                    ]
                )
            ))
    return main
