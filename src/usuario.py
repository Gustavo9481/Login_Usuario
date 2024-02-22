from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass



""" --------------------------------------------- Login_Usuario   | usuario """



# -------------------------------------------------------------- Clase Usuario 󰌠

@dataclass
class Usuario(UserMixin):

        id: int | None
        nombre: str | None
        usuario: str | None
        email: str | None
        password: str | None

        
        # ------------------------------------ método | generar_hash
        # toma el password literal y genera un hash de seguridad
        # cls: classmethod, uso de método sin instancia necesaria
        # password: contraseña de usuario (Usuario.password)
        
        @classmethod
        def generar_hash(cls, password):
                
                return generate_password_hash(password)
                

        # ----------------------------- método | checkeo_de_password
        # verifica la coincidencia del password literal y el hash de seguridad
        # cls: classmethod, uso de método sin instancia necesaria
        # hash_tabla: hash generado y almacenado en la base de datos
        # password: contraseña literal ingresada por el usuario en formulario Login

        @classmethod
        def checkeo_de_password(cls, hash_tabla, password):
                
                return check_password_hash(hash_tabla, password)


        # ------------------------------------------ método | get_id
        # obtiene el id del Usuario necesario para el sistema LoginManager
        
        def get_id(self) -> str:
                
                return str(self.id)
