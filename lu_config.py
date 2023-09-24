import appdirs
import os
import json
import sys

_DEFAULT_IP = "127.0.0.1"
_KEY_HOST_IP = "host_ip"

_DEFAULT_RCON_PASSWORD = "password"
_KEY_RCON_PASSWORD = "rcon_password"

class Config:
    def __init__(self, host_ip: str = _DEFAULT_IP, rcon_password = _DEFAULT_RCON_PASSWORD) -> None:
        self.host_ip = host_ip
        self.rcon_password = rcon_password

    def Save(self):
        config_path = GetConfigPath()
        settings = {}
        settings[_KEY_HOST_IP] = self.host_ip
        settings[_KEY_RCON_PASSWORD] = self.rcon_password

        with open(config_path, "w") as config_file:
            json.dump(settings, config_file, indent=4)

def GetConfigPath() -> str:
    app_dir = appdirs.user_config_dir(appname="linkup", appauthor="com.github.jakestanley")
    config_path = os.path.join(app_dir, "config.json")
    return config_path

def LoadConfigFromJson(data):
    config: Config = Config()
    config.host_ip = data.get(_KEY_HOST_IP, _DEFAULT_IP)
    config.rcon_password = data.get(_KEY_RCON_PASSWORD, _DEFAULT_RCON_PASSWORD)
    return config

def LoadConfig():
    config_path = GetConfigPath()
    try:
        with open(config_path, "r") as config_file:
            return LoadConfigFromJson(json.load(config_file))
    except (FileNotFoundError):
        print("Warning: no configuration found. Creating a new one")
        return Config()
    except (json.JSONDecodeError):
        print("Error: Got a JSONDecodeError when loading configuration. Check or remove the file")
        sys.exit(1)