from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """Configuracoes gerais da aplicacao

    Parameters
    ----------
    BaseSettings : _type_
        _description_
    """    

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:1433@localhost:5432/fastapi'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
