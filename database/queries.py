from database.db_connection import connect
import json
import datetime
def save_user(id):
    try:
        with open('utils/user.json','w') as f:
            json.dump(id,f)
    except:
        pass
def load_json():
    try:
        with open('utils/user.json','r') as f:
            user = json.load(f)
        with open('utils/mesa_load.json','r') as f:
            mesa = json.load(f)
        with open('utils/comanda.json','r') as f:
            comanda = json.load(f)
        return [user,mesa,comanda]
    except Exception as e:
        print(e)
def save_comanda(id):
    try:
        with open('utils/comanda.json','w') as f:
            json.dump(id,f)
    except:
        pass
def select_login(user,password):
    conexao_cursor = connect()#0_conexao, 1_cursor
    conexao_cursor[1].execute('SELECT * FROM Usuario WHERE _Login = ? and senha = ?', (user,password))
    usuario_logado = conexao_cursor[1].fetchall()
    save_user(usuario_logado[0][0])
    load_json()
    conexao_cursor[0].close()
    return usuario_logado[0]
def insert_mesa():
    conexao_cursor = connect()#0_conexao, 1_cursor
    conexao_cursor[1].execute('SELECT * FROM Mesa')
    numero_mesas = conexao_cursor[1].fetchall()
    conexao_cursor[1].execute(f"INSERT INTO Mesa(NumeroMesa,_Status) VALUES({len(numero_mesas)+1},'Fechada')")
    conexao_cursor[0].commit()
    conexao_cursor[0].close()
def select_mesa():
    conexao_cursor = connect()
    conexao_cursor[1].execute('SELECT * FROM Mesa')
    mesas = conexao_cursor[1].fetchall()
    conexao_cursor[0].close()
    return mesas
def delete_mesa(id):
    conexao_cursor = connect()
    conexao_cursor[1].execute(f'DELETE FROM Mesa where Id_Mesa = ?',(id))
    conexao_cursor[0].commit()
    conexao_cursor[0].close()
def alter_status_mesa(status,id):
    conexao_cursor = connect()
    conexao_cursor[1].execute('UPDATE Mesa SET _Status = ? WHERE Id_Mesa = ?',(status,id))
    conexao_cursor[0].commit()
    conexao_cursor[0].close()
def insert_comanda():
    mesa_user = load_json()
    data_abertura = datetime.datetime.now().strftime('%d/%m/%Y')
    conexao_cursor = connect()
    conexao_cursor[1].execute('INSERT INTO comanda(Id_Mesa,Id_Garçom,Data_Abertura,_Status) VALUES (?,?,?,?)',(mesa_user[1],mesa_user[0],data_abertura,'Aberta'))
    conexao_cursor[0].commit()
    conexao_cursor[0].close()
def select_comanda():
    mesa_user = load_json()
    conexao_cursor = connect()
    conexao_cursor[1].execute('SELECT * FROM comanda WHERE Id_Mesa = ?',(mesa_user[1]))
    comandas = conexao_cursor[1].fetchall()
    conexao_cursor[0].close()
    return comandas
def select_categoria_produto():
    conexao_cursor = connect()
    conexao_cursor[1].execute('SELECT * FROM CategoriaProduto')
    categorias = conexao_cursor[1].fetchall()
    print(categorias)
    conexao_cursor[0].close()
    return categorias