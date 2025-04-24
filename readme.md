/restaurant_app/
│
├── main.py                # Arquivo principal (inicializa o app e define rotas)
│
├── /database/             # Tudo relacionado ao Banco de Dados
│   ├── db_connection.py   # Conexão com o SQL Server
│   ├── queries.py         # Selects, Inserts, Updates e Deletes
│   ├── models.py          # Definição de classes que representam tabelas (opcional)
│
├── /pages/                # Cada página/tela do app
│   ├── login_page.py
│   ├── home_admin_page.py
│   ├── home_garcom_page.py
│   ├── abrir_comanda_page.py
│   ├── visualizar_comandas_page.py
│   ├── adicionar_pedido_page.py
│   ├── gerenciar_estoque_page.py
│   ├── gerenciar_produtos_page.py
│   ├── gerenciar_mesas_page.py
│   ├── relatorios_page.py
│
├── /components/           # Pequenos componentes reaproveitáveis
│   ├── navbar.py          # Barra de navegação
│   ├── mesa_card.py       # Card de uma mesa
│   ├── pedido_item.py     # Item de pedido na comanda
│   ├── input_field.py     # Campos customizados (se quiser estilizar)
│
├── /assets/               # Imagens, ícones, fontes
│   ├── logo.png
│   ├── icons/
│   └── fonts/
│
├── /utils/                # Funções auxiliares
│   ├── auth.py            # Funções de login e verificação de usuário
│   ├── formatters.py      # Formatadores (datas, moedas etc)
│   ├── validators.py      # Validações de formulários
│
├── /config/               # Configurações gerais
│   ├── settings.py        # Configurações do app, como conexões, variáveis de ambiente
│   ├── routes.py          # Organização das rotas
│
└── README.md              # Documentação do projeto
