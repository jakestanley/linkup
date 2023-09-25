#!/usr/bin/env python3
import os
import appdirs
import subprocess

from lu_config import LoadConfig, Config
from lu_steam import Steam, GAME_INSURGENCY
import lu_steam_ui as steam_ui
from lu_common import UpdateConfig

from lu_insurgency import Insurgency

# app initial setup
app_dir = appdirs.user_config_dir(appname="linkup", appauthor="com.github.jakestanley")
steam = Steam(app_dir)
selected_game = steam_ui.UpdateGames(steam)

config: Config = LoadConfig()
config: Config = UpdateConfig(config)
config.Save()

# TODO: consider a "game manager" class
if selected_game == GAME_INSURGENCY.appId:
    Insurgency(config, steam.games_dir)

print("Completed")
