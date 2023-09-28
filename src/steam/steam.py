import os
import shutil
from typing import List

from pysteamcmd import steamcmd
from src.steam.game import Game

GAME_INSURGENCY=Game("Insurgency", 581330)
GAME_CS2=Game("Counter-Strike 2", 730)
GAMES = [GAME_INSURGENCY, GAME_CS2]

class Steam:
    def __init__(self, app_dir: str) -> None:
        self.steamcmd_dir = os.path.join(app_dir, "steamcmd")
        self.games_dir = os.path.join(app_dir, "games")
        self.cmd = self._SetupSteamCmd()

    def _SetupSteamCmd(self):

        os.makedirs(self.steamcmd_dir, exist_ok=True)
        os.makedirs(self.games_dir, exist_ok=True)

        cmd = steamcmd.Steamcmd(self.steamcmd_dir)
        # TODO make unixy
        if os.path.exists(os.path.join(self.steamcmd_dir, "steamcmd.exe")):
            pass
        else:
            cmd.install()

        return cmd

    def GetGames(self) -> List[Game]:

        for game in GAMES:
            game_dir = os.path.join(self.games_dir, game.name)
            if os.path.exists(game_dir):
                game.installed = True

        # TODO: as per convention this is intended to be static but i am not 
        #   using it as such
        return GAMES

    def InstallGame(self, game: Game, validate: bool):

        game_dir = os.path.join(self.games_dir, game.name)
        self.cmd.install_gamefiles(gameid=game.appId, game_install_dir=game_dir, user='anonymous', password=None, validate=validate)
        game.installed = True

    def UninstallGame(self, game: Game):

        game_dir = os.path.join(self.games_dir, game.name)
        shutil.rmtree(game_dir)
        game.installed = False

