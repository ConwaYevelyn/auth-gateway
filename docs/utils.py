import os
import time
from typing import Dict

class Utils:
    @staticmethod
    def get_current_timestamp():
        return int(time.time())

    @staticmethod
    def get_user_agent() -> Dict[str, str]:
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3"
        }

    @staticmethod
    def get_project_path() -> str:
        return os.path.dirname(os.path.abspath(__file__))