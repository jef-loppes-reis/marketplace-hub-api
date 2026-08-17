from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuracoes gerais da aplicacao

    Parameters
    ----------
    BaseSettings : _type_
        _description_
    """    

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:meupg1433@localhost:5432/marketplacehubapi'

    model_config = SettingsConfigDict(
        case_sensitive = True
    )


settings: Settings = Settings()
