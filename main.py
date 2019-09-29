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

        # Form instantiation
        self.form = Form()
        self.form.setFixedSize(420, 270)
        self.form.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle("Authentication")

    def keyPressEvent(self, e):
        # Enter Key
        if e.key() == 16777220:
            self.authenticate()

    def authenticate(self):
        if self.password.text() == "tripathi" and self.user.text() == "abhishek":
            self.hide()
            self.form.show()
        else:
            errorMessage("Username and password doesn't match")


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        layout = QGridLayout()

        teacher_name = QLabel("Select teacher name from the drop down menu")
        self.cb = QComboBox()
        self.cb.addItems(["Abhishek", "Akshat", "Himanshu", "Aakash"])
        layout.addWidget(teacher_name)
        layout.addWidget(self.cb)

        groupbox1 = QGroupBox("The syllabus is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option11 = QRadioButton("Related to your course")
        self.option12 = QRadioButton("Not Related to course")
        self.option13 = QRadioButton("Somewhat close to course")
        self.option14 = QRadioButton("Don't know")
        hbox1.addWidget(self.option11)
        hbox1.addWidget(self.option12)
        hbox2.addWidget(self.option13)
        hbox2.addWidget(self.option14)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox1.setLayout(vbox)
        layout.addWidget(groupbox1)

        groupbox2 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option21 = QRadioButton("Appropriate")
        self.option22 = QRadioButton("Not appropriate")
        self.option23 = QRadioButton("Somewhat apt")
        self.option24 = QRadioButton("Don't know")
        hbox1.addWidget(self.option21)
        hbox1.addWidget(self.option22)
        hbox2.addWidget(self.option23)
        hbox2.addWidget(self.option24)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox2.setLayout(vbox)
        layout.addWidget(groupbox2)

        self.setLayout(layout)
        self.setWindowTitle("Feedback Form")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = Authentication()

    # Top, left, width, height
    start.setGeometry(300, 300, 300, 100)

    # Icon
    start.setWindowIcon(QIcon('icon.png'))

    start.show()
    sys.exit(app.exec_())
