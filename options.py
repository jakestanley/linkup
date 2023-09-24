import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QGroupBox, \
    QRadioButton, QDialogButtonBox, QComboBox

from insurgency import maps, teams

class InsurgencyDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(InsurgencyDialog, self).__init__(parent)

        self.setWindowTitle("Insurgency Co-op")

        # build layout
        layout: QVBoxLayout = QVBoxLayout(self)
        self.teams_group = self.create_teams_groupbox()
        layout.addWidget(self.teams_group)

        self.maps_combobox = self.create_maps_combobox()
        layout.addWidget(self.maps_combobox)

        # confirm or close
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)


    def set_team(self, team):
        self.team = team

        
    def create_teams_groupbox(self):
        groupbox_modes = QGroupBox("Team")
        layout = QVBoxLayout()

        for team in teams:
            radio = QRadioButton(team, self)
            if team == teams[1]:
                radio.setChecked(True)
                self.set_team(teams[1])
            radio.clicked.connect(lambda: self.set_team(team))
            layout.addWidget(radio)

        groupbox_modes.setLayout(layout)
        return groupbox_modes
    

    def create_maps_combobox(self):

        combobox = QComboBox()

        for map in maps:
            combobox.addItem(map)

        return combobox


def OpenInsurgencyDialog():
    app = QApplication([])

    dialog = InsurgencyDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        pass
    else:
        sys.exit(0)

if __name__ == "__main__":
    OpenInsurgencyDialog()