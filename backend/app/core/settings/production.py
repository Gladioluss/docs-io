from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):

    title: str = "Prod Docs-io app"

    class Config(AppSettings.Config):
        env_file = ".env"
