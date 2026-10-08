from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "FikriUsta API"

    APP_DESCRIPTION: str = (
        "Koltuk Yıkama ve İlaçlama Sipariş Yönetim Sistemi"
    )

    VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///database/siparis.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()