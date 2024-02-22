from usuario import Usuario



""" ---------------------------------------------- Login_Usuario   | models """



class ModeloUsuario():

    # ----------------------------------------- Login de usuario
    # verifica datos del usuario y permitir el login (LoginManager)
    # parámetros:
    # cls: classmethod, uso de método sin instancia necesaria
    # db: instancia de conexión base de datos (app)
    # id: identificador de usuario

    @classmethod
    def login_usuario(cls, db, id):
             
        try:
            cursor = db.connection.cursor()

            sql = ("SELECT id, nombre, usuario, email, password " 
                    "FROM tabla_usuarios " 
                    "WHERE id = '{}'").format(id)

            cursor.execute(sql)
            
            data_usuario = cursor.fetchone()

            cursor.connection.commit()

            if data_usuario is not None:
                    inst_usuario = Usuario(
                        data_usuario[0],
                        data_usuario[1],
                        data_usuario[2],
                        data_usuario[3],
                        data_usuario[4],
                    )

                    return inst_usuario
        
        except Exception as ex:

            raise Exception(ex)



    # -------------------------------- Registro de Nuevo Usuario
    # realiza nuevo registro de los datos en la base de datos
    # parámetros:
    # cls: classmethod, uso de método sin instancia necesaria
    # db: instancia de conexión base de datos (app)
    # instancia: objeto de clase Usuario

    @classmethod
    def crear_nuevo_usuario(cls, db, instancia):
        
        try:
            cursor = db.connection.cursor()

            datos_usuario = (
                instancia.nombre, 
                instancia.usuario, 
                instancia.email, 
                instancia.password
            )

            sql_registro = ("INSERT INTO tabla_usuarios" 
                            "(nombre, usuario, email, password)" 
                            "VALUES (%s, %s, %s, %s)"
            )

            cursor.execute(sql_registro, datos_usuario)

            db.connection.commit()
                
        except Exception as ex:

            raise Exception(ex)

