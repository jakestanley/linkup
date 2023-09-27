import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QRadioButton, QDialogButtonBox, QLabel
from typing import List

from src.games.csgo.options import CsgoOptions

class CsgoDialog(QDialog):
    def __init__(self, game_types: List[str], parent=None) -> None:
        super(CsgoDialog, self).__init__(parent)

        self.setWindowTitle("CSGO")

        layout: QVBoxLayout = QVBoxLayout(self)
        

        self.radio_buttons = []
        for gt in game_types:
            radio = QRadioButton(gt, self)
            self.radio_buttons.append(radio)
            layout.addWidget(radio)

        self.radio_buttons[0].setChecked(True)

        warning = QLabel("If you want to play on this machine, please launch CSGO before clicking OK!")
        warning.setWordWrap(True)
        layout.addWidget(warning)

        # confirm or close
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

def GetCsgoOptions(game_types: dict):
    app = QApplication([])

    dialog = CsgoDialog(game_types.keys())
    if dialog.exec() == QDialog.DialogCode.Accepted:
        opts: CsgoOptions = CsgoOptions()
        for radio in dialog.radio_buttons:
            if radio.isChecked():
                opts.gtm = game_types[radio.text()]
                break
        return opts

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CsgoDialog(["a", "b", "c"])
    if dialog.exec() == QDialog.DialogCode.Accepted:
        for radio in dialog.radio_buttons:
            if radio.isChecked():
                continue
    else:
        print("closed")
