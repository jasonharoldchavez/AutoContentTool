class Settings:
    """
    Application-wide configuration settings.
    Extend this with API keys, model paths, flags, etc.
    """
    APP_NAME: str = "AutoContentTool"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

settings = Settings()
