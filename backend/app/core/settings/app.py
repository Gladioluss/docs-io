from typing import Any

from pydantic import AnyHttpUrl, PostgresDsn, field_validator, ValidationInfo

from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    API_PREFIX: str = "/api"
    API_TITLE: str
    APP_PORT: int | str
    CORS_ORIGINS: list[str] | list[AnyHttpUrl]

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int | str
    DATABASE_NAME: str

    DB_POOL_SIZE: int = 90
    ASYNC_DATABASE_URI: PostgresDsn | None = None

    SECRET_KEY: bytes

    @field_validator("ASYNC_DATABASE_URI")
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> Any:

        if isinstance(v, str):
            return v
        a =PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("DATABASE_USER"),
            password=values.data.get("DATABASE_PASSWORD"),
            host=values.data.get("DATABASE_HOST"),
            port=int(values.data.get("DATABASE_PORT")),
            path=f"{values.data.get('DATABASE_NAME') or ''}",
        )
        print(values.data.get("DATABASE_HOST"))
        return a

    class Config:
        case_sensitive = True
        validate_assignment = True