import os
import subprocess
import random

from src.config import Config
from src.games.cs2.options import GameTypeMode, CsgoOptions
from src.games.cs2.ui import GetCs2Options

# Game Types: https://totalcsgo.com/commands/gametype
GAME_TYPES = {
    "Casual": GameTypeMode("Casual", 0, 0, ["mg_hostage", "mg_dust"], "cs_office"),
    "GunGame": GameTypeMode("GunGame", 1, 0, ["mg_armsrace"], "ar_shoots"),
    "Deathmatch": GameTypeMode("Deathmatch", 1, 2, ["mg_armsrace", "mg_dust", "mg_hostage"], "de_dust")
}

# TODO: game superclass
def Csgo(config: Config, games_dir: str):
    opts: CsgoOptions = GetCs2Options(GAME_TYPES)

    csgo_dir = os.path.join(games_dir, "csgo")
    # TODO set autoexec values
    autoexec_path = os.path.join(csgo_dir, "csgo", "cfg", "autoexec.cfg")

    binpath = os.path.join(csgo_dir, "srcds.exe")
    
    # what about flying scoutsman
    command = [binpath, "-game", "csgo", "-console", "-usercon", 
               "+game_type", str(opts.gtm.type), 
               "+game_mode", str(opts.gtm.mode), 
               "+mapgroup", random.choice(opts.gtm.map_groups), 
               "+map", opts.gtm.start_map]
    print(command)

    # TODO RCON gui
    # server monitor/rcon gui should allow quick switching
    # allow voting

    # known good command
    # command = [binpath, "-game", "csgo", "-console", "-usercon", "+game_type", "1", "+game_mode", "2", "+mapgroup", "mg_allclassic", "+map de_dust"]
    subprocess.call(command, cwd=csgo_dir, shell=True, stderr=subprocess.STDOUT)

if __name__ == "__main__":
    Csgo(None, "C:\\Users\\mail\\AppData\\Local\\com.github.jakestanley\\linkup\\games\\")