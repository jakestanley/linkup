import sys
from typing import List
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, \
    QLabel, QWidget, QDialogButtonBox, QPushButton, QListWidget, \
    QListWidgetItem
from lu_steam import Steam
from lu_steam_game import Game
from lu_patience import PatienceDialog

class T_Install(QThread):
    finished = pyqtSignal()

    def __init__(self, steam, game, validate):
        super().__init__()
        self.steam = steam
        self.game = game
        self.validate = validate

    def run(self):
        self.steam.InstallGame(self.game, self.validate)
        self.finished.emit()


class GameWidget(QWidget):
    def __init__(self, game: Game, steam: Steam, dialog) -> None:
        super().__init__()

        self.name = game.name
        self.game = game
        self.steam = steam
        self.dialog = dialog

        layout = QHBoxLayout()
        
        self.label_name = QLabel(self.name)
        self.label_installed = QLabel("Installed" if self.game.installed else "Not installed")
        self.add_button = QPushButton("Install")
        self.add_button.setEnabled(not self.game.installed)
        self.add_button.clicked.connect(self.install_clicked)
        self.remove_button = QPushButton("Uninstall")
        self.remove_button.setEnabled(self.game.installed)
        self.remove_button.clicked.connect(self.uninstall_clicked)
        self.validate_button = QPushButton("Validate")
        self.validate_button.setEnabled(self.game.installed)
        self.validate_button.clicked.connect(self.validate_clicked)
        self.play_button = QPushButton("Play")
        self.play_button.setEnabled(self.game.installed)
        self.play_button.clicked.connect(self.play_clicked)

        layout.addWidget(self.label_name)
        layout.addWidget(self.label_installed)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.validate_button)
        layout.addWidget(self.play_button)

        self.setLayout(layout)

    def close_please_wait(self):
        self.please_wait.accept()
        self.redraw()

    def install_clicked(self):
        self.worker_thread = T_Install(self.steam, self.game, False)
        self.worker_thread.finished.connect(self.close_please_wait)
        self.worker_thread.start()
        self.please_wait = PatienceDialog(self)
        if self.please_wait.exec() == QDialog.DialogCode.Rejected:
            # TODO: implement cancel validate
            # self.worker_thread.finished.disconnect()
            pass

    def uninstall_clicked(self):
        self.steam.UninstallGame(self.game)
        self.redraw()

    def validate_clicked(self):
        self.worker_thread = T_Install(self.steam, self.game, True)
        self.worker_thread.finished.connect(self.close_please_wait)
        self.worker_thread.start()
        self.please_wait = PatienceDialog(self)
        if self.please_wait.exec() == QDialog.DialogCode.Rejected:
            # TODO: implement cancel validate
            # self.worker_thread.finished.disconnect()
            pass

    def play_clicked(self):
        self.dialog.play_app_id = self.game.appId
        self.dialog.accept()

    def redraw(self):
        self.add_button.setEnabled(not self.game.installed)
        self.remove_button.setEnabled(self.game.installed)
        self.validate_button.setEnabled(self.game.installed)
        self.play_button.setEnabled(self.game.installed)
        self.label_installed.setText("Installed" if self.game.installed else "Not installed")
        

class SteamDialog(QDialog):
    def __init__(self, games: List[Game], steam: Steam, parent=None) -> None:
        super(SteamDialog, self).__init__(parent)
        self.setWindowTitle("Steam")

        layout: QVBoxLayout = QVBoxLayout(self)
        self.game_list_widget = QListWidget()
        layout.addWidget(self.game_list_widget)

        for game in games:
            game_widget = GameWidget(game, steam, self)
            list_item = QListWidgetItem(self.game_list_widget)
            list_item.setSizeHint(game_widget.sizeHint())
            self.game_list_widget.setItemWidget(list_item, game_widget)

        # confirm or close
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)


def UpdateGames(steam: Steam):
    app = QApplication([])
    games = steam.GetGames()

    dialog = SteamDialog(games, steam)
    dialog.setGeometry(100, 100, 640, 480)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        return dialog.play_app_id
    else:
        sys.exit(0)