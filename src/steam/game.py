class Game:
    def __init__(self, name, appId, steamcmd) -> None:
        self.name = name
        self.appId = appId
        self.steamcmd = steamcmd
        self.installed = False
        self.path = ""