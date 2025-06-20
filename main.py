#--------------------------------------------------------------------------------------------
from flask import Flask , render_template , redirect , request , url_for , flash , jsonify
from flask_socketio import SocketIO , emit ,  join_room, leave_room , send
import sqlite3
from datetime import datetime
import os
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'OLA'
io = SocketIO(app)
#--------------------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from flask_cors import CORS


#--------------------------------------------------------------------------------------------
from flask import Flask , render_template , request , redirect
from flask_socketio import SocketIO , emit 
import sqlite3
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OLA'
io = SocketIO(app)
#--------------------------------------------------------------------------------------------
# usuario_sala_ativa = {}
usuario_cadastrado = 'False'
#--------------------------------------------------------------------------------------------
# formatação da rota inicial que é o login
@app.route('/')
def homes():
    return render_template('index.html')

# fim da fromatação da rota inicial que é o login
#--------------------------------------------------------------------------------------------

# inicio da formtação da configuração do chat de conveersa

# fimda configuração do chat de conveersa    

#--------------------------------------------------------------------------------------------
# formatação do link da rota de cadastro enviado pelo javascript
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
# fim da formatação do link da rota de cadastro enviado pelo javascript
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
# formataçã da routa da pagina de cadastro
@app.route('/cadastro.html' , methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    apelido = request.form.get('apelido')
    senha = request.form.get('senha')
    telefone = request.form.get('tel')
    foto = request.files.get('foto')
    ID_usuario = random.randrange(1000,9999)
    novo_nome_da_foto = foto.filename.replace("-", "_")
    foto.save(os.path.join('static/arquivo_usuario' , novo_nome_da_foto))
    print(novo_nome_da_foto)


   


    conexão = sqlite3.connect('Learn_width_Me')
    cursor = conexão.cursor()
    cursor.execute('''create table if not exists usuario(
    
    id integer primary key,
    nome char(45),
    apelido char(45),
    senha char(45),
    telefone char(45),
    foto char(200),
    ID_usuario char(45),
    curso_usuario
    
    
    )''')

    cursor.execute('''insert into usuario(nome , apelido , senha , telefone , foto , ID_usuario) values (?,?,?,?,?,?)''',(nome , apelido , senha , telefone , novo_nome_da_foto , ID_usuario))
    conexão.commit()
    conexão.close()


    return render_template('index.html')
# fim da formtação da routa da pagina de cadastro
#--------------------------------------------------------------------------------------------


# formatação do inicio de sessão do site
#--------------------------------------------------------------------------------------------
vetor_numerico = []
vetor__SMS = []
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

# --- Funções Auxiliares para Banco de Dados ---
# É uma boa prática ter funções para se conectar e fechar conexões
def get_db_connection(db_name='Learn_width_me'):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row # Permite acessar colunas por nome
    return conn

def close_db_connection(conn):
    if conn:
        conn.close()

# --- Rotas ---

@app.route('/')
def home():
    if 'nome' in session:
        # Se o usuário está na sessão, redireciona para a página principal após login
        # Você pode ajustar isso para ir direto para o dashboard ou uma página de "início"
        return redirect(url_for('inicio_page'))
    return render_template('index.html') # Página de login inicial

@app.route('/index.html', methods=['POST']) # Ou simplesmente @app.route('/login', methods=['POST'])
def logar():
    
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    conexão = sqlite3.connect('Learn_width_Me')
    cursor = conexão.cursor()
    lista = cursor.execute('''select nome , senha , foto , ID_usuario ,  curso_usuario from usuario order by nome asc;''')
    obter = lista.fetchall()
    for x in obter:
        sujeito = f'{x[0]}_{x[3]}'
        n = sujeito
        if (x[0] == nome and x[1] == senha):
            usuario_cadastrado = 'True'
            conexão = sqlite3.connect('Learn_width_Me')
            cursor = conexão.cursor()
            listaAmigos = cursor.execute('''select nome , foto , id from usuario order by nome asc;''')
            obterAmigos = listaAmigos.fetchall()
           
            b = x[2]
            n = f'{x[0]}_{x[3]}'
            codigo_usuario = x[3]
            sujeito = n
        
            
          

            face = sqlite3.connect('faceCurso')
            cursoFace = face.cursor()
            cursoFace.execute('''create table if not exists facess(
            
            id integer primary key,
            nome_user char(45),
            nome_curso char(45),
            link_facebook char(200),
            link_whatsapp char(200),
            imagem_curso char(200)
            
            
            )''')


     
            faceLista = cursoFace.execute('''select nome_user , nome_curso , link_facebook , link_whatsapp , imagem_curso from facess order by nome_curso asc;''')
            faceObter = faceLista.fetchall()

            short = sqlite3.connect('short')
            cursorFaceShort = short.cursor()
            cursorFaceShort.execute('''create table if not exists short(
            
            id integer primary key,
            nome char(45),
            whatsApp char(200),
            short char(200),
            texto char(200)
            
            
            )''')
            listaShort = cursorFaceShort.execute('''select nome , whatsApp , short , texto from short order by nome asc;''')
            obterListaShort = listaShort.fetchall()

            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()
            listaObter=cursor.execute('SELECT nome, foto, id, ID_usuario FROM usuario ORDER BY nome ASC;') # Recarrega lista de amigos
            obterAmigos = listaObter.fetchall()
            # for c in obterAmigos:
            #     print(f'nome:{c[0]} foto:{c[1]} id_usuario:{x[2]}')
            #     print('muito bem avelino')

            conn_sujeito = sqlite3.connect(f'{sujeito}.dados')
            cursor_sujeito = conn_sujeito.cursor()
            cursor_sujeito.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_table (
                     id INTEGER PRIMARY KEY,
                     nome_remitente CHAR(45),
                     imagem_destinatario CHAR(100)
                 )
             ''')
            conn_sujeito.commit()
            obter3 = cursor_sujeito.execute(f'SELECT nome_remitente, imagem_destinatario FROM {sujeito}_table;').fetchall()
            conn_sujeito.commit()
            conn_sujeito.close()


            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()

              # Conectar ao banco de dados de números (sujeito.numero)
            conn_numero = sqlite3.connect(f'{sujeito}.numero')
            cursor_numero = conn_numero.cursor()
            cursor_numero.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_numero (
                     id INTEGER PRIMARY KEY,
                     nome CHAR(45),
                     contador CHAR(100)
                 )
             ''')
            conn_numero.commit()
            listaNumero = cursor_numero.execute(f'SELECT id FROM {sujeito}_numero').fetchall()
            conn_numero.commit()
            conn_numero.close()


            conn_sms = sqlite3.connect(f'{sujeito}_SMS')
            cursor_sms = conn_sms.cursor()
            cursor_sms.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_sms (
                     id INTEGER PRIMARY KEY,
                     destinatario CHAR(45),
                     contador CHAR(45)
                 )
             ''')
            conn_sms.commit()
            obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {sujeito}_sms;').fetchall()

            conn_sms.commit()
            conn_sms.close()

            conn_denuncias = get_db_connection('DENUNCIAS')
            cursor_denuncia = conn_denuncias.cursor()
            cursor_denuncia.execute('''
                 CREATE TABLE IF NOT EXISTS denuncia (
                     id INTEGER PRIMARY KEY,
                     sujeito CHAR(45),
                     remitente CHAR(45),
                     descricao CHAR(100)
                 )
             ''')
            conn_denuncias.commit()
            obter_denuncias = cursor_denuncia.execute('SELECT remitente, sujeito, descricao FROM denuncia ORDER BY id ASC;').fetchall()
            conn_denuncias.commit()
            conn_denuncias.close()

            resultado = "None"

            conn_sms = sqlite3.connect(f'{sujeito}_SMS')
            cursor_sms = conn_sms.cursor()
            cursor_sms.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_sms (
                     id INTEGER PRIMARY KEY,
                     destinatario CHAR(45),
                     contador CHAR(45)
                 )
             ''')
            conn_sms.commit()
            obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {sujeito}_sms;').fetchall()
            for sms in obterSMS:
                v_sms = sms[0]
                
            
            
            conn_sms.commit()
            conn_sms.close()
            # print('outro avelino!')
            # print(sujeito)

            codigos = sqlite3.connect(f'{sujeito}_codigo_gerado')
            cursor_codigo = codigos.cursor()
            cursor_codigo.execute(f'''create table if not exists {sujeito}_codigo_gerado(
                                  
                                  id integer primary key,
                                  nome char(100),
                                  codigo char(100),
                                  outro char(100)

                                  )''')
            Lista_cursor_codigo = cursor_codigo.execute(f'''select id , codigo from {sujeito}_codigo_gerado order by id asc;''')
            obter_Lista_cursor_codigo = Lista_cursor_codigo.fetchall()
            # for w in obter_Lista_cursor_codigo:
            #     print('*'*100)
            #     print(w[0])
            #     print('*'*100)
            codigos.commit()
            codigos.close()

            



            






        
            if usuario_cadastrado == 'True':
                return render_template('inicio.html' , obter_Lista_cursor_codigo = obter_Lista_cursor_codigo , resultado = resultado , obter = obter , obter_denuncias = obter_denuncias , obterSMS = obterSMS ,listaNumero = listaNumero ,  OBTER_LISTA_EMITENTE = OBTER_LISTA_EMITENTE , b = b , n = n , faceObter = faceObter , obterListaShort = obterListaShort , obterAmigos = obterAmigos , sujeito = sujeito , obter3 = obter3)
            else:
   
                return render_template('index.html')
        elif nome == 'Avelino' and senha =='422517Usuario':
            conexão = sqlite3.connect('Learn_To_Mee')
            cursor = conexão.cursor()
            lista = cursor.execute('''select nome , apelido , telefone , foto from usuario order by nome asc;''')
            obter = lista.fetchall()
            
            return render_template('usuario_cadastrado_na_Learn_To_Me.html' , obter = obter)
    return render_template('index.html')
# inicio da formtação das criação da sala do professor
#--------------------------------------------------------------------------------------------
@app.route('/alugar_sala' , methods = ['POST'])
def alugar_sala():
    try:

        nome_da_sala1 = request.form.get('sala')
        novo_nome_da_sala = nome_da_sala1.replace(" ","_")
        nome_usuario = request.form.get('nome')
        senha_usuario = request.form.get('senha')
        link_facebook = request.form.get('facebook')
        link_whatsapp = request.form.get('whatsApp')
        nome_foto = request.files.get('file')
        novo_nome_da_foto = nome_foto.filename.replace(" ","_")

        Learn_width_me = sqlite3.connect('Learn_width_Me')
        cursor_Learn_width_me = Learn_width_me.cursor()
        cursor_Learn_width_me.execute('''create table if not exists usuario(
        
        id integer primary key,
        nome char(45),
        apelido char(45),
        senha char(45),
        telefone char(45),
        foto char(200),
        ID_usuario char(45),
        curso_usuario
        
        
        )''')
        cursor_Learn_width_me.execute(f'''insert into usuario(curso_usuario) values(?)''',(novo_nome_da_sala,))
        lista = cursor_Learn_width_me.execute('''select curso_usuario from usuario order by id asc;''')
        print(f'este é o nome do curso adicionado no banco de dados do usuario {lista.fetchall()}')
        Learn_width_me.commit()
        Learn_width_me.close()
        adim = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
        cursorAdim = adim.cursor()
        cursorAdim.execute(f'''create table if not exists {novo_nome_da_sala}(
        

        id integer primary key,
        nome char(45),
        apelido char(45),
        senha char (45),
        telefone char(45),
        foto char(45),
        video char(200),
        texto char(1000),
        administrador char(45)
        
        
        )''')
        cursorAdim.execute(f'''insert into {novo_nome_da_sala}(administrador , senha) values(?,?)''',(nome_usuario , senha_usuario))
        listaAdim = cursorAdim.execute(f'''select nome , senha from {novo_nome_da_sala} order by nome asc;''')
        obterAdmim = listaAdim.fetchall()
        for x in listaAdim:
            # print('_'*60)
            # print(x[0])
            # print('_'*60)
            print()
        adim.commit()
        adim.close()
    


        face = sqlite3.connect('faceCurso')
        cursoFace = face.cursor()
        cursoFace.execute('''create table if not exists facess(
        
        id integer primary key,
        nome_curso char(45),
        nome_user char(45),
        link_facebook char(200),
        link_whatsapp char(200),
        imagem_curso char(200)
        
        
        )''')

        cursoFace.execute('''insert into facess(nome_curso , nome_user , link_facebook , link_whatsapp , imagem_curso) values(?,?,?,?,?)''',(novo_nome_da_sala ,nome_usuario , link_facebook , link_whatsapp , novo_nome_da_foto))
        face.commit()
        face.close()
        
        face_pasta = os.path.join('static/imagem_face')
        os.makedirs(face_pasta , exist_ok=True)
        #  foto.save(os.path.join('static/arquivo_usuario' , novo_nome_da_foto))
        nome_foto.save(os.path.join('static/imagem_face' , novo_nome_da_foto))

        video = os.path.join('static/' , novo_nome_da_sala)
        imagem = os.path.join(f'static/img_{novo_nome_da_sala}' )
        # print(nome_usuario)
        os.makedirs(video , exist_ok=True)
        os.makedirs(imagem , exist_ok=True)
        conexão = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
        cursor = conexão.cursor()
        cursor.execute(f'''create table if not exists {novo_nome_da_sala}(
        
        id integer primary key,
        nome char(45),
        apelido char(45),
        senha char(45),
        telefone char(45),
        foto char(200)
        
        )''')
        conexão.commit()
        conexão.close()

        return render_template('index.html')
    except Exception as e:
            conexão = sqlite3.connect('Learn_width_Me')
            cursor = conexão.cursor()
            lista = cursor.execute('''select nome , senha , foto , ID_usuario ,  curso_usuario from usuario order by nome asc;''')
            obter = lista.fetchall()
            listaAmigos = cursor.execute('''select nome , foto , id from usuario order by nome asc;''')
            obterAmigos = listaAmigos.fetchall()
           
            b = "x[2]"
            n = "fsuario"
            codigo_usuario = "x[3]"
            sujeito =" n"
            # print(f'este é o codigo do usuario {codigo_usuario}')
            
            # print(b)


            face = sqlite3.connect('faceCurso')
            cursoFace = face.cursor()
            cursoFace.execute('''create table if not exists facess(
            
            id integer primary key,
            nome_user char(45),
            nome_curso char(45),
            link_facebook char(200),
            link_whatsapp char(200),
            imagem_curso char(200)
            
            
            )''')


     
            faceLista = cursoFace.execute('''select nome_user , nome_curso , link_facebook , link_whatsapp , imagem_curso from facess order by nome_curso asc;''')
            faceObter = faceLista.fetchall()

            short = sqlite3.connect('short')
            cursorFaceShort = short.cursor()
            cursorFaceShort.execute('''create table if not exists short(
            
            id integer primary key,
            nome char(45),
            whatsApp char(200),
            short char(200),
            texto char(200)
            
            
            )''')
            listaShort = cursorFaceShort.execute('''select nome , whatsApp , short , texto from short order by nome asc;''')
            obterListaShort = listaShort.fetchall()

            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()
            listaObter=cursor.execute('SELECT nome, foto, id, ID_usuario FROM usuario ORDER BY nome ASC;') # Recarrega lista de amigos
            obterAmigos = listaObter.fetchall()
            # for c in obterAmigos:
            #     print(f'nome:{c[0]} foto:{c[1]} id_usuario:{x[2]}')
            #     print('muito bem avelino')

            conn_sujeito = sqlite3.connect(f'{sujeito}.dados')
            cursor_sujeito = conn_sujeito.cursor()
            cursor_sujeito.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_table (
                     id INTEGER PRIMARY KEY,
                     nome_remitente CHAR(45),
                     imagem_destinatario CHAR(100)
                 )
             ''')
            conn_sujeito.commit()
            obter3 = cursor_sujeito.execute(f'SELECT nome_remitente, imagem_destinatario FROM {sujeito}_table;').fetchall()
            conn_sujeito.commit()
            conn_sujeito.close()


            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()

              # Conectar ao banco de dados de números (sujeito.numero)
            conn_numero = sqlite3.connect(f'{sujeito}.numero')
            cursor_numero = conn_numero.cursor()
            cursor_numero.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_numero (
                     id INTEGER PRIMARY KEY,
                     nome CHAR(45),
                     contador CHAR(100)
                 )
             ''')
            conn_numero.commit()
            listaNumero = cursor_numero.execute(f'SELECT id FROM {sujeito}_numero').fetchall()
            conn_numero.commit()
            conn_numero.close()


            conn_sms = sqlite3.connect(f'{sujeito}_SMS')
            cursor_sms = conn_sms.cursor()
            cursor_sms.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_sms (
                     id INTEGER PRIMARY KEY,
                     destinatario CHAR(45),
                     contador CHAR(45)
                 )
             ''')
            conn_sms.commit()
            obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {sujeito}_sms;').fetchall()

            conn_sms.commit()
            conn_sms.close()

            conn_denuncias = get_db_connection('DENUNCIAS')
            cursor_denuncia = conn_denuncias.cursor()
            cursor_denuncia.execute('''
                 CREATE TABLE IF NOT EXISTS denuncia (
                     id INTEGER PRIMARY KEY,
                     sujeito CHAR(45),
                     remitente CHAR(45),
                     descricao CHAR(100)
                 )
             ''')
            conn_denuncias.commit()
            obter_denuncias = cursor_denuncia.execute('SELECT remitente, sujeito, descricao FROM denuncia ORDER BY id ASC;').fetchall()
            conn_denuncias.commit()
            conn_denuncias.close()

            resultado = "None"

            return render_template('inicio.html' , resultado = resultado , obter = obter , obter_denuncias = obter_denuncias , obterSMS = obterSMS ,listaNumero = listaNumero ,  OBTER_LISTA_EMITENTE = OBTER_LISTA_EMITENTE , b = b , n = n , faceObter = faceObter , obterListaShort = obterListaShort , obterAmigos = obterAmigos , sujeito = sujeito , obter3 = obter3)
    

# fim da formtação da criação da sala do professor

# inicio da formatação da rota dos curso

@app.route('/curso')
def curso():
    return render_template('index.html')

# fim da formatação da rota do curso
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
# inicio da formtação do cadastramento do usuario na sala

@app.route('/user_cadastro' , methods = ['POST'])
def user_cadastro():
    nome_da_sala = request.form.get('sala')
    novo_nome_da_sala = nome_da_sala.replace(" ","_")
    nome_usuario = request.form.get('nome')
    apelido_usuario =request.form.get('apelido')
    telefone_usuario = request.form.get('telefone')
    senha_usuario = request.form.get('senha')
    foto_usuario = request.files.get('file')
    nova_foto_usuario = foto_usuario.filename.replace(" ","_")
    imagem = os.path.join(f'static/img_{novo_nome_da_sala}/imagem_usuario')
    video  = os.path.join(f'static/{novo_nome_da_sala}/video__usuario')
    os.makedirs(imagem , exist_ok=True)
    os.makedirs(video , exist_ok=True)

    
    foto_usuario.save(os.path.join(f'static/img_{novo_nome_da_sala}/imagem_usuario' , nova_foto_usuario))

    sala = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
    cursor = sala.cursor()
    cursor.execute(f'''create table if not exists {novo_nome_da_sala}(
    

    id integer primary key,
    nome char(45),
    apelido char(45),
    senha char (45),
    telefone char(45),
    foto char(45),
    video char(200),
    texto char(1000),
    administrador char(45)
    
    
    )''')

    # cursor.execute(f'''create table if not exists {novo_nome_da_sala}(
                   
    #                id integer primary key,
    #                nome char(45),
    #                apelido char(45),
    #                senha char (45),
    #                telefone char(45),
    #                foto char(45)
                   
    #                )''')
    cursor.execute(f'''insert into {novo_nome_da_sala}(nome , apelido , senha , telefone , foto) values(?,?,?,?,?)''',(nome_usuario , apelido_usuario , senha_usuario , telefone_usuario , nova_foto_usuario))
    sala.commit()
    sala.close()
    # print('esta é a função que esta a ser executada Cláudio Avelino')
    return render_template("index.html")
# fimda formtação do cadastramento dousuario na sala
#--------------------------------------------------------------------------------------------


# inicio da formtação das aulas adionadas as pasta
#--------------------------------------------------------------------------------------------
@app.route('/adicionar_video' , methods = ['POST'])
def adicionar_video():
    nome_sala = request.form.get('sala')
    nome_usuario2 = request.form.get('nome')
    senha_usuario = request.form.get('senha')
    texto = request.form.get('texto')
    novo_nome_da_sala = nome_sala.replace(" ","_")
    video = request.files.get('file')
    novo_nome_do_video = video.filename.replace(" ","_")
    adime = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
    cursorAdime = adime.cursor()
    listaAdime = cursorAdime.execute(f'''select administrador , senha , video from {novo_nome_da_sala} order by nome asc;''')
    obterAdmime = listaAdime.fetchall()
    nome_da_sala = request.form.get('sala')
    novoNomeDaSala = nome_da_sala.replace(" ","_")
    nomeUser = request.form.get('nome')
    senhaUser = request.form.get('senha')
    banco_de_dados = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
    cursoDoBancoDeDados = banco_de_dados.cursor()
    listaDoBancoDeDados = cursoDoBancoDeDados.execute(f'''select nome , apelido , senha , telefone , administrador foto from {novoNomeDaSala} order by nome asc;''')
    obterListaDoBancoDeDados = listaDoBancoDeDados.fetchall()
    for L in obterListaDoBancoDeDados:
        if (L[0] == nomeUser and L[2] == senhaUser):
            banco_de_dados_do_administrador = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
            cursor_do_banco_de_dados_do_administrador = banco_de_dados_do_administrador.cursor()
            lista_do_banco_de_dados_do_administrador = cursor_do_banco_de_dados_do_administrador.execute(f'''select nome , senha , video , texto , administrador from {novoNomeDaSala} order by nome asc;''')
            obter_lista_do_banco_de_dados_do_administrador = lista_do_banco_de_dados_do_administrador.fetchall()
            for t in obter_lista_do_banco_de_dados_do_administrador:
                print(f' bem vindo administrador {t[4]}')
                if t[4]!=None:

                    adiministrador = t[4]
            
            
            O = obter_lista_do_banco_de_dados_do_administrador
            sala = novoNomeDaSala
    conexão = sqlite3.connect('Learn_width_Me')
    cursor = conexão.cursor()
    lista = cursor.execute('''select nome , senha , foto , ID_usuario ,  curso_usuario from usuario order by nome asc;''')
    obter = lista.fetchall()
    for x in obter:
        sujeito = f'{x[0]}_{x[3]}'
        n = sujeito
     
        usuario_cadastrado = 'True'
        conexão = sqlite3.connect('Learn_width_Me')
        cursor = conexão.cursor()
        listaAmigos = cursor.execute('''select nome , foto , id from usuario order by nome asc;''')
        obterAmigos = listaAmigos.fetchall()
       
        b = x[2]
        n = f'{x[0]}_{x[3]}'
        codigo_usuario = x[3]
        sujeito = n
        # print(f'este é o codigo do usuario {codigo_usuario}')
            
        # print(b)


        face = sqlite3.connect('faceCurso')
        cursoFace = face.cursor()
        cursoFace.execute('''create table if not exists facess(
            
            id integer primary key,
            nome_user char(45),
            nome_curso char(45),
            link_facebook char(200),
            link_whatsapp char(200),
            imagem_curso char(200)
            
            
            )''')


     
        faceLista = cursoFace.execute('''select nome_user , nome_curso , link_facebook , link_whatsapp , imagem_curso from facess order by nome_curso asc;''')
        faceObter = faceLista.fetchall()

        short = sqlite3.connect('short')
        cursorFaceShort = short.cursor()
        cursorFaceShort.execute('''create table if not exists short(
            
            id integer primary key,
            nome char(45),
            whatsApp char(200),
            short char(200),
            texto char(200)
            
            
            )''')
        listaShort = cursorFaceShort.execute('''select nome , whatsApp , short , texto from short order by nome asc;''')
        obterListaShort = listaShort.fetchall()

        conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
        cursor_friend = conn_friend.cursor()
        cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
        conn_friend.commit()
        OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
        conn_friend.commit()
        conn_friend.close()
        listaObter=cursor.execute('SELECT nome, foto, id, ID_usuario FROM usuario ORDER BY nome ASC;') # Recarrega lista de amigos
        obterAmigos = listaObter.fetchall()
        # for c in obterAmigos:
        #         print(f'nome:{c[0]} foto:{c[1]} id_usuario:{x[2]}')
        #         print('muito bem avelino')

        conn_sujeito = sqlite3.connect(f'{sujeito}.dados')
        cursor_sujeito = conn_sujeito.cursor()
        cursor_sujeito.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_table (
                     id INTEGER PRIMARY KEY,
                     nome_remitente CHAR(45),
                     imagem_destinatario CHAR(100)
                 )
             ''')
        conn_sujeito.commit()
        obter3 = cursor_sujeito.execute(f'SELECT nome_remitente, imagem_destinatario FROM {sujeito}_table;').fetchall()
        conn_sujeito.commit()
        conn_sujeito.close()


        conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
        cursor_friend = conn_friend.cursor()
        cursor_friend.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                     id INTEGER PRIMARY KEY,
                     nome_destinatario CHAR(45),
                     nome_sala CHAR(45),
                     foto CHAR(100),
                     menssagem CHAR(45)
                 )
             ''')
        conn_friend.commit()
        OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
        conn_friend.commit()
        conn_friend.close()

              # Conectar ao banco de dados de números (sujeito.numero)
        conn_numero = sqlite3.connect(f'{sujeito}.numero')
        cursor_numero = conn_numero.cursor()
        cursor_numero.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_numero (
                     id INTEGER PRIMARY KEY,
                     nome CHAR(45),
                     contador CHAR(100)
                 )
             ''')
        conn_numero.commit()
        listaNumero = cursor_numero.execute(f'SELECT id FROM {sujeito}_numero').fetchall()
        conn_numero.commit()
        conn_numero.close()


        conn_sms = sqlite3.connect(f'{sujeito}_SMS')
        cursor_sms = conn_sms.cursor()
        cursor_sms.execute(f'''
                 CREATE TABLE IF NOT EXISTS {sujeito}_sms (
                     id INTEGER PRIMARY KEY,
                     destinatario CHAR(45),
                     contador CHAR(45)
                 )
             ''')
        conn_sms.commit()
        obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {sujeito}_sms;').fetchall()

        conn_sms.commit()
        conn_sms.close()

        conn_denuncias = get_db_connection('DENUNCIAS')
        cursor_denuncia = conn_denuncias.cursor()
        cursor_denuncia.execute('''
                 CREATE TABLE IF NOT EXISTS denuncia (
                     id INTEGER PRIMARY KEY,
                     sujeito CHAR(45),
                     remitente CHAR(45),
                     descricao CHAR(100)
                 )
             ''')
        conn_denuncias.commit()
        obter_denuncias = cursor_denuncia.execute('SELECT remitente, sujeito, descricao FROM denuncia ORDER BY id ASC;').fetchall()
        conn_denuncias.commit()
        conn_denuncias.close()


    for xA in obterAdmime:
        # print(xA[0])
        # print(xA[1])
        
        # print('-'*40)
        # print(nome_usuario2)
        # print(senha_usuario)
        # print('-'*40)

        if (xA[0] == nome_usuario2 and xA[1] == senha_usuario):
            nome_do_banco_de_dados = f'{xA[0]}_{xA[1]}'
            banco_de_dados_do_texto = sqlite3.connect(nome_do_banco_de_dados)
            cursor = banco_de_dados_do_texto.cursor()
            cursor.execute(f'''create table if not exists {nome_do_banco_de_dados}(
                           
                           id integer primary key,
                           nome_do_administrador char(45),
                           texto_do_administrador char(45),
                           posicao char(100)

                           
                           )''')
            cursor.execute(f'''insert into {nome_do_banco_de_dados}(texto_do_administrador,nome_do_administrador,posicao) values (?,?,?)''',(texto,nome_usuario2,0))
            listar = cursor.execute(f'''select nome_do_administrador , texto_do_administrador from {nome_do_banco_de_dados} order by id asc''')
            obter = listar.fetchall()
            abrir_sala = sqlite3.connect(f'{sujeito}_abrir_sala')
            cursor_abrir_sala = abrir_sala.cursor()
            cursor_abrir_sala.execute(f'''create table if not exists {sujeito}_abrir_sala(
                                    
                                    id integer primary key,
                                    nome char (45),
                                    valor char(45)

                                    )''')
            cursor_abrir_sala.execute(f'''insert into {sujeito}_abrir_sala(nome , valor) values (?,?)''',(sujeito ,novoNomeDaSala))
            abrir_lista = cursor_abrir_sala.execute(f'''select nome , valor from {sujeito}_abrir_sala order by id asc;''')
            obter_lista_aberta = abrir_lista.fetchall()
            for t in obter_lista_aberta:
                resultado = t[1]
            abrir_sala.commit()
            abrir_sala.close()
            for r in obter:
                # print('_'*90)
                # print(r)
                c = r[1]
                # print('_'*90)
            banco_de_dados_do_texto.commit()
            banco_de_dados_do_texto.close()
            # print('-'*40)
            # print('esta funcionando claudio avelino!')
            # print('-'*40)
            vd = xA[2]
            sala = novo_nome_da_sala
            video.save(os.path.join(f'static/{novo_nome_da_sala}' , novo_nome_do_video))
            adime = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
            cursorAdime = adime.cursor()
            cursorAdime.execute(f'''insert into {novo_nome_da_sala}(nome , senha , video , texto) values(? , ? , ? , ?)''',(nome_usuario2, senha_usuario , novo_nome_do_video , texto))
            L = cursorAdime.execute(f'''select nome , senha , video , texto from {novo_nome_da_sala} order by nome asc;''')
            O = L.fetchall()
            for f in O:
                sala = novo_nome_da_sala
                # print("-"*40)
                # print(f[3])
                # print("-"*40)
            adime.commit()
            adime.close()
            print(sala)
            # print('esta é a sala')
            n = nome_usuario2
            # print(f'este é o sujeito claudio {n}')
            return render_template('inicio.html' , nome_usuario2 = nome_usuario2 , resultado = resultado , c = c  , adiministrador = adiministrador , O = O , sala = sala , nome_da_sala = nome_da_sala , nomeUser = nomeUser , obter = obter , obter_denuncias = obter_denuncias , obterSMS = obterSMS ,listaNumero = listaNumero ,  OBTER_LISTA_EMITENTE = OBTER_LISTA_EMITENTE , b = b , n = n , faceObter = faceObter , obterListaShort = obterListaShort , obterAmigos = obterAmigos , sujeito = sujeito , obter3 = obter3)
        
    adime.commit()
    adime.close()
        

    if (xA[0] == nome_usuario2  and xA[1]==senha_usuario):
            # print(xA[0])
            # print(xA[1])
            video.save(os.path.join(f'static/{novo_nome_da_sala}' , novo_nome_do_video))
            adime = sqlite3.connect(f'{novo_nome_da_sala}_banco_de_dados')
            cursorAdime = adime.cursor()
            cursorAdime.execute(f'''insert into {novo_nome_da_sala}(administrador , senha , video) values(? , ? , ?)''',(nome_usuario2, senha_usuario , novo_nome_do_video))
            adime.commit()
            adime.close()
            return render_template('index.html')
    else:
        return render_template('index.html')
    return render_template('index.html')
#--------------------------------------------------------------------------------------------



# fim da formytaçã das aulas adionais as pasta


# inicio da formtaçãofde entrar na sala
#--------------------------------------------------------------------------------------------

@app.route('/entrar_na_sala', methods=['POST'])
def entrar_na_sala():
    try:
            
        nome_da_sala = request.form.get('sala')
        novoNomeDaSala = nome_da_sala.replace(" ","_")
        nomeUser = request.form.get('nome')
        senhaUser = request.form.get('senha')
        banco_de_dados = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
        cursoDoBancoDeDados = banco_de_dados.cursor()
        listaDoBancoDeDados = cursoDoBancoDeDados.execute(f'''select nome , apelido , senha , telefone , foto from {novoNomeDaSala} order by nome asc;''')
        obterListaDoBancoDeDados = listaDoBancoDeDados.fetchall()
        for L in obterListaDoBancoDeDados:
            if (L[0] == nomeUser and L[2] == senhaUser):
                banco_de_dados_do_administrador = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
                cursor_do_banco_de_dados_do_administrador = banco_de_dados_do_administrador.cursor()
                lista_do_banco_de_dados_do_administrador = cursor_do_banco_de_dados_do_administrador.execute(f'''select nome , senha , video , texto , administrador from {novoNomeDaSala} order by nome asc;''')
                obter_lista_do_banco_de_dados_do_administrador = lista_do_banco_de_dados_do_administrador.fetchall()
                for t in obter_lista_do_banco_de_dados_do_administrador:
                    # print(f' bem vindo administrador {t[4]}')
                    if t[4]!=None:

                        adiministrador = t[4]
                # print('fora')
                # print(adiministrador)
                O = obter_lista_do_banco_de_dados_do_administrador
                sala = novoNomeDaSala
        conexão = sqlite3.connect('Learn_width_Me')
        cursor = conexão.cursor()
        lista = cursor.execute('''select nome , senha , foto , ID_usuario ,  curso_usuario from usuario order by nome asc;''')
        obter = lista.fetchall()
        for g in obter:
            # print('este é o obter claudio avelino',g[0])
            sujeito = f'{g[0]}_{g[3]}'
            n = nomeUser
            # print(f'esta aqui:{g[3]}')
            
            usuario_cadastrado = 'True'
            conexão = sqlite3.connect('Learn_width_Me')
            cursor = conexão.cursor()
            listaAmigos = cursor.execute('''select nome , foto , id from usuario order by nome asc;''')
            obterAmigos = listaAmigos.fetchall()
            
            b = g[2]
            codigo_usuario = g[3]
            sujeito = n
            # print(f'este é o codigo do usuario {codigo_usuario}')
                
            # print(b)


            face = sqlite3.connect('faceCurso')
            cursoFace = face.cursor()
            cursoFace.execute('''create table if not exists facess(
                
                id integer primary key,
                nome_user char(45),
                nome_curso char(45),
                link_facebook char(200),
                link_whatsapp char(200),
                imagem_curso char(200)
                
                
                )''')


        
            faceLista = cursoFace.execute('''select nome_user , nome_curso , link_facebook , link_whatsapp , imagem_curso from facess order by nome_curso asc;''')
            faceObter = faceLista.fetchall()

            short = sqlite3.connect('short')
            cursorFaceShort = short.cursor()
            cursorFaceShort.execute('''create table if not exists short(
                
                id integer primary key,
                nome char(45),
                whatsApp char(200),
                short char(200),
                texto char(200)
                
                
                )''')
            listaShort = cursorFaceShort.execute('''select nome , whatsApp , short , texto from short order by nome asc;''')
            obterListaShort = listaShort.fetchall()

            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                    CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                        id INTEGER PRIMARY KEY,
                        nome_destinatario CHAR(45),
                        nome_sala CHAR(45),
                        foto CHAR(100),
                        menssagem CHAR(45)
                    )
                ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()
            listaObter=cursor.execute('SELECT nome, foto, id, ID_usuario FROM usuario ORDER BY nome ASC;') # Recarrega lista de amigos
            obterAmigos = listaObter.fetchall()
            for c in obterAmigos:
                    # print(f'nome:{c[0]} foto:{c[1]} id_usuario:{g[2]}')
                    # print('muito bem avelino')
                    a = 0

            conn_sujeito = sqlite3.connect(f'{sujeito}.dados')
            cursor_sujeito = conn_sujeito.cursor()
            cursor_sujeito.execute(f'''
                    CREATE TABLE IF NOT EXISTS {sujeito}_table (
                        id INTEGER PRIMARY KEY,
                        nome_remitente CHAR(45),
                        imagem_destinatario CHAR(100)
                    )
                ''')
            conn_sujeito.commit()
            obter3 = cursor_sujeito.execute(f'SELECT nome_remitente, imagem_destinatario FROM {sujeito}_table;').fetchall()
            conn_sujeito.commit()
            conn_sujeito.close()


            conn_friend = sqlite3.connect(f'{sujeito}_FRIEND')
            cursor_friend = conn_friend.cursor()
            cursor_friend.execute(f'''
                    CREATE TABLE IF NOT EXISTS {sujeito}_tabela_conversa (
                        id INTEGER PRIMARY KEY,
                        nome_destinatario CHAR(45),
                        nome_sala CHAR(45),
                        foto CHAR(100),
                        menssagem CHAR(45)
                    )
                ''')
            conn_friend.commit()
            OBTER_LISTA_EMITENTE = cursor_friend.execute(f'SELECT nome_destinatario, nome_sala, foto, menssagem FROM {sujeito}_tabela_conversa;').fetchall()
            conn_friend.commit()
            conn_friend.close()

                # Conectar ao banco de dados de números (sujeito.numero)
            conn_numero = sqlite3.connect(f'{sujeito}.numero')
            cursor_numero = conn_numero.cursor()
            cursor_numero.execute(f'''
                    CREATE TABLE IF NOT EXISTS {sujeito}_numero (
                        id INTEGER PRIMARY KEY,
                        nome CHAR(45),
                        contador CHAR(100)
                    )
                ''')
            conn_numero.commit()
            listaNumero = cursor_numero.execute(f'SELECT id FROM {sujeito}_numero').fetchall()
            conn_numero.commit()
            conn_numero.close()


            conn_sms = sqlite3.connect(f'{sujeito}_SMS')
            cursor_sms = conn_sms.cursor()
            cursor_sms.execute(f'''
                    CREATE TABLE IF NOT EXISTS {sujeito}_sms (
                        id INTEGER PRIMARY KEY,
                        destinatario CHAR(45),
                        contador CHAR(45)
                    )
                ''')
            conn_sms.commit()
            obterSMS = cursor_sms.execute(f'SELECT id, destinatario FROM {sujeito}_sms;').fetchall()

            conn_sms.commit()
            conn_sms.close()

            conn_denuncias = get_db_connection('DENUNCIAS')
            cursor_denuncia = conn_denuncias.cursor()
            cursor_denuncia.execute('''
                    CREATE TABLE IF NOT EXISTS denuncia (
                        id INTEGER PRIMARY KEY,
                        sujeito CHAR(45),
                        remitente CHAR(45),
                        descricao CHAR(100)
                    )
                ''')
            conn_denuncias.commit()
            obter_denuncias = cursor_denuncia.execute('SELECT remitente, sujeito, descricao FROM denuncia ORDER BY id ASC;').fetchall()
            conn_denuncias.commit()
            conn_denuncias.close()
            abrir_sala = sqlite3.connect(f'{sujeito}_abrir_sala')
            cursor_abrir_sala = abrir_sala.cursor()
            cursor_abrir_sala.execute(f'''create table if not exists {sujeito}_abrir_sala(
                                    
                                    id integer primary key,
                                    nome char (45),
                                    valor char(45)

                                    )''')
            cursor_abrir_sala.execute(f'''insert into {sujeito}_abrir_sala(nome , valor) values (?,?)''',(sujeito ,novoNomeDaSala))
            abrir_lista = cursor_abrir_sala.execute(f'''select nome , valor from {sujeito}_abrir_sala order by id asc;''')
            obter_lista_aberta = abrir_lista.fetchall()
            for t in obter_lista_aberta:
                resultado = t[1]
            abrir_sala.commit()
            abrir_sala.close()
            sala = novoNomeDaSala
            # print(sala)
            # print('esta é o novo nome da sua sala')
            adime = sqlite3.connect(f'{sala}_banco_de_dados')
            cursorAdime = adime.cursor()
            listaAdime = cursorAdime.execute(f'''select administrador , senha , video from {sala} order by nome asc;''')
            obterAdmime = listaAdime.fetchall()
            nome_da_sala = request.form.get('sala')
            novoNomeDaSala = nome_da_sala.replace(" ","_")
            nomeUser = request.form.get('nome')
            senhaUser = request.form.get('senha')
            banco_de_dados = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
            cursoDoBancoDeDados = banco_de_dados.cursor()
            listaDoBancoDeDados = cursoDoBancoDeDados.execute(f'''select nome , apelido , senha , telefone , foto from {novoNomeDaSala} order by nome asc;''')
            obterListaDoBancoDeDados = listaDoBancoDeDados.fetchall()
            for L in obterListaDoBancoDeDados:
                if (L[0] == nomeUser and L[2] == senhaUser):
                    banco_de_dados_do_administrador = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
                    cursor_do_banco_de_dados_do_administrador = banco_de_dados_do_administrador.cursor()
                    lista_do_banco_de_dados_do_administrador = cursor_do_banco_de_dados_do_administrador.execute(f'''select nome , senha , video , texto , administrador from {novoNomeDaSala} order by nome asc;''')
                    obter_lista_do_banco_de_dados_do_administrador = lista_do_banco_de_dados_do_administrador.fetchall()
                    for t in obter_lista_do_banco_de_dados_do_administrador:
                        # print(f' bem vindo administrador {t[4]}')
                        if t[4]!=None:

                            adiministrador = t[4]
                    # print('fora')
                    # print(adiministrador)
                    O = obter_lista_do_banco_de_dados_do_administrador
                    membro = sqlite3.connect(f'{novoNomeDaSala}_banco_de_dados')
                    cursor_membro = membro.cursor()
                    cursor_membro.execute(f'''create table if not exists {novoNomeDaSala}(
        

                        id integer primary key,
                        nome char(45),
                        apelido char(45),
                        senha char (45),
                        telefone char(45),
                        foto char(45),
                        video char(200),
                        texto char(1000),
                        administrador char(45)
                        
                        
                        )''')

                    lista_membro = cursor_membro.execute(f'''select nome , apelido , telefone , administrador from {novoNomeDaSala} order by id asc;''')
                    obter_lista_membro = lista_membro.fetchall()
                    # print(f'kakakakakakakkakakakkakakakakka é este :  {obter_lista_membro}')
                    for p in obter_lista_membro:
                        # print('____'*100)
                        # print(f'nome:{p[0]}  apelido:{p[1]}')
                        # print('____'*100)
                        # print(p)
                        administrador_nome = p[3]

                    membro.commit()
                    membro.close()
                
                    # print(f'este é o sujeito claudio {n}')
                    # print(f'esta aqui:{g[3]}')

                    carregar_menssagem = sqlite3.connect(f'{nome_da_sala}_mensagem_grupo')
                    cursor_carregar_menssagem = carregar_menssagem.cursor()
                    cursor_carregar_menssagem .execute(f'''create table if not exists {nome_da_sala}_mensagem_grupo(
                                   
                                   id integer primary key,
                                   nome char(100),
                                   menssagem char(1000),
                                   sala char(45),
                                   caso char(45)
                                   



                                   )''')
                    Listas = cursor_carregar_menssagem.execute(f'''select nome , menssagem , sala from {nome_da_sala}_mensagem_grupo order by id asc;''')
                    obter_menssgem_grupo = Listas.fetchall()
                    for t in obter_menssgem_grupo:
                        # print('menssagem do grupo')
                        # print(t)
                        a = 0
                    carregar_menssagem.commit()
                    carregar_menssagem.close()
                    

            # print('outro avelino!')
            # print(sujeito)

            codigos = sqlite3.connect(f'{sujeito}_codigo_gerado')
            cursor_codigo = codigos.cursor()
            cursor_codigo.execute(f'''create table if not exists {sujeito}_codigo_gerado(
                                  
                                  id integer primary key,
                                  nome char(100),
                                  codigo char(100),
                                  outro char(100)

                                  )''')
            Lista_cursor_codigo = cursor_codigo.execute(f'''select id , codigo from {sujeito}_codigo_gerado order by id asc;''')
            obter_Lista_cursor_codigo = Lista_cursor_codigo.fetchall()
            for w in obter_Lista_cursor_codigo:
                # print('*'*100)
                # print(w[0])
                # print('*'*100)
                a = 0
            codigos.commit()
            codigos.close()







        return render_template("inicio.html" , obter_Lista_cursor_codigo = obter_Lista_cursor_codigo , obter_menssgem_grupo = obter_menssgem_grupo , n = n , obter_lista_membro = obter_lista_membro , O = O , sala = sala , resultado = resultado  , obter = obter , obter_denuncias = obter_denuncias , obterSMS = obterSMS ,listaNumero = listaNumero ,  OBTER_LISTA_EMITENTE = OBTER_LISTA_EMITENTE , b = b , faceObter = faceObter , obterListaShort = obterListaShort , obterAmigos = obterAmigos , sujeito = sujeito , obter3 = obter3 , novoNomeDaSala=novoNomeDaSala , nomeUser = nomeUser)
    except Exception as e:
        print('ola mundo')
        return render_template('index.html')


#--------------------------------------------------------------------------------------------



# fim da formtação de entrar na sala


# inicio da configuração do short
#--------------------------------------------------------------------------------------------
@app.route('/short' , methods=["POST"])
def short():
    nome_short = request.files.get('file')
    link_whatsapp_short = request.form.get('whatsApp')
    nomeUser = request.form.get('nome')
    texto = request.form.get('texto')
    novo_nome_short = nome_short.filename.replace(" ","_")
    pastaUser = os.path.join(f'static/meu_short/short')
    os.makedirs(pastaUser , exist_ok=True)
    nome_short.save(os.path.join('static/meu_short/short' , novo_nome_short))

    shor = sqlite3.connect('short')
    cursor = shor.cursor()
    cursor.execute('''create table if not exists short(
    
    id integer primary key,
    nome char(45),
    texto char(200),
    whatsApp char(200),
    shorts char(200)
    
    )''')
    cursor.execute('''insert into short(nome , texto , whatsApp , short) values(?,?,?,?)''',(nomeUser , texto , link_whatsapp_short , novo_nome_short))
    shor.commit()
    shor.close()

    return render_template('index.html')
#--------------------------------------------------------------------------------------------




























DATABASE = 'chat.db'  # O arquivo será criado na mesma pasta



first_request = True
#--------------------------------------------------------------------------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
    return conn
#--------------------------------------------------------------------------------------------
def close_db(conn):
    if conn:
        conn.close()
#--------------------------------------------------------------------------------------------
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room TEXT NOT NULL,
            sender TEXT NOT NULL,
            text TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    close_db(conn)
#--------------------------------------------------------------------------------------------
@app.before_request
def before_request():
    global first_request
    if first_request:
        init_db()
        print('Banco de dados inicializado (se necessário).')
        first_request = False

#--------------------------------------------------------------------------------------------
@io.on('join')
def on_join(data):
    room = data.get('room')
    user = data.get('user')
    if room and user:
        join_room(room)
        emit('status', {'msg': f'{user} entrou na sala {room}.'}, room=room)

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT sender, text, timestamp FROM messages WHERE room = ? ORDER BY timestamp", (room,))
        messages = cursor.fetchall()
        for t in messages:
            # print('---'*100)
            # print(t[1])
            # print('---'*100)
            a = 0
        close_db(conn)

        messages_data = [{'sender': msg['sender'], 'text': msg['text'], 'timestamp': msg['timestamp']} for msg in messages]
        emit('carregar_mensagenss', {'messages': messages_data})
     
    else:
        emit('status', {'msg': 'Por favor, especifique um nome de sala e seu nome para entrar.'}, session=request.sid)
#--------------------------------------------------------------------------------------------
@io.on('leave')
def on_leave(data):
    room = data.get('room')
    user = data.get('user')
    if room and user:
        leave_room(room)
        emit('status', {'msg': f'{user} saiu da sala {room}.'}, room=room)
#--------------------------------------------------------------------------------------------
@io.on('message')
def handle_message(data):
    room = data.get('room')
    message = data.get('message')
    sender = data.get('sender')
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    if room and message and sender:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (room, sender, text, timestamp) VALUES (?, ?, ?, ?)", (room, sender, message, timestamp))
        conn.commit()
        close_db(conn)

        emit('new_message', {'sender': sender, 'text': message, 'timestamp': timestamp}, room=room)

#--------------------------------------------------------------------------------------------
@io.on('typing')
def handle_typing(data):
    room = data.get('room')
    user = data.get('user')
    if room and user:
        emit('user_typing', {'room': room, 'user': user}, room=room, include_self=False)
#--------------------------------------------------------------------------------------------
@io.on('stop_typing')
def handle_stop_typing(data):
    room = data.get('room')
    user = data.get('user')
    if room and user:
        emit('user_stopped_typing', {'room': room, 'user': user}, room=room, include_self=False)
#--------------------------------------------------------------------------------------------
usuarios_conectados= {}
@io.on('conn')
def connecta(data):
    nome = data.get('nome_remitente')

    if nome:
        sid = request.sid
        # print('-'*50)
        # print(nome)
        # print('muito bem, você está conectado!')
        # print('usuario conectado:', sid)
        usuarios_conectados[sid] = {'nome': nome}

        # Salvar informações no banco de dados
        DATABASE_NOTA = sqlite3.connect('nota')
        cursor = DATABASE_NOTA.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS noticia (
                                        id INTEGER PRIMARY KEY,
                                        sid_usuario CHAR(45),
                                        nome_usuario CHAR(45)
                                    )''')
        cursor.execute('''INSERT INTO noticia (sid_usuario, nome_usuario) VALUES (?, ?)''', (sid, nome))
        DATABASE_NOTA.commit()
        DATABASE_NOTA.close()

        # print("Lista de usuários conectados:", usuarios_conectados)
vetor = []
@io.on('sendNoticia')
def sendNoticia(data):
    nome_remitente = data.get('nome_remitente')
    nome_destinatario = data.get('nome_destinatario')
    imagem_destinatario = data.get('imagem')
    sala = data.get('sala')

    print(f"Mensagem de: {nome_remitente} para: {nome_destinatario}")

    sid_destinatario = None
    for sid_conectado, info in usuarios_conectados.items():
        if info['nome'] == nome_destinatario:
            sid_destinatario = sid_conectado
            break

    if sid_destinatario:
        emit('getNoticia', {'nome_destinatario': nome_remitente, 'image': imagem_destinatario,'sala':sala}, to=sid_destinatario )
        print(f"Notificação enviada para o SID: {sid_destinatario}")
        # Salvar a notificação no banco de dados do destinatário
        DATABASE2 = sqlite3.connect(f'{nome_destinatario}.dados')
        cursor2 = DATABASE2.cursor()
        cursor2.execute(f'''CREATE TABLE IF NOT EXISTS {nome_destinatario}_table (
                                            id INTEGER PRIMARY KEY,
                                            nome_remitente CHAR(45),
                                            imagem_destinatario CHAR(100)
                                        )''')
        cursor2.execute(f'''INSERT INTO {nome_destinatario}_table (nome_remitente, imagem_destinatario) VALUES (?, ?)''', (nome_remitente, imagem_destinatario))
        DATABASE2.commit()
        DATABASE2.close()
    else:
        print(f"Usuário destinatário '{nome_destinatario}' não encontrado ou não conectado.")
    # inicio da formatação do numero de notificação
    f = sqlite3.connect(f'{nome_destinatario}.numero')
    c = f.cursor()
    c.execute(f'''create table if not exists {nome_destinatario}_numero(
              
              id integer primary key,
              nome char(45),
              contador char(100)

              )''')
    c.execute(f'''insert into {nome_destinatario}_numero(nome,contador)values(?,?)''',(nome_destinatario,0))
    l = c.execute(f'''select nome, id from {nome_destinatario}_numero;''')
    b = l.fetchall()
    for t in b:
        # print(t)
        a = 0
    f.commit()
    f.close()

    # fim do inicio da formatação do numero da notificação    


   

#-----------------------------------------------------------------------------------------------------------------
   
   
#-----------------------------------------------------------------------------------------------------------------

@io.on('usuario')
def conecta(data):
    # print(data['nome'])
    nome = request.sid
    emit('get_user',{'nome':nome} , broadcast=True)
    # print('esta certo')
    # print(nome)
    # print('-'*50)



@io.on('criar_sala')
def criar_sala(data):
    nome_remitente = data['nome_remitente']
    # print(nome_remitente)
    nome_destinatario = data['nome_destinatario']
    # print(f'ola claudio este é o valor da variavel nom_destinatario:{nome_destinatario}')
    nome_sala = data['sala']
    DATABASE_LEARN = sqlite3.connect('Learn_width_Me')
    CURSOR_DATABASE_LEARN =DATABASE_LEARN.cursor()
    LISTA_LEARN = CURSOR_DATABASE_LEARN.execute('''select nome , foto , ID_usuario from usuario order by nome asc;''')
    OBTER_LISTA_LEARN = LISTA_LEARN.fetchall()
    for LEARN in OBTER_LISTA_LEARN:
        nomeUser = f'{LEARN[0]}_{LEARN[2]}'
        if nome_destinatario == nomeUser:
            # print('-'*100)
            foto = LEARN[1]
            # print('esta é a minha foto')

            DATABASE_REMITENTE = sqlite3.connect(f'{nome_remitente}_FRIEND')
            CURSOR_REMITENTE = DATABASE_REMITENTE.cursor()
            CURSOR_REMITENTE.execute(f'''create table if not exists {nome_remitente}_tabela_conversa(
                                    
                                    id integer primary key,
                                    nome_destinatario char(45),
                                    nome_sala char(45),
                                    foto char(100),
                                    menssagem char(45)

                                    
                                    
                                    )''') 
            
            CURSOR_REMITENTE.execute(f'''insert into {nome_remitente}_tabela_conversa(nome_destinatario,nome_sala,foto) values(?,?,?)''',(nome_destinatario,nome_sala,foto))
            DATABASE_REMITENTE.commit()
            DATABASE_REMITENTE.close()
    #-------------------------------------------------------------
        elif nome_remitente == nomeUser:
            foto2 = LEARN[1]
            DATABASE_DESTINATARIO = sqlite3.connect(f'{nome_destinatario}_FRIEND')
            CURSOR_DESTINATARIO = DATABASE_DESTINATARIO.cursor()
            CURSOR_DESTINATARIO.execute(f'''create table if not exists {nome_destinatario}_tabela_conversa(
                                        

                                        id integer primary key,
                                        nome_destinatario char(45),
                                        nome_sala char(45),
                                        foto char(100),
                                        menssagem char(45)
                                        
                                        
                                        )''')
            CURSOR_DESTINATARIO.execute(f'''insert into {nome_destinatario}_tabela_conversa( nome_destinatario,nome_sala,foto) values(?,?,?)''',(nome_remitente,nome_sala,foto2))
            DATABASE_DESTINATARIO.commit()
            DATABASE_DESTINATARIO.close()


            nome_destinatario = data.get('nome_destinatario') # estou a pegar o nome do desnatario pelo javascript
            sala = data.get('sala') # estou a pegar o nome da sala pelo javascript
            nome_remitente = data.get('nome_remitente') # estou a pegar o nome do remitente pelo javasript

            sid_destinatario = None
            for sid_conectado, info in usuarios_conectados.items():
                if info['nome'] == nome_destinatario:
                    sid_destinatario = sid_conectado
                    break
            

            if sid_destinatario:
                emit('nova_sala_criada_notificacao', {'nome_remitente': nome_remitente, 'sala': sala}, to=sid_destinatario)
                print(f"Notificação (nova_sala_criada_notificacao) enviada para {nome_destinatario} (SID: {sid_destinatario}), sala: {sala}")
            else:
                print(f"Destinatário '{nome_destinatario}' não encontrado ou não conectado para notificação da sala: {sala}")

    #------------------------------------------------------------------
    

@io.on('limpar')
def limpar(data):
    # print(data.get('nome_remitente'))
    # print('_'*100)
    nome_remitente = data.get('nome_remitente')
    DATABASE2 = sqlite3.connect(f'{nome_remitente}.dados')
    CURSOR_DATABASE2 = DATABASE2.cursor()
    CURSOR_DATABASE2.execute(f'''delete from {nome_remitente}_table''')
    DATABASE2.commit()
    DATABASE2.close()

    
@io.on('deletar_amigo')
def deletar_amigo(data):
    nome_remitente = data.get('nome_remitente')


    nome_destinatario_deletar = data.get('nome_amigo')
    # print(nome_remitente)
    # print(nome_destinatario_deletar)
    DATABASE_REMITENTE = sqlite3.connect(f'{nome_remitente}_FRIEND')
    CURSOR_DATABASE_REMITENTE = DATABASE_REMITENTE.cursor()
    CURSOR_DATABASE_REMITENTE.execute(f'''create table if not exists {nome_remitente}_tabela_conversa(
                                      
                                        id integer primary key,
                                        nome_destinatario char(45),
                                        nome_sala char(45),
                                        foto char(100),
                                        menssagem char(45)
                                       
                                      
                                      )''')
    CURSOR_DATABASE_REMITENTE.execute(f'''delete from {nome_remitente}_tabela_conversa where nome_destinatario=?''',(nome_destinatario_deletar,))
    print(f'o {nome_destinatario_deletar} foi deletado.')
    L = CURSOR_DATABASE_REMITENTE.execute(f'''select * from {nome_remitente}_tabela_conversa;''')
    B = L.fetchall()
    for t in B:
        # print(f'_'*40)
        # print(t)
        # print(f'_'*40)
        a = 0
    DATABASE_REMITENTE.commit()
    DATABASE_REMITENTE.close()

@io.on('limpa')
def limpar(data):
    nome_remitente = data.get('nome_remitente')
    DATABASE = sqlite3.connect(f'{nome_remitente}.numero')
    CURSOR = DATABASE.cursor()
    CURSOR.execute(f'''delete from {nome_remitente}_numero''')
    print('dados deletado com sucesso!')
    DATABASE.commit()
    DATABASE.close()


# @io.on('contador_menssagem')
# def contador_menssagem(data):
#     remitente = data.get('nome_remitente')
#     destinatario = data.get('nome_destinatario')
#     sid_destinatario = None
#     for sid_conectado, info in usuarios_conectados.items():
#         if info['nome'] == destinatario:
#             sid_destinatario = sid_conectado
#             break
            

#         if sid_destinatario:
#             emit('nova_menssagem', {'nome_remitente': remitente}, to=sid_destinatario)
#             print(f"Notificação (nova_sala_criada_notificacao) enviada para {destinatario} (SID: {sid_destinatario})")
#         else:
#             print(f"Destinatário '{destinatario}' não encontrado ou não conectado para notificação da sala:")

#     print(f'funcionou avelino! >>>{remitente}')
vetor_sms = []
@io.on('nova__menssagem')
def nova__menssagem(data):
    contador = data.get('contador')
    nome_destinatario = data['nome_destinatario']
    nome_remitente = data['nome_remitente']
    # print(f'avelino já estou a capturar o nome do remitente:{nome_remitente}')
    # print(f'este e o nome do destinatario: {nome_destinatario}')
    # print(f'este é o valor do contador:{contador}')

    # segunda fase
    DATABASE = sqlite3.connect(f'{nome_destinatario}_SMS')
    cursor = DATABASE.cursor()
    cursor.execute(f'''create table if not exists {nome_destinatario}_sms(
                   
                   id integer primary key,
                   destinatario char(45),
                   contador char(45)
                   
                   )''')
    cursor.execute(f'''insert into {nome_destinatario}_sms(destinatario,contador) values(?,?)''',(nome_remitente,0))
    L = cursor.execute(f'''select id from {nome_destinatario}_sms''')
    B = L.fetchall()
    for r in B:
        # print(r[0])
        # print('__'*40)
        a = 0
    DATABASE.commit()
    DATABASE.close()
    DATABASE_REMITENTE = sqlite3.connect(f'{nome_destinatario}_FRIEND')
    CURSOR_REMITENTE = DATABASE_REMITENTE.cursor()
    CURSOR_REMITENTE.execute(f'''create table if not exists {nome_destinatario}_tabela_conversa(
                                     
                             id integer primary key,
                             nome_destinatario char(45),
                             nome_sala char(45),
                             foto char(100),
                             menssagem char(45)
                                     
                                     )''')
    CURSOR_REMITENTE.execute(f'''update {nome_destinatario}_tabela_conversa set menssagem = ? where nome_destinatario = ?''',(nome_remitente,nome_remitente))
    lista = CURSOR_REMITENTE.execute(f'''select nome_destinatario , menssagem from {nome_destinatario}_tabela_conversa;''')
    obter = lista.fetchall()
    for t in obter:
        # print('_'*50)
        # print(f'este é o resultado:{t[0]}__________{t[1]}')
        # print('_'*50)
        a = 0
    DATABASE_REMITENTE.commit()
    DATABASE_REMITENTE.close()


  
  
    # fim da segunda fase

@io.on('apagar_sms')
def apagar_sms(data):
    nome_remitente = data['nome_remitente']
    # print(nome_remitente)
    DATABASE = sqlite3.connect(f'{nome_remitente}_SMS')
    cursor = DATABASE.cursor()
    cursor.execute(f'''delete from {nome_remitente}_sms;''')
    print('banco de dados deletado com sucesso!')
    DATABASE.commit()
    DATABASE.close()


# inicio da formatação a editação da imagem da foto de perfil do usurio

@app.route('/editar_imagem', methods = ['POST'])
def editar_imagem():
    # nome = request.form.get('nome')
    # print(f'este é o meu nome:{nome}')
    nome_da_imagem_para_editar = request.files.get('editar_imagem')
    nome = request.form.get('nome')
    novo_nome_da_foto_para_editar = nome_da_imagem_para_editar.filename.replace(f'{'-'}',f'_')
    # print(novo_nome_da_foto_para_editar)
    nome_da_imagem_para_editar.save(os.path.join('static/arquivo_usuario',novo_nome_da_foto_para_editar))
    banco = sqlite3.connect('Learn_width_Me')
    cursor = banco.cursor()
    cursor.execute('''update usuario set foto = ?  where nome = ?''',(novo_nome_da_foto_para_editar, nome))
    print('dados editados com sucesso!')
    banco.commit()
    banco.close()

    

    print('_'*50)
    return render_template('index.html')

@app.route('/editar_nome' , methods=['POST'])
def editar_nome():
    nome_actual = request.form.get('nome')
    novo_nome = request.form.get('nome2')
    banco = sqlite3.connect('Learn_width_Me')
    cursor = banco.cursor()
    cursor.execute('''update usuario set nome = ?  where nome = ?''',(novo_nome,nome_actual))
    print('dados editados com sucesso!')
    banco.commit()
    banco.close()
    return render_template('index.html')

@io.on('visto')
def visto(data):
    nome_remitente = data.get('nome_remitente')
    nome_destinatario = data.get('nome_destinatario')
    # print(f'usuario_actual:{nome_remitente}: destinatario:{nome_destinatario}')
    DATABASE_REMITENTE = sqlite3.connect(f'{nome_remitente}_FRIEND')
    CURSOR_REMITENTE = DATABASE_REMITENTE.cursor()
    CURSOR_REMITENTE.execute(f'''create table if not exists {nome_remitente}_tabela_conversa(
                                     
                             id integer primary key,
                             nome_destinatario char(45),
                             nome_sala char(45),
                             foto char(100),
                             menssagem char(45)
                                     
                                     )''')
    CURSOR_REMITENTE.execute(f'''update {nome_remitente}_tabela_conversa set menssagem = ? where nome_destinatario = ?''',("None",nome_destinatario))
    lista = CURSOR_REMITENTE.execute(f'''select nome_destinatario , menssagem from {nome_remitente}_tabela_conversa;''')
    obter = lista.fetchall()
    for t in obter:
        # print('_'*50)
        # print(f'este é o resultado:{t[0]}__________{t[1]}')
        # print('_'*50)
        a = 0
    DATABASE_REMITENTE.commit()
    DATABASE_REMITENTE.close()

@io.on('menssagem_em_tempo_real')
def menssagem_em_tempo_real(data):
    nome_remitente = data.get('nome_remitente')
    nome_destinatario = data.get('nome_destinatario')
    menssagem_do_usuario = data.get('message')
    
    # print(nome_remitente,nome_destinatario,menssagem_do_usuario,':feito avelino!')
    sid_destinatario = None
    

    for sid_conectado, info in usuarios_conectados.items():
        if info['nome'] == nome_destinatario:
            sid_destinatario = sid_conectado
            break
    if sid_destinatario:
        emit('Nova_menssagem_para_o_destinatario', {'nome_remitente': nome_remitente,'nova_menssagem':menssagem_do_usuario}, to=sid_destinatario )
        emit('ola',{'nome_remitente':nome_remitente,'menssagem':menssagem_do_usuario},to=sid_destinatario)
        print(f"menssagem enviada enviada para o SID: {sid_destinatario}")
    else:
        print(f"Usuário destinatário '{nome_destinatario}' não encontrado ou não conectado.")

@io.on('denuncia')
def denuncia(data):
    sujeito = data.get('sujeito')
    descrição = data.get('descricao')
    remitente = data.get('remitente')
    database = sqlite3.connect('DENUNCIAS')
    cursor = database.cursor()
    cursor.execute('''create table if not exists denuncia(
                   id integer primary key,
                   sujeito char(45),
                   remitente char(45),
                   descricao char(100)
                   )''')
    cursor.execute('''insert into denuncia(sujeito, remitente, descricao) values(?,?,?)''',(sujeito,remitente,descrição))
    lista = cursor.execute('''select sujeito , remitente , descricao from denuncia order by id asc;''')
    obter = lista.fetchall()
    for x in obter:
        # print('__'*40)
        # print(f'remitente:{x[1]} sujeito:{x[0]}  descrição:{x[2]}')
        # print('__'*40)
        a = 0
    database.commit()
    database.close()


@io.on('melhor')
def melhor(data):
    nome_remitente = data.get('nome_remitente')
    texto = data.get('texto')
    # print(f'remitente:{nome_remitente}  texto:{texto}')
    DATABASE = sqlite3.connect('melhor')
    cursor = DATABASE.cursor()
    cursor.execute('''create table if not exists melhor(
                   
                   id integer primary key,
                   nome_remitente char(45),
                   texto char(500)
                   
                   )''')
    cursor.execute('''insert into melhor(nome_remitente,texto) values(?,?)''',(nome_remitente,texto))
    lista = cursor.execute('''select nome_remitente , texto from melhor order by id asc;''')
    obter = lista.fetchall()
    for x in obter:
        # print('__'*50)
        # print(f'Nome_remitente:{x[0]}  comentario_remitente:{x[1]}')
        # print('__'*50)
        a = 0
    DATABASE.commit()
    DATABASE.close()


# @io.on('set_sala_ativa')
# def set_sala_ativa(data):
#     sid = request.sid # O SID do cliente que enviou esta mensagem
#     nome_da_sala_foco = data.get('sala')
#     usuario_sala_ativa[sid] = nome_da_sala_foco
#     print(f"SID {sid} agora está focado na sala: {nome_da_sala_foco}")


@io.on('grupo')
def grupo(data):
    nome_remitente = data.get('remitente')
    menssagem_usuario = data.get('menssagem')
    nome_da_sala = data.get('sala_do_grupo')
    novo_nome_da_sala = nome_da_sala
    nome_da_sala_db = sqlite3.connect(f'{nome_da_sala}_banco_de_dados')
    cursor_nome_da_sala = nome_da_sala_db.cursor()
    lista = cursor_nome_da_sala.execute(f'''select nome from {nome_da_sala} order by id asc;''')
    obter = lista.fetchall()
    dados_menssagem = sqlite3.connect(f'{nome_da_sala}_mensagem_grupo')
    dados_menssagem_cursor = dados_menssagem.cursor()
    dados_menssagem_cursor.execute(f'''create table if not exists {nome_da_sala}_mensagem_grupo(
                                   
                                   id integer primary key,
                                   nome char(100),
                                   menssagem char(1000),
                                   sala char(45),
                                   caso char(45)
                                   



                                   )''')
    dados_menssagem_cursor.execute(f'''insert into {nome_da_sala}_mensagem_grupo(nome , menssagem , sala) values (?,?,?)''',(nome_remitente , menssagem_usuario , nome_da_sala))
    Lista = dados_menssagem_cursor.execute(f'''select nome , menssagem , sala from {nome_da_sala}_mensagem_grupo order by id asc;''')
    dados_menssagem.commit()
    dados_menssagem.close() 
        

  
    

    
   
    # sid_destinatario = None
    for sid_conectado, info in usuarios_conectados.items():
        for v in obter:
                print('novo usuario:',info['nome'])
                if info['nome'] == v[0]:
        
                    sid_destinatario = sid_conectado
                        

                    if sid_destinatario:
                            print(f'este é o seu ID:{sid_conectado}')
                            emit('getMenssageGupo', {'nome_destinatario': nome_remitente , 'menssagem':menssagem_usuario , 'nome_da_sala':nome_da_sala}, to=sid_destinatario )
                            print(f"Notificação enviada para o SID: {sid_destinatario}")
                            break

                else:
                        print('não esta a funcionar!')
 
    nome_da_sala_db.commit()
    nome_da_sala_db.close()

@io.on('gerar_codigo')
def gerar_codigo(data):
    nome_usuario = data.get('nome_usuario')
    nome_da_sala = data.get('nome_da_sala')
    usuario_codigo = sqlite3.connect(f'{nome_da_sala}_banco_de_dados')
    cursor = usuario_codigo.cursor()
    Lista = cursor.execute(f'''select administrador from {nome_da_sala};''')
    obter = Lista.fetchall()
    for t in obter:
        # print('_'*100)
        # print(t[0])
        # print('_'*100)
        if t[0] == nome_usuario:
            meu_codigo = random.randint(0 , 99999)
            codigo = sqlite3.connect(f'{nome_usuario}_codigo_gerado')
            cursor_codigo = codigo.cursor()
            cursor_codigo.execute(f'''create table if not exists {nome_usuario}_codigo_gerado(
                                  
                                  id integer primary key,
                                  nome char(100),
                                  codigo char(100),
                                  outro char(100)

                                  )''')
            cursor_codigo.execute(f'''insert into {nome_usuario}_codigo_gerado(nome,codigo) values(?,?)''',(nome_usuario,meu_codigo))
            Lista_codigo = cursor_codigo.execute(f'''select codigo from {nome_usuario}_codigo_gerado order by id asc;''')
            Obter_Litsta = Lista_codigo.fetchall()
            for v in Obter_Litsta:
                # print('*'*30)
                # print(v[0])
                # print('*'*30)
                a = 0

            
            

            
            codigo.commit()
            codigo.close()
            print('resultou Cláudio Avelino!')
            
    usuario_codigo.commit()
    usuario_codigo.close()

@io.on('Verificar_Codigo')
def Verificar_Codigo(data):
        nome_do_formador = data.get('nome_do_formador')
        nome_do_usuario = data.get('nome_do_usuario')
        codigo_digitado_pelo_usuario = data.get('codigo_digitado_pelo_usuario')
        codigo = sqlite3.connect(f'{nome_do_formador}_codigo_gerado')
        cursor_codigo = codigo.cursor()
        lista_cursor_codigo = cursor_codigo.execute(f'''select codigo from {nome_do_formador}_codigo_gerado order by id asc;''')
        obter_lista_cursor_codigo = lista_cursor_codigo.fetchall()
        for r in obter_lista_cursor_codigo:
            print('--'*40)
            print(r[0])
            print('--'*40)
            if r[0] == codigo_digitado_pelo_usuario:
                #  'delete from {nome_remitente}_tabela_conversa where nome_destinatario=?''',(nome_destinatario_deletar,
                 codigo = sqlite3.connect(f'{nome_do_formador}_codigo_gerado')
                 cursor_codigo = codigo.cursor()
                 lista_cursor_codigo = cursor_codigo.execute(f'''delete from {nome_do_formador}_codigo_gerado where codigo=?''',(codigo_digitado_pelo_usuario,))

                 
                 sid_destinatario = None
                 confirmação = 'Aprovado'
    

                 for sid_conectado, info in usuarios_conectados.items():
                    if info['nome'] == nome_do_usuario:
                        sid_destinatario = sid_conectado
                        break
                 if sid_destinatario:
                    confirmação = 'Aprovado'
                    emit('Nova_menssagem_para_o_destinatario', {'nome_remitente': nome_do_usuario,'nova_menssagem':nome_do_usuario}, to=sid_destinatario )
                    emit('codigo_verificado',{'nome_remitente':nome_do_usuario,'menssagem':confirmação},to=sid_destinatario)
                    emit('codigos',{'nome_remitente':nome_do_usuario,'menssagem':confirmação},to=sid_destinatario)
                    print(f"menssagem enviada enviada para o SID: {sid_destinatario}")
            
            else:
                print(f"Usuário destinatário '{nome_do_usuario}' não encontrado ou não conectado.")
              

        codigo.commit()
        codigo.close()



    








# inicio da formtação da chamada em tempo real

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura o CORS. Em produção, restrinja 'origins' ao seu domínio.
CORS(app, origins=["http://127.0.0.1:5000", "http://localhost:5000"]) # Permite acesso do próprio servidor Flask

# Obtenha as credenciais Twilio das variáveis de ambiente
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_API_KEY_SID = os.environ.get('TWILIO_API_KEY_SID')
TWILIO_API_KEY_SECRET = os.environ.get('TWILIO_API_KEY_SECRET')

# Rota para servir a página HTML principal
@app.route('/transmitir')
def Tempo_real():
    return render_template('transmitir.html')

# Rota para gerar e retornar o Twilio Access Token
@app.route('/token', methods=['GET'])
def get_token():
    # Obtém a identidade do usuário e o nome da sala dos parâmetros da query
    identity = request.args.get('identity', f'user-{os.urandom(8).hex()}')
    room_name = request.args.get('roomName', 'default-room')

    # Verifica se as credenciais Twilio estão configuradas
    if not all([TWILIO_ACCOUNT_SID, TWILIO_API_KEY_SID, TWILIO_API_KEY_SECRET]):
        return jsonify({"error": "Twilio credentials not set in environment variables. Please check your .env file."}), 500

    # Cria um Access Token Twilio
    token = AccessToken(
        TWILIO_ACCOUNT_SID,
        TWILIO_API_KEY_SID,
        TWILIO_API_KEY_SECRET,
        identity=identity
    )

    # Adiciona um Video Grant ao token, especificando a sala
    video_grant = VideoGrant(room=room_name)
    token.add_grant(video_grant)

    # Retorna o token JWT e a identidade do usuário em formato JSON
    return jsonify({
        'identity': identity,
     'token': token.to_jwt() # Remova o .decode('utf-8')
    })


if __name__ in '__main__':
    io.run(app, debug=True, host='0.0.0.0', port=5000)


# Z8NBUVXQJ3WRRAJ9RG1QKW3R