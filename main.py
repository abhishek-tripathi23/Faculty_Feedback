import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QApplication, QComboBox, QScrollArea, QMessageBox, QHBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton, QFormLayout, QLabel, QLineEdit, QRadioButton, QDialog)


def errorMessage(message):
    msg = QMessageBox()
    msg.setGeometry(300, 300, 300, 500)
    msg.setText(message)
    msg.setWindowTitle("WARNING")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()


class Authentication(QWidget):

    def __init__(self):
        super().__init__()

        vbox = QFormLayout()
        user_name = QLabel("Username")
        self.user = QLineEdit()
        passw = QLabel("Password")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(lambda: self.authenticate())
        vbox.addRow(user_name, self.user)
        vbox.addRow(passw, self.password)
        vbox.addRow(self.submit_button)
        self.setLayout(vbox)
        self.submit_button.keyPressEvent = self.keyPressEvent
        self.setWindowTitle("Authentication")

    def keyPressEvent(self, e):
        # Enter Key
        if e.key() == 16777220:
            self.authenticate()

    def authenticate(self):
        if self.password.text() == "tripathi" and self.user.text() == "abhishek":
            print("Successfully verified")
        else:
            errorMessage("Username and password doesn't match")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Authentication()

    # Top, left, width, height
    a.setGeometry(300, 300, 300, 100)

    # Icon
    a.setWindowIcon(QIcon('icon.png'))

    a.show()
    sys.exit(app.exec_())
