from os.path import join, dirname
from dotenv import load_dotenv


def load_env(dotenv_path: str = None) -> bool:
    if dotenv_path is None:
        dotenv_path = join(dirname(__file__), '.env')
    return load_dotenv(dotenv_path, override=False)
