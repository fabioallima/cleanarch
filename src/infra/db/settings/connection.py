import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            os.getenv('DB_DRIVER', 'mysql+pymysql'),
            os.getenv('DB_USER', 'cleanarch_user'),
            os.getenv('DB_PASSWORD', '123456'),
            os.getenv('DB_HOST', 'localhost'),
            os.getenv('DB_PORT', '3307'),
            os.getenv('DB_NAME', 'clean_database')
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
