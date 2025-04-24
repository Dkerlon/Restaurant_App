from database.db_connection import connect

def select_login(user,password):
    conexao_cursor = connect()#0_conexao, 1_cursor
    conexao_cursor[1].execute('SELECT * FROM Usuario WHERE _Login = ? and senha = ?', (user,password))
    usuario_logado = conexao_cursor[1].fetchall()
    conexao_cursor[0].close()
    return usuario_logado[0]