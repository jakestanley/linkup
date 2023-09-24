import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QGroupBox, \
    QRadioButton, QDialogButtonBox, QComboBox
from lu_insurgency_constants import maps, map_aliases, teams

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
        self.team = None
        for button in self.radio_buttons:
            if button.isChecked():
                self.team = button.text()
                return
                

        
    def create_teams_groupbox(self):
        groupbox_modes = QGroupBox("Team")
        layout = QVBoxLayout()

        self.radio_buttons = []
        for team in teams:
            radio = QRadioButton(team, self)
            radio.toggled.connect(self.set_team)
            self.radio_buttons.append(radio)
            layout.addWidget(radio)

        self.radio_buttons[0].setChecked(True)

        groupbox_modes.setLayout(layout)
        return groupbox_modes
    

    def create_maps_combobox(self):

        combobox = QComboBox()

        for map in maps:
            combobox.addItem(map)

        return combobox
