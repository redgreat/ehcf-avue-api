import pathlib

from starlette.config import Config

ROOT = pathlib.Path(__file__).resolve().parent.parent  # app/
BASE_DIR = ROOT.parent  # ./

config = Config(BASE_DIR / "app/config/ehcf_api.cnf")


API_USERNAME = config("API_USERNAME", str)
API_PASSWORD = config("API_PASSWORD", str)

# Auth configs.
API_SECRET_KEY = config("API_SECRET_KEY", str)
API_ALGORITHM = config("API_ALGORITHM", str)
APP_KEY = config("APP_KEY", str)
API_ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "API_ACCESS_TOKEN_EXPIRE_MINUTES", int
)  # infinity

# Database Config
DATABASE_URL = config("DATABASE_URL", str)
DATABASE_URL_ASYNC = config("DATABASE_URL_ASYNC", str)
