import os
import subprocess

from lu_config import Config

# Game Types: https://totalcsgo.com/commands/gametype
# TODO: superclass
def Csgo(config: Config, games_dir: str):

    csgo_dir = os.path.join(games_dir, "csgo")
    # TODO set autoexec values
    autoexec_path = os.path.join(csgo_dir, "csgo", "cfg", "autoexec.cfg")

    binpath = os.path.join(csgo_dir, "srcds.exe")
    command = [binpath, "-game", "csgo", "-console", "-usercon", "+game_type", "1", "+game_mode", "2", "+mapgroup", "mg_allclassic", "+map de_dust"]

    # TODO RCON gui
    subprocess.call(command, cwd=csgo_dir, shell=True, stderr=subprocess.STDOUT)

if __name__ == "__main__":
    Csgo(None, "C:\\Users\\mail\\AppData\\Local\\com.github.jakestanley\\linkup\\games\\")