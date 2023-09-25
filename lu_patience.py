import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, \
    QProgressBar

class PatienceDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(PatienceDialog, self).__init__(parent)

        self.setWindowTitle("Please wait")

        layout: QVBoxLayout = QVBoxLayout(self)

        label = QLabel("Please wait while the game installs or validates...")
        layout.addWidget(label)

        spinner: QProgressBar = QProgressBar(self)
        spinner.setRange(0, 0)  # Set the range to continuous (indeterminate)
        spinner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(spinner)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    PatienceDialog().exec()
