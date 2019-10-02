import sys
from PyQt5.QtCore import QSize
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QWidget, QApplication, QComboBox, QScrollArea, QMessageBox, QHBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton, QFormLayout, QLabel, QLineEdit, QRadioButton, QDialog)

stylesheet_QRadioButton = 'QRadioButton{font: 14pt} QRadioButton::indicator{ width: 14px; height: 14px;}'
stylesheet_QGroupBox = 'QGroupBox{font: 16pt}'
stylesheet_QLabel = 'QLabel{font: 16pt}'
stylesheet_QComboBox = 'QComboBox{font: 16pt}'
stylesheet_QPushButton = 'QPushButton{font: 16pt Times New Roman}'

# QRadioButton.setStyleSheet(stylesheet_QRadioButton)


def errorMessage(message):
    msg = QMessageBox()
    msg.setGeometry(300, 300, 300, 500)
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("WARNING")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()


class Authentication(QWidget):

    def __init__(self, u, p):
        super().__init__()
        self.user_match = u
        self.pass_match = p
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
        # self.form.setFixedSize(420, 270)
        self.form.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle("Authentication")

    def keyPressEvent(self, e):
        # Enter Key
        if e.key() == 16777220:
            self.authenticate()

    def authenticate(self):
        # print(type(self.user_match), type(self.pass_match)
        # print(self.user.text(), self.password.text())
        if self.user.text() == self.user_match and self.password.text() == str(self.pass_match):
            self.hide()
            self.form.showMaximized()
        else:
            errorMessage("Username and password doesn't match")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        vbox = QVBoxLayout()
        admin = QPushButton("ADMINISTRATOR")
        student = QPushButton("STUDENT")
        admin.setStyleSheet(stylesheet_QPushButton)
        student.setStyleSheet(stylesheet_QPushButton)

        admin.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        student.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # self.admin_login = Authentication("admin", 123)
        # self.admin_login.setGeometry(300, 300, 350, 100)
        # admin.clicked.connect(self.authenticate)

        self.student_login = Authentication("uiet", "hacker")
        self.student_login.setGeometry(300, 300, 350, 100)
        student.clicked.connect(self.authenticate_student)

        vbox.addWidget(admin, 2)
        vbox.addWidget(student, 2)
        self.setLayout(vbox)
        self.setWindowTitle("Faculty Feedback")

    def authenticate_admin(self):
        self.admin_login.show()
        self.hide()

    def authenticate_student(self):
        self.student_login.show()
        self.hide()


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        win = QWidget()
        layout = QVBoxLayout(win)

        name_layout = QVBoxLayout()

        teacher_name = QLabel("Select teacher name from the drop down menu")
        teacher_name.setStyleSheet(stylesheet_QLabel)
        # teacher_name.setAlignment(Qt.AlignCenter)
        self.cb = QComboBox()
        self.cb.addItems(["Abhishek", "Akshat", "Himanshu", "Aakash"])
        self.cb.setStyleSheet(stylesheet_QComboBox)

        name_layout.addWidget(teacher_name)
        name_layout.addWidget(self.cb)

        name_layout.setSpacing(20)
        name_layout.setContentsMargins(0, 0, 0, 40)

        layout.addLayout(name_layout)

        groupbox_layout = QVBoxLayout()

        groupbox1 = QGroupBox("The syllabus is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option11 = QRadioButton("Related to your course")
        self.option12 = QRadioButton("Not Related to course")
        self.option13 = QRadioButton("Somewhat close to course")
        self.option14 = QRadioButton("Don't know")
        self.option11.setStyleSheet(stylesheet_QRadioButton)
        self.option12.setStyleSheet(stylesheet_QRadioButton)
        self.option13.setStyleSheet(stylesheet_QRadioButton)
        self.option14.setStyleSheet(stylesheet_QRadioButton)

        hbox1.addWidget(self.option11)
        hbox1.addWidget(self.option12)
        hbox2.addWidget(self.option13)
        hbox2.addWidget(self.option14)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # vbox.addWidget(self.option11)
        # vbox.addWidget(self.option12)
        # vbox.addWidget(self.option13)
        # vbox.addWidget(self.option14)
        groupbox1.setLayout(vbox)
        groupbox_layout.addWidget(groupbox1)

        groupbox2 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option21 = QRadioButton("Appropriate")
        self.option22 = QRadioButton("Not appropriate")
        self.option23 = QRadioButton("Somewhat apt")
        self.option24 = QRadioButton("Don't know")
        self.option21.setStyleSheet(stylesheet_QRadioButton)
        self.option22.setStyleSheet(stylesheet_QRadioButton)
        self.option23.setStyleSheet(stylesheet_QRadioButton)
        self.option24.setStyleSheet(stylesheet_QRadioButton)
        hbox1.addWidget(self.option21)
        hbox1.addWidget(self.option22)
        hbox2.addWidget(self.option23)
        hbox2.addWidget(self.option24)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        # vbox.addWidget(self.option21)
        # vbox.addWidget(self.option22)
        # vbox.addWidget(self.option23)
        # vbox.addWidget(self.option24)
        groupbox2.setLayout(vbox)
        groupbox_layout.addWidget(groupbox2)

        groupbox3 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option31 = QRadioButton("Related to your course")
        self.option32 = QRadioButton("Not Related to course")
        self.option33 = QRadioButton("Somewhat close to course")
        self.option34 = QRadioButton("Don't know")
        self.option31.setStyleSheet(stylesheet_QRadioButton)
        self.option32.setStyleSheet(stylesheet_QRadioButton)
        self.option33.setStyleSheet(stylesheet_QRadioButton)
        self.option34.setStyleSheet(stylesheet_QRadioButton)
        hbox1.addWidget(self.option31)
        hbox1.addWidget(self.option32)
        hbox2.addWidget(self.option33)
        hbox2.addWidget(self.option34)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox3.setLayout(vbox)
        groupbox_layout.addWidget(groupbox3)

        groupbox4 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option41 = QRadioButton("Related to your course")
        self.option42 = QRadioButton("Not Related to course")
        self.option43 = QRadioButton("Somewhat close to course")
        self.option44 = QRadioButton("Don't know")
        hbox1.addWidget(self.option41)
        hbox1.addWidget(self.option42)
        hbox2.addWidget(self.option43)
        hbox2.addWidget(self.option44)
        self.option41.setStyleSheet(stylesheet_QRadioButton)
        self.option42.setStyleSheet(stylesheet_QRadioButton)
        self.option43.setStyleSheet(stylesheet_QRadioButton)
        self.option44.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox4.setLayout(vbox)
        groupbox_layout.addWidget(groupbox4)

        groupbox5 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option51 = QRadioButton("Related to your course")
        self.option52 = QRadioButton("Not Related to course")
        self.option53 = QRadioButton("Somewhat close to course")
        self.option54 = QRadioButton("Don't know")
        hbox1.addWidget(self.option51)
        hbox1.addWidget(self.option52)
        hbox2.addWidget(self.option53)
        hbox2.addWidget(self.option54)
        self.option51.setStyleSheet(stylesheet_QRadioButton)
        self.option52.setStyleSheet(stylesheet_QRadioButton)
        self.option53.setStyleSheet(stylesheet_QRadioButton)
        self.option54.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox5.setLayout(vbox)
        groupbox_layout.addWidget(groupbox5)

        groupbox6 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option61 = QRadioButton("Related to your course")
        self.option62 = QRadioButton("Not Related to course")
        self.option63 = QRadioButton("Somewhat close to course")
        self.option64 = QRadioButton("Don't know")
        hbox1.addWidget(self.option61)
        hbox1.addWidget(self.option62)
        hbox2.addWidget(self.option63)
        hbox2.addWidget(self.option64)
        self.option61.setStyleSheet(stylesheet_QRadioButton)
        self.option62.setStyleSheet(stylesheet_QRadioButton)
        self.option63.setStyleSheet(stylesheet_QRadioButton)
        self.option64.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox6.setLayout(vbox)
        groupbox_layout.addWidget(groupbox6)

        groupbox7 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option71 = QRadioButton("Related to your course")
        self.option72 = QRadioButton("Not Related to course")
        self.option73 = QRadioButton("Somewhat close to course")
        self.option74 = QRadioButton("Don't know")
        hbox1.addWidget(self.option71)
        hbox1.addWidget(self.option72)
        hbox2.addWidget(self.option73)
        hbox2.addWidget(self.option74)
        self.option71.setStyleSheet(stylesheet_QRadioButton)
        self.option72.setStyleSheet(stylesheet_QRadioButton)
        self.option73.setStyleSheet(stylesheet_QRadioButton)
        self.option74.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox7.setLayout(vbox)
        groupbox_layout.addWidget(groupbox7)

        groupbox8 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option81 = QRadioButton("Related to your course")
        self.option82 = QRadioButton("Not Related to course")
        self.option83 = QRadioButton("Somewhat close to course")
        self.option84 = QRadioButton("Don't know")
        hbox1.addWidget(self.option81)
        hbox1.addWidget(self.option82)
        hbox2.addWidget(self.option83)
        hbox2.addWidget(self.option84)
        self.option81.setStyleSheet(stylesheet_QRadioButton)
        self.option82.setStyleSheet(stylesheet_QRadioButton)
        self.option83.setStyleSheet(stylesheet_QRadioButton)
        self.option84.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox8.setLayout(vbox)
        groupbox_layout.addWidget(groupbox8)

        groupbox9 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option91 = QRadioButton("Related to your course")
        self.option92 = QRadioButton("Not Related to course")
        self.option93 = QRadioButton("Somewhat close to course")
        self.option94 = QRadioButton("Don't know")
        hbox1.addWidget(self.option91)
        hbox1.addWidget(self.option92)
        hbox2.addWidget(self.option93)
        hbox2.addWidget(self.option94)
        self.option91.setStyleSheet(stylesheet_QRadioButton)
        self.option92.setStyleSheet(stylesheet_QRadioButton)
        self.option93.setStyleSheet(stylesheet_QRadioButton)
        self.option94.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox9.setLayout(vbox)
        groupbox_layout.addWidget(groupbox9)

        groupbox10 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option101 = QRadioButton("Related to your course")
        self.option102 = QRadioButton("Not Related to course")
        self.option103 = QRadioButton("Somewhat close to course")
        self.option104 = QRadioButton("Don't know")
        hbox1.addWidget(self.option101)
        hbox1.addWidget(self.option102)
        hbox2.addWidget(self.option103)
        hbox2.addWidget(self.option104)
        self.option101.setStyleSheet(stylesheet_QRadioButton)
        self.option102.setStyleSheet(stylesheet_QRadioButton)
        self.option103.setStyleSheet(stylesheet_QRadioButton)
        self.option104.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox10.setLayout(vbox)
        groupbox_layout.addWidget(groupbox10)

        groupbox11 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option111 = QRadioButton("Related to your course")
        self.option112 = QRadioButton("Not Related to course")
        self.option113 = QRadioButton("Somewhat close to course")
        self.option114 = QRadioButton("Don't know")
        hbox1.addWidget(self.option111)
        hbox1.addWidget(self.option112)
        hbox2.addWidget(self.option113)
        hbox2.addWidget(self.option114)
        self.option111.setStyleSheet(stylesheet_QRadioButton)
        self.option112.setStyleSheet(stylesheet_QRadioButton)
        self.option113.setStyleSheet(stylesheet_QRadioButton)
        self.option114.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox11.setLayout(vbox)
        groupbox_layout.addWidget(groupbox11)

        groupbox12 = QGroupBox("Content is:")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option121 = QRadioButton("Related to your course")
        self.option122 = QRadioButton("Not Related to course")
        self.option123 = QRadioButton("Somewhat close to course")
        self.option124 = QRadioButton("Don't know")
        hbox1.addWidget(self.option121)
        hbox1.addWidget(self.option122)
        hbox2.addWidget(self.option123)
        hbox2.addWidget(self.option124)
        self.option121.setStyleSheet(stylesheet_QRadioButton)
        self.option122.setStyleSheet(stylesheet_QRadioButton)
        self.option123.setStyleSheet(stylesheet_QRadioButton)
        self.option124.setStyleSheet(stylesheet_QRadioButton)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        groupbox12.setLayout(vbox)
        groupbox_layout.addWidget(groupbox12)

        groupbox_layout.setSpacing(20)
        layout.addLayout(groupbox_layout)

        groupbox1.setStyleSheet(stylesheet_QGroupBox)
        groupbox2.setStyleSheet(stylesheet_QGroupBox)
        groupbox3.setStyleSheet(stylesheet_QGroupBox)
        groupbox4.setStyleSheet(stylesheet_QGroupBox)
        groupbox5.setStyleSheet(stylesheet_QGroupBox)
        groupbox6.setStyleSheet(stylesheet_QGroupBox)
        groupbox7.setStyleSheet(stylesheet_QGroupBox)
        groupbox8.setStyleSheet(stylesheet_QGroupBox)
        groupbox9.setStyleSheet(stylesheet_QGroupBox)
        groupbox10.setStyleSheet(stylesheet_QGroupBox)
        groupbox11.setStyleSheet(stylesheet_QGroupBox)
        groupbox12.setStyleSheet(stylesheet_QGroupBox)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(win)

        layout_All = QVBoxLayout()
        layout_All.addWidget(self.scrollArea)

        # layout_All.setContentsMargins(400, 0, 400, 0)

        self.setLayout(layout_All)
        self.setWindowTitle("Feedback Form")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # start = Authentication()
    start = MainWindow()

    # Top, left, width, height
    # start.setGeometry(300, 300, 300, 100)
    start.setFixedSize(450, 300)

    # Icon
    start.setWindowIcon(QIcon('icon.png'))

    start.show()
    sys.exit(app.exec_())
