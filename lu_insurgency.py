import os
import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QDialog
from configparser import ConfigParser

from lu_config import Config
from lu_insurgency_ui import InsurgencyDialog
from lu_insurgency_constants import map_aliases

class InsurgencyOptions:
    def __init__(self, map: str, team: str) -> None:
        self.map = map_aliases[map]
        self.scenario = GetScenario(map, team)

def GetScenario(map: str, team: str):
    return f"Scenario_{map}_Checkpoint_{team}"

def OpenInsurgencyDialog():
    app = QApplication([])

    dialog = InsurgencyDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        return InsurgencyOptions(dialog.maps_combobox.currentText(), dialog.team)
    else:
        sys.exit(0)

def Insurgency(config: Config, games_dir: str):
    opts: InsurgencyOptions = OpenInsurgencyDialog()

    # https://mod.io/g/insurgencysandstorm/r/server-admin-guide
    server_config_path=os.path.join(games_dir, "insurgency", "Insurgency", "Saved", "Config", "WindowsServer")
    os.makedirs(name=server_config_path, exist_ok=True)

    iniparser = ConfigParser()
    game_ini_path = os.path.join(server_config_path, "Game.ini")
    # game_ini = config.read(game_ini_path)
    iniparser.add_section('/script/insurgency.inscoopmode')
    iniparser['/script/insurgency.inscoopmode']['bBots'] = 'True'
    iniparser['/script/insurgency.inscoopmode']['FriendlyBotQuota'] = '4'

    with open(game_ini_path, 'w') as configfile:
        iniparser.write(configfile)

    binpath = os.path.join(games_dir, "insurgency", "InsurgencyServer.exe")
    # Steam appears to be required, but clashes with regular Steam. `-multihome` (host binding) appears to alleviate this
    command = f"{binpath} {opts.map}?Scenario={opts.scenario}?MaxPlayers=28 -log -NoEAC -multihome={config.host_ip} -motd=BALLS -Rcon -RconPassword={config.rcon_password} -RconListenPort=27015"
    # TODO use threads so UI can continue on main thread
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
