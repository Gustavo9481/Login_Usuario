from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.widgets import EmailInput
from wtforms.validators import DataRequired, Email, Length



""" ----------------------------------------------- Login_Usuario   | forms """



# --------------------------------------------------------- formulario | Login 󰌠
# vista login -> acceso de usuarios
# campos:
#   usuario: nombre de identificación interna del usuario
#   password: conttraseña del usuario
#   bt_login: botón login (submit) para enviar datos de usuario

class Login(FlaskForm):
    
    usuario = StringField(
        "usuario", validators=[DataRequired(), Length(max=20)]
    )
    
    password = PasswordField(
        "password", validators=[DataRequired()]
    )
    
    bt_login = SubmitField("Login")



# ------------------------------------------------------ formulario | Registro 󰌠
# vista registro -> registro de nuevos usuarios
# campos:
#   nombre: nombre completo del usuario
#   usuario: nombre de identificación interna del usuario
#   email: correo electrónico del usuario
#   password: conttraseña del usuario
#   bt_registro: botón registro (submit) para enviar datos de usuario

class Registro(FlaskForm):
    
    nombre = StringField(
        "nombre", validators=[DataRequired(), Length(max=50)]
    )

    usuario = StringField(
        "usuario", validators=[DataRequired(), Length(max=20)]
    )
    
    email = StringField(
        "email", validators=[DataRequired(), Email()], widget=EmailInput()
    )
    
    password = PasswordField(
        "password", validators=[DataRequired()]
    )
    
    bt_registro = SubmitField("Registro")