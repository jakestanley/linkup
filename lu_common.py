import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, \
    QLineEdit, QDialogButtonBox
from lu_config import Config


class CommonDialog(QDialog):
    def __init__(self, config: Config, parent=None) -> None:
        super(CommonDialog, self).__init__(parent)

        self.setWindowTitle("Options")

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.addWidget(QLabel("Enter Server IP"))
        self.host_ip = QLineEdit(self)
        self.host_ip.setText(config.host_ip)
        layout.addWidget(self.host_ip)

        layout.addWidget(QLabel("RCON password"))
        self.rcon_password = QLineEdit(self)
        self.rcon_password.setText(config.rcon_password)
        layout.addWidget(self.rcon_password)

        # confirm or close
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

def UpdateConfig(config: Config):
    app = QApplication([])

    dialog = CommonDialog(config)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        config.host_ip = dialog.host_ip.text()
        config.rcon_password = dialog.rcon_password.text()
        return config
    else:
        sys.exit(0)

if __name__ == "__main__":
    UpdateConfig(Config())
