import os
from dotenv import load_dotenv



""" ---------------------------------------------- Login_Usuario   | config """
# El presente archivo debe ser incluido en el gitignore por seguridad

load_dotenv()

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")

#SECRET_KEY = "guscode_8425321992314480191"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")


config = {
    "development": DevelopmentConfig
}


clave = DevelopmentConfig()


print(clave.MYSQL_PASSWORD)
