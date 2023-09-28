#!/usr/bin/env python3
import appdirs

import src.steam.ui as steam_ui

from src.config import LoadConfig, Config
from src.steam.steam import Steam, GAME_INSURGENCY, GAME_CS2
from src.common import UpdateConfig

from src.games.sandstorm.sandstorm import Insurgency
from src.games.cs2.cs2 import Csgo

# app initial setup
app_dir = appdirs.user_config_dir(
    appname="linkup", 
    appauthor="com.github.jakestanley")
steam = Steam(app_dir)
selected_game = steam_ui.UpdateGames(steam)

config: Config = LoadConfig()
config: Config = UpdateConfig(config)
config.Save()

# TODO: consider a "game manager" class
if selected_game == GAME_INSURGENCY.appId:
    Insurgency(config, steam.games_dir)
elif selected_game == GAME_CS2.appId:
    Csgo(config, steam.games_dir)

print("Completed")
