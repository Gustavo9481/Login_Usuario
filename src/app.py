from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, login_required, logout_user
from config import config
from forms import Login, Registro
from usuario import Usuario
from models import ModeloUsuario



""" ------------------------------------------------- Login_Usuario   | app """
"""
Aplicación sencilla de Login de usuario, con manejo de sesión, logout-
Creación de nuevos usuarios
Rutas restringidas o protegidas que requieren login del usuario
Base de datos MySQL
"""



# -------------- instancias principales y variables globales

app = Flask(__name__)

db = MySQL(app)

usuario_conectado = ""
usuario_actual = ""


# ---------------------------------- sistema de LoginManager
# permite el manejo de sesiónes de usuario
# login -> redirección para rutas protegidas en caso de no haber usuario logeado
# load_User -> carga instancia de usuario y lo establece como usuario logeado

login_manager_app = LoginManager(app)

login_manager_app.login_view = 'login'

@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.login_usuario(db, id)



# --------------------------------------------------------------- vista | home 󰌠
@app.route("/")
def home():

    global usuario_conectado
    global usuario_actual
    
    return render_template(
        "home.html", 
        usuario_conectado = usuario_conectado, usuario_actual = usuario_actual
    )



# -------------------------------------------------------------- vista | login 󰌠
# formulario: form -> Login
# print(f"instancia: {inst_usuario}") -> comprobación de instancia correcta
# print(f"usuario actual -------> {usuario_actual}") -> carga login_user

@app.route("/login", methods=["GET", "POST"])
def login():
    
    global usuario_conectado
    global usuario_actual

    form_Login = Login()


    if request.method == 'POST' and form_Login.validate_on_submit():
        usuario_log = form_Login.usuario.data 
        password_log = form_Login.password.data

        try:
            cursor = db.connection.cursor()

            sql = ("SELECT id, nombre, usuario, email, password " 
                    "FROM tabla_usuarios " 
                    "WHERE usuario = '{}'").format(usuario_log)

            cursor.execute(sql)
            
            data_usuario = cursor.fetchone()

            cursor.connection.commit()

            if data_usuario is not None:

                    inst_usuario = Usuario(
                        data_usuario[0],
                        data_usuario[1],
                        data_usuario[2],
                        data_usuario[3],
                        password_log
                    )

                    if Usuario.checkeo_de_password(data_usuario[4], inst_usuario.password):

                        usuario_conectado = f"{inst_usuario.nombre}"
                        usuario_actual = login_user(inst_usuario)
                        
                        return render_template(
                            "home.html", 
                            usuario_conectado = usuario_conectado,
                            usuario_actual = usuario_actual
                        )

                    else:

                        flash("Contraseña Errada", "error")
                        form_Login.usuario.data = ""
                        form_Login.password.data = ""
                        
                        return render_template(
                            "login.html", 
                            form = form_Login
                        )

            else:

                flash("Usuario no encontrado", "error")
                form_Login.usuario.data = ""
                form_Login.password.data = ""
                
                return render_template(
                    "login.html", 
                    form = form_Login
                ) 
                
        except Exception as ex:

            raise Exception(ex)


    return render_template(
        "login.html",
        form = form_Login,
        usuario_conectado = usuario_conectado,
        usuario_actual = usuario_actual
    )



# ----------------------------------------------------------- vista | registro 󰌠
# registro de nuevos usuarios

@app.route("/registro", methods=["GET", "POST"])
def registro():
    
    global usuario_conectado
    global usuario_actual

    form_Registro = Registro()


    if request.method == 'POST' and form_Registro.validate_on_submit():

        nombre = form_Registro.nombre.data
        usuario = form_Registro.usuario.data
        email = form_Registro.email.data
        password = form_Registro.password.data

        inst_usuario = Usuario(
            1, 
            nombre, 
            usuario, 
            email, 
            Usuario.generar_hash(password)
        )
        
        usuario_conectado = inst_usuario.nombre
        usuario_actual = login_user(inst_usuario)
        print(inst_usuario)
        ModeloUsuario.crear_nuevo_usuario(db, inst_usuario)

        return render_template("home.html", usuario_actual=usuario_actual, usuario_conectado=usuario_conectado )   

    else:
        render_template(
            "registro.html",
            form = form_Registro
        )


    return render_template(
        "registro.html",
        form = form_Registro
    )



# -------------------------------------------------------- vista | restringido 󰌠
# ruta protegida, login requerido obligatoriamente

@app.route("/restringido")
@login_required
def restringido():
    
    global usuario_conectado
    global usuario_actual
    
    return render_template(
        "restringido.html",
        usuario_conectado = usuario_conectado,
        usuario_actual = usuario_actual
    )



# ------------------------------------------------------------- vista | logout 󰌠

@app.route("/logout")
def logout():

    global usuario_conectado
    global usuario_actual
    
    logout_user()
    
    usuario_conectado = ""
    usuario_actual = ""
    
    return redirect( url_for("home") )





if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
