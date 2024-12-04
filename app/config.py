from pydantic_settings import BaseSettings 

class Settings(BaseSettings): #in it, we can list all the environment variables we set as proberties in the class
    database_hostname: str # it is written in small case, but the model take care of conversion
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()

