from flet import *
from database.queries import select_categoria_produto
def categorias_produto():
    main = Row(
        height=100,
        expand=True,
        wrap=True
    )
    categorias = select_categoria_produto()
    print(categorias)
    for c in categorias:
        main.controls.append(
            Container(
                height=50,
                width=100,
                bgcolor='blue',
                border_radius=4,
                content=Column(
                    expand=True,
                    alignment='center',
                    controls=[
                        Text(f'{c[1]}',color='white',size=16,text_align='center',weight=FontWeight.BOLD,width=80)
                    ]
                )
            )
        )
    return main