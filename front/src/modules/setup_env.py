import os

from dotenv import load_dotenv

load_dotenv()


class _SetupEnv:
    def init_settings(self):
        try:
            self.LOGS_PATH: str = os.environ["LOGS_PATH"]
        except KeyError as e:
            raise ValueError(f"Missing key in env file: {e}")
        return self


env = None


def get_env_instance():
    global env
    if env is None:
        env = _SetupEnv().init_settings()
    return env
