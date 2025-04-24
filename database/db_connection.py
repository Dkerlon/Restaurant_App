import pyodbc

def connect():
    try:
        dados_conexao = (
            'Driver={SQL SERVER};'
            'Server=localhost\\SQLEXPRESS;'
            'Database=Garçons_App'
        )
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        return [conexao,cursor]
    except Exception as e:
        print('Erro: '+ e)
