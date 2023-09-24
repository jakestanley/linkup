import os
import appdirs
import subprocess
from configparser import ConfigParser

from pysteamcmd import steamcmd

from lib.appids import AppIds

# app initial setup
app_dir = appdirs.user_config_dir(appname="linkup", appauthor="com.github.jakestanley")
app_config_path = os.path.join(app_dir, "config.json")

steamcmd_path = os.path.join(app_dir, "steamcmd")
games_path = os.path.join(app_dir, "games")
os.makedirs(steamcmd_path, exist_ok=True)

host_ip = "192.168.68.4"

cmd = steamcmd.Steamcmd(steamcmd_path)
if os.path.exists(os.path.join(steamcmd_path, "steamcmd.exe")):
    pass
else:
    cmd.install()

def install(app: str, validate: bool):
    gameserver_path = os.path.join(games_path, app)
    cmd.install_gamefiles(gameid=AppIds[app], game_install_dir=gameserver_path, user='anonymous', password=None, validate=validate)

# insurgency stuff
# https://mod.io/g/insurgencysandstorm/r/server-admin-guide
server_config_path=os.path.join(games_path, "insurgency", "Insurgency", "Saved", "Config", "WindowsServer")
config = ConfigParser()
game_ini_path = os.path.join(server_config_path, "Game.ini")
# game_ini = config.read(game_ini_path)
# config['DEFAULT']['bBots'] = 'True'
# config['DEFAULT']['FriendlyBotQuota'] = '4'

# with open(game_ini_path, 'w') as configfile:    # save
    # config.write(configfile)

map="Farmhouse"
scenario="Scenario_Farmhouse_Checkpoint_Insurgents"
rcon_password="password"

def start_insurgency():
    binpath = os.path.join(games_path, "insurgency", "InsurgencyServer.exe")
    # Steam appears to be required, but clashes with regular Steam. Multihome (host binding) appears to alleviate this
    command = f"{binpath} {map}?Scenario={scenario}?MaxPlayers=28 -log -NoEAC -multihome={host_ip} -motd=BALLS -Rcon -RconPassword={rcon_password} -RconListenPort=27015"
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# TODO if NOT verify, do not reinstall or validate. still need to install if not present
validate = False
install("Insurgency Sandstorm Dedicated Server", validate)
start_insurgency()




# start insurgency

print("OK")
