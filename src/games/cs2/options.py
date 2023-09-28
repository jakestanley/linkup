from typing import List

class GameTypeMode:
    def __init__(self, name: str, type: int, mode: int, map_groups: List[str], start_map: str):
        self.name = name
        self.type = type
        self.mode = mode
        self.map_groups = map_groups
        self.start_map = start_map

class CsgoOptions:
    def __init__(self) -> None:
        self.gtm: GameTypeMode = None
