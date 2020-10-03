import sys
import smtplib
from PyQt5.QtCore import QSize
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QWidget, QApplication, QComboBox, QScrollArea, QMessageBox, QHBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton, QFormLayout, QLabel, QLineEdit, QRadioButton, QDialog)
from firebase import firebase

stylesheet_QRadioButton = 'QRadioButton{font: 14pt} QRadioButton::indicator{ width: 14px; height: 14px;}'
stylesheet_QGroupBox = 'QGroupBox{font: 16pt}'
stylesheet_QLabel = 'QLabel{font: 16pt}'
stylesheet_QLabel1 = 'QLabel{font: 20px Times New Roman}'
stylesheet_QComboBox = 'QComboBox{font: 16pt}'
stylesheet_QPushButton = 'QPushButton{font: 16pt Times New Roman}'
stylesheet_QPushButton1 = 'QPushButton{font: 20px Times New Roman}'
stylesheet_authenticate_submit = 'QPushButton{padding: 10px}'
stylesheet_submit_button = 'QPushButton{font: 20pt Times New Roman; background-color: white;padding: 10px; border-style: outset; border-width: 2px; border-radius: 10px; border-color: black;}'
stylesheet_slider_label = 'QLabel{font: 12pt Arial }'


fire = firebase.FirebaseApplication(
    "https://faculty-3a510.firebaseio.com/", None)

answer_array = []
question_array = ["Course Content", "Relevance of the course in the overall structure of program", "Overlap with other courses",
                  "Recommended Reading material was", "Class tests/mid-semester tests were conducted", "The class tests/mid-term tests were",
                  "The teacher completes the entire syllabus in time","The teacher has subject knowledge",
                  "The teacher communicates clearly and inspires me by his/her teaching", "The teacher is punctual in the class",
                  "The teacher comes well prepared for the class", "The teacher encourage participation and discussion in the class", 
                  "The teacher uses teaching aids, handouts, gives suitable references, make presentations and conduct seminars/tutorials, etc.",
                  "The teacher's attitude towards students is friendly and helpful", "The teacher is available and accessible in the department",
                  "The evaluation process is fair and unbiased"]

option_array = [["Can be covered in one semester", "Not enough for one semester", "Too much to be adequately covered in one semester", "Difficult to comment"], ["Very relevant", "Not at all relevant", "Reasonably relevant", "Difficult to comment"], ["No overlap", "Repetition of several topics",
    "Some overlap", "Difficult to comment"], ["Adeqaute and relevant", "Mostly inadequate", "To some extent adequate and relevant", "Cannot comment"], ["As per schedule and satisfactorily", "In an unsatisfactory manner", "Never", "But were inadequate"], ["Difficult", "Balanced", "Easy", "Out of Syllabus"],
    ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"],
    ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"],
    ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"], ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"],
    ["Strongly Disagree", "Disagree", "Neither agree or disagree", "Agree", "Strongly Agree"]]


# creates SMTP session

def sendEmail(message_body, to_email):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication

        s.login("facultyfeedback.uiet@gmail.com", "uietpu2019")

        # message to be sent
        message = message_body

        # sending the mail
        s.sendmail("facultyfeedback.uiet@gmail.com",
                   to_email, message)

        # terminating the session
        s.quit()
    except:
        print("net not working")


def get_teacher_name():
    result = fire.get('/Teacher', None)
    arr = []
    for items in result.values():
        arr.append(items)
    arr.sort()
        # print(arr)
    return arr

def get_course_name():
    result = fire.get('/Course', None)
    arr = []
    for items in result.values():
        arr.append(items)
    arr.sort()
        # print(arr)
    return arr


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
        self.submit_button = QPushButton("SUBMIT")
        self.submit_button.setStyleSheet(stylesheet_authenticate_submit)
        self.submit_button.clicked.connect(lambda: self.authenticate())
        vbox.addRow(user_name, self.user)
        vbox.addRow(passw, self.password)
        vbox.addRow(self.submit_button)
        self.setLayout(vbox)
        self.submit_button.keyPressEvent = self.keyPressEvent

        # Administrator Initiation
        self.administrator = Administrator()
        self.administrator.setFixedSize(420, 270)

        # Form instantiation
        self.form = Form()
        self.form.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle("Authentication")

    def keyPressEvent(self, e):
        # Enter Key
        if e.key() == 16777220:
            self.authenticate()

    def authenticate(self):
        if self.user.text() == "admin" and self.user.text() == self.user_match and self.password.text() == str(self.pass_match):
            self.hide()
            self.administrator.show()
        elif self.user.text() == "uiet" and self.user.text() == self.user_match and self.password.text() == str(self.pass_match):
            self.hide()
            self.form.showMaximized()
        else:
            errorMessage("Username and password doesn't match")


class Consolidated_Form_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        label_teacher = QLabel("Teacher name")
        label_teacher.setStyleSheet(stylesheet_QLabel1)
        self.teacher_name = QComboBox()
        self.teacher_name.addItems(get_teacher_name())

        label_semester = QLabel("Semester")
        label_semester.setStyleSheet(stylesheet_QLabel1)
        self.semester_cb = QComboBox()
        self.semester_cb.addItems(['1', '2', '3','4','5','6','7','8'])

        label_email = QLabel("Administrator email")
        label_email.setStyleSheet(stylesheet_QLabel1)
        self.email_id = QLineEdit()

        submit_button = QPushButton("GENERATE")
        submit_button.clicked.connect(self.generate_form)
        submit_button.setStyleSheet(stylesheet_QPushButton)
        submit_button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        vbox.addWidget(label_teacher)
        vbox.addWidget(self.teacher_name)
        vbox.addWidget(label_semester)
        vbox.addWidget(self.semester_cb)
        vbox.addWidget(label_email)
        vbox.addWidget(self.email_id)
        vbox.addWidget(submit_button)

        self.setLayout(vbox)
        self.setWindowTitle("Consolidated Form")

    def generate_form(self):
        new_teacher_name = self.teacher_name.currentText().replace(".", " ")

        report = fire.get(new_teacher_name, None)
        courses_name = []
        for item in report:
            if item[3] == self.semester_cb.currentText():
                courses_name.append(item)

        feedbacks = []
        temp = []
       

        answer_array_temp = [[0 for i in range(4)] for j in range(6)] + [[0 for j in range(5)] for k in range(10)]

        for course in courses_name:
            feedback_node = new_teacher_name + '/' + course
            course_report = fire.get(feedback_node, None)
            for feedback in course_report.values():
                temp.append(feedback)
            feedbacks.append(temp)
            temp = []

        course_response_array = []
        for feedback in feedbacks:
            for response in feedback:
                for i in range(6):
                    answer_choice = response[i].index(1)
                    answer_array_temp[i][answer_choice] += 1
                for j in range(6, 16):
                    answer_choice = response[j].index(1)
                    answer_array_temp[j][answer_choice] += 1
                print()
            course_response_array.append(answer_array_temp)
            answer_array_temp = [[0 for i in range(4)] for j in range(6)] + [[0 for j in range(5)] for k in range(10)]

        print(course_response_array)

        message_header = ""
        message_body = ""
        message = ""

        print(course_response_array[0][6][3])
        print(course_response_array[0][7])
        print(course_response_array[0][15][3])
        print()
        print(len(courses_name))


        for i in range(len(courses_name)):
            message_header = "Teacher Name - " + self.teacher_name.currentText() + "\n" + "Semester - " + \
                self.semester_cb.currentText() + "\n" + "Course Name - " + courses_name[i]
            message_body = "Consolidated Form: " + "\n\n"
            for j in range(6):
                message_body += str(j+1) + ". "
                message_body += question_array[j] + "\n"
                message_body += "(a) "
                message_body += option_array[j][0] + ": " + str(course_response_array[i][j][0]) + "\n"
                message_body += "(b) "
                message_body += option_array[j][1] + ": " + str(course_response_array[i][j][1]) + "\n"
                message_body += "(c) "
                message_body += option_array[j][2] + ": " + str(course_response_array[i][j][2]) + "\n"
                message_body += "(d) "
                message_body += option_array[j][3] + ": " + str(course_response_array[i][j][3]) + "\n"
                message_body += "\n"
            for l in range(6, 16):
                message_body += str(l+1) + ". "
                message_body += question_array[l] + "\n"
                message_body += "(a) "
                message_body += option_array[l][0] + ": " + str(course_response_array[i][l][0]) + "\n"
                message_body += "(b) "
                message_body += option_array[l][1] + ": " + str(course_response_array[i][l][1]) + "\n"
                message_body += "(c) "
                message_body += option_array[l][2] + ": " + str(course_response_array[i][l][2]) + "\n"
                message_body += "(d) "
                message_body += option_array[l][3] + ": " + str(course_response_array[i][l][3]) + "\n"
                message_body += "(e) "
                message_body += option_array[l][4] + ": " + str(course_response_array[i][l][4]) + "\n"
                message_body += "\n"

            message = message_header + "\n\n" + message_body
            sendEmail(message, self.email_id.text())
            message = ""

class Administrator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        vbox = QVBoxLayout()
        course_mgmt = QPushButton("COURSE MANAGEMENT")
        teacher_mgmt = QPushButton("TEACHER MANAGEMENT")
        consolidated_form = QPushButton("CONSOLIDATED FORM")
        course_mgmt.setStyleSheet(stylesheet_QPushButton)
        teacher_mgmt.setStyleSheet(stylesheet_QPushButton)
        consolidated_form.setStyleSheet(stylesheet_QPushButton)

        course_mgmt.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        teacher_mgmt.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        consolidated_form.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.teacher_window = Teacher_Management()
        self.teacher_window.setGeometry(300, 300, 400, 100)
        teacher_mgmt.clicked.connect(self.show_teacher)

        self.consolidated_window = Consolidated_Form_Window()
        self.consolidated_window.setFixedSize(450, 250)
        consolidated_form.clicked.connect(self.show_consolidated)
        self.course_window = Course_Management()
        self.course_window.setGeometry(300, 300, 400, 100)     
        course_mgmt.clicked.connect(self.show_course)

        vbox.addWidget(course_mgmt, 2)
        vbox.addWidget(teacher_mgmt, 2)
        vbox.addWidget(consolidated_form, 2)
        self.setLayout(vbox)
        self.setWindowTitle("Administrator")

    def show_teacher(self):
        self.teacher_window.show()
        self.hide()

    def show_consolidated(self):
        self.consolidated_window.show()
        self.hide()

    def show_course(self):
        self.course_window.show()
        self.hide()


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

        self.admin_login = Authentication("admin", "hacker")
        self.admin_login.setFixedSize(350, 120)
        admin.clicked.connect(self.authenticate_admin)

        self.student_login = Authentication("uiet", "hacker")
        self.student_login.setFixedSize(350, 120)
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


class Course_Management(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        mainbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox1 = QHBoxLayout()

        label1 = QLabel("Add Course")
        label1.setStyleSheet(stylesheet_QLabel1)
        vbox1.addWidget(label1)
        self.name = QLineEdit()
        self.submit_button = QPushButton("SUBMIT")
        self.submit_button.clicked.connect(self.add_name)
        hbox1.addWidget(self.name)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.submit_button)
        vbox1.setContentsMargins(0, 0, 0,20)
        self.submit_button.setStyleSheet(stylesheet_QPushButton1)
        self.submit_button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        mainbox.addLayout(vbox1)

        label2 = QLabel("Delete Course")
        label2.setStyleSheet(stylesheet_QLabel1)
        vbox2.addWidget(label2)
        self.cb2 = self.add_combo()
        vbox2.addWidget(self.cb2)
        delete_course = QPushButton("DELETE")
        delete_course.clicked.connect(self.delete_course)
        vbox2.addWidget(delete_course)
        delete_course.setStyleSheet(stylesheet_QPushButton1)

        delete_course.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        mainbox.addLayout(vbox2)

        self.setLayout(mainbox)
        self.setWindowTitle("Course Management")

    def delete_course(self):
        name = self.cb2.currentText()
        result = fire.get('/Course', None)
        for item in result:
            if (result[item]) == name:
                term = item
                break

        fire.delete('/Course', term)

        self.hide()
        self.t = Course_Management()
        self.t.setGeometry(300, 300, 400, 100)

        self.t.show()

    def add_name(self):
        course_name = self.name.text()
        result = fire.post('/Course', course_name)
        self.hide()
        self.t = Course_Management()
        self.t.setGeometry(300, 300, 400, 100)
        self.t.show()

    def add_combo(self):
        cb = QComboBox()
        arr = get_course_name()
        cb.addItems(arr)
        return cb



class Teacher_Management(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        mainbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox1 = QHBoxLayout()

        label1 = QLabel("Add Teacher")
        label1.setStyleSheet(stylesheet_QLabel1)
        self.cb = QComboBox()
        self.cb.addItems(["Mr", "Ms"])
        vbox1.addWidget(label1)
        self.name = QLineEdit()
        self.submit_button = QPushButton("SUBMIT")
        self.submit_button.clicked.connect(self.add_name)
        hbox1.addWidget(self.cb)
        hbox1.addWidget(self.name)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.submit_button)
        vbox1.setContentsMargins(0, 0, 0,20)
        self.submit_button.setStyleSheet(stylesheet_QPushButton1)
        self.submit_button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        mainbox.addLayout(vbox1)

        label2 = QLabel("Delete Teacher")
        label2.setStyleSheet(stylesheet_QLabel1)
        vbox2.addWidget(label2)
        self.cb2 = self.add_combo()
        vbox2.addWidget(self.cb2)
        delete_teacher = QPushButton("DELETE")
        delete_teacher.clicked.connect(self.delete_teacher)
        vbox2.addWidget(delete_teacher)
        delete_teacher.setStyleSheet(stylesheet_QPushButton1)

        delete_teacher.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        mainbox.addLayout(vbox2)

        self.setLayout(mainbox)
        self.setWindowTitle("Teacher Management")

    def delete_teacher(self):
        name = self.cb2.currentText()
        result = fire.get('/Teacher', None)
        for item in result:
            if (result[item]) == name:
                term = item
                break

        fire.delete('/Teacher', term)

        self.hide()
        self.t = Teacher_Management()
        self.t.setGeometry(300, 300, 400, 100)

        self.t.show()

    def add_name(self):
        teacher_name = self.cb.currentText() + ". " + self.name.text()
        result = fire.post('/Teacher', teacher_name)
        self.hide()
        self.t = Teacher_Management()
        self.t.setGeometry(300, 300, 400, 100)
        self.t.show()

    def add_combo(self):
        cb = QComboBox()
        arr = get_teacher_name()
        cb.addItems(arr)
        return cb


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        win = QWidget()
        layout = QVBoxLayout(win)

        # Details layout

        details_layout = QVBoxLayout()

        name_layout = QVBoxLayout()

        teacher_name = QLabel("Select teacher name from the drop down menu")
        teacher_name.setStyleSheet(stylesheet_QLabel)
        self.cb = QComboBox()
        self.cb.addItems(get_teacher_name())
        self.cb.setStyleSheet(stylesheet_QComboBox)

        name_layout.addWidget(teacher_name)
        name_layout.addWidget(self.cb)

        name_layout.setSpacing(20)
        name_layout.setContentsMargins(0, 0, 0, 20)

        course_layout = QVBoxLayout()
        course_name = QLabel("Select course name from the drop down menu")
        course_name.setStyleSheet(stylesheet_QLabel)
        self.course_cb = QComboBox()
        self.course_cb.addItems(get_course_name())
        self.course_cb.setStyleSheet(stylesheet_QComboBox)

        course_layout.addWidget(course_name)
        course_layout.addWidget(self.course_cb)

        course_layout.setSpacing(20)
        course_layout.setContentsMargins(0, 0, 0, 40)

        details_layout.addLayout(name_layout)
        details_layout.addLayout(course_layout)

        layout.addLayout(details_layout)

        groupbox_layout = QVBoxLayout()

        question_1 = QLabel(
            "1. For each of the question, you are required to indicate your opinion by choosing options given below.")
        groupbox_layout.addWidget(question_1)
        question_1.setStyleSheet(stylesheet_QLabel)

        groupbox1 = QGroupBox("Course Content")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option11 = QRadioButton("Can be covered in one semester")
        self.option12 = QRadioButton("Not enough for one semester")
        self.option13 = QRadioButton(
            "Too much to be adequately covered in one semester")
        self.option14 = QRadioButton("Difficult to comment")
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
        groupbox1.setLayout(vbox)
        groupbox_layout.addWidget(groupbox1)

        groupbox2 = QGroupBox(
            "Relevance of the course in the overall structure of program")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option21 = QRadioButton("Very relevant")
        self.option22 = QRadioButton("Not at all relevant")
        self.option23 = QRadioButton("Reasonably relevant")
        self.option24 = QRadioButton("Difficult to comment")
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
        groupbox2.setLayout(vbox)
        groupbox_layout.addWidget(groupbox2)

        groupbox3 = QGroupBox("Overlap with other courses")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option31 = QRadioButton("No overlap")
        self.option32 = QRadioButton("Repetition of several topics")
        self.option33 = QRadioButton("Some overlap")
        self.option34 = QRadioButton("Difficult to comment")
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

        groupbox4 = QGroupBox("Recommended Reading material was")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option41 = QRadioButton("Adeqaute and relevant")
        self.option42 = QRadioButton("Mostly inadequate")
        self.option43 = QRadioButton("To some extent adequate and relevant")
        self.option44 = QRadioButton("Cannot comment")
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

        groupbox5 = QGroupBox("Class tests/mid-semester tests were conducted")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option51 = QRadioButton("As per schedule and satisfactorily")
        self.option52 = QRadioButton("In an unsatisfactory manner")
        self.option53 = QRadioButton("Never")
        self.option54 = QRadioButton("But were inadequate")
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

        groupbox6 = QGroupBox("The class tests/mid-term tests were")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        self.option61 = QRadioButton("Difficult")
        self.option62 = QRadioButton("Balanced")
        self.option63 = QRadioButton("Easy")
        self.option64 = QRadioButton("Out of Syllabus")
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

        question_2 = QLabel(
            "2. Using the rating scale below, please choose the best value that expresses your opinion.\n    (1-Strongly disagree, 2-disagree, 3-neither agree nor disgaree, 4-agree, 5-strognly agree)")
        groupbox_layout.addWidget(question_2)
        question_2.setStyleSheet(stylesheet_QLabel)

        groupbox7 = QGroupBox(
            "The teacher completes the entire syllabus in time")
        hbox = QHBoxLayout()
        self.option71 = QRadioButton("Strongly Disagree")
        self.option72 = QRadioButton("Disagree")
        self.option73 = QRadioButton("Neither agree or disagree")
        self.option74 = QRadioButton("Agree")
        self.option75 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option71)
        hbox.addWidget(self.option72)
        hbox.addWidget(self.option73)
        hbox.addWidget(self.option74)
        hbox.addWidget(self.option75)
        self.option71.setStyleSheet(stylesheet_QRadioButton)
        self.option72.setStyleSheet(stylesheet_QRadioButton)
        self.option73.setStyleSheet(stylesheet_QRadioButton)
        self.option74.setStyleSheet(stylesheet_QRadioButton)
        self.option75.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox7.setLayout(hbox)
        groupbox_layout.addWidget(groupbox7)

        groupbox8 = QGroupBox(
            "The teacher has subject knowledge")
        hbox = QHBoxLayout()
        self.option81 = QRadioButton("Strongly Disagree")
        self.option82 = QRadioButton("Disagree")
        self.option83 = QRadioButton("Neither agree or disagree")
        self.option84 = QRadioButton("Agree")
        self.option85 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option81)
        hbox.addWidget(self.option82)
        hbox.addWidget(self.option83)
        hbox.addWidget(self.option84)
        hbox.addWidget(self.option85)
        self.option81.setStyleSheet(stylesheet_QRadioButton)
        self.option82.setStyleSheet(stylesheet_QRadioButton)
        self.option83.setStyleSheet(stylesheet_QRadioButton)
        self.option84.setStyleSheet(stylesheet_QRadioButton)
        self.option85.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox8.setLayout(hbox)
        groupbox_layout.addWidget(groupbox8)

        groupbox9 = QGroupBox(
            "The teacher communicates clearly and inspires me by his/her teaching")
        hbox = QHBoxLayout()
        self.option91 = QRadioButton("Strongly Disagree")
        self.option92 = QRadioButton("Disagree")
        self.option93 = QRadioButton("Neither agree or disagree")
        self.option94 = QRadioButton("Agree")
        self.option95 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option91)
        hbox.addWidget(self.option92)
        hbox.addWidget(self.option93)
        hbox.addWidget(self.option94)
        hbox.addWidget(self.option95)
        self.option91.setStyleSheet(stylesheet_QRadioButton)
        self.option92.setStyleSheet(stylesheet_QRadioButton)
        self.option93.setStyleSheet(stylesheet_QRadioButton)
        self.option94.setStyleSheet(stylesheet_QRadioButton)
        self.option95.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox9.setLayout(hbox)
        groupbox_layout.addWidget(groupbox9)

        groupbox10 = QGroupBox(
            "The teacher is punctual in the class")
        hbox = QHBoxLayout()
        self.option101 = QRadioButton("Strongly Disagree")
        self.option102 = QRadioButton("Disagree")
        self.option103 = QRadioButton("Neither agree or disagree")
        self.option104 = QRadioButton("Agree")
        self.option105 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option101)
        hbox.addWidget(self.option102)
        hbox.addWidget(self.option103)
        hbox.addWidget(self.option104)
        hbox.addWidget(self.option105)
        self.option101.setStyleSheet(stylesheet_QRadioButton)
        self.option102.setStyleSheet(stylesheet_QRadioButton)
        self.option103.setStyleSheet(stylesheet_QRadioButton)
        self.option104.setStyleSheet(stylesheet_QRadioButton)
        self.option105.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox10.setLayout(hbox)
        groupbox_layout.addWidget(groupbox10)

        groupbox11 = QGroupBox(
            "The teacher comes well prepared for the class")
        hbox = QHBoxLayout()
        self.option111 = QRadioButton("Strongly Disagree")
        self.option112 = QRadioButton("Disagree")
        self.option113 = QRadioButton("Neither agree or disagree")
        self.option114 = QRadioButton("Agree")
        self.option115 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option111)
        hbox.addWidget(self.option112)
        hbox.addWidget(self.option113)
        hbox.addWidget(self.option114)
        hbox.addWidget(self.option115)
        self.option111.setStyleSheet(stylesheet_QRadioButton)
        self.option112.setStyleSheet(stylesheet_QRadioButton)
        self.option113.setStyleSheet(stylesheet_QRadioButton)
        self.option114.setStyleSheet(stylesheet_QRadioButton)
        self.option115.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox11.setLayout(hbox)
        groupbox_layout.addWidget(groupbox11)

        groupbox12 = QGroupBox(
            "The teacher encourage participation and discussion in the class")
        hbox = QHBoxLayout()
        self.option121 = QRadioButton("Strongly Disagree")
        self.option122 = QRadioButton("Disagree")
        self.option123 = QRadioButton("Neither agree or disagree")
        self.option124 = QRadioButton("Agree")
        self.option125 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option121)
        hbox.addWidget(self.option122)
        hbox.addWidget(self.option123)
        hbox.addWidget(self.option124)
        hbox.addWidget(self.option125)
        self.option121.setStyleSheet(stylesheet_QRadioButton)
        self.option122.setStyleSheet(stylesheet_QRadioButton)
        self.option123.setStyleSheet(stylesheet_QRadioButton)
        self.option124.setStyleSheet(stylesheet_QRadioButton)
        self.option125.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox12.setLayout(hbox)
        groupbox_layout.addWidget(groupbox12)

        groupbox13 = QGroupBox(
            "The teacher uses teaching aids, handouts, gives suitable references, make presentations and conduct seminars/tutorials, etc.")
        hbox = QHBoxLayout()
        self.option131 = QRadioButton("Strongly Disagree")
        self.option132 = QRadioButton("Disagree")
        self.option133 = QRadioButton("Neither agree or disagree")
        self.option134 = QRadioButton("Agree")
        self.option135 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option131)
        hbox.addWidget(self.option132)
        hbox.addWidget(self.option133)
        hbox.addWidget(self.option134)
        hbox.addWidget(self.option135)
        self.option131.setStyleSheet(stylesheet_QRadioButton)
        self.option132.setStyleSheet(stylesheet_QRadioButton)
        self.option133.setStyleSheet(stylesheet_QRadioButton)
        self.option134.setStyleSheet(stylesheet_QRadioButton)
        self.option135.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox13.setLayout(hbox)
        groupbox_layout.addWidget(groupbox13)

        groupbox14 = QGroupBox(
            "The teacher's attitude towards students is friendly and helpful")
        hbox = QHBoxLayout()
        self.option141 = QRadioButton("Strongly Disagree")
        self.option142 = QRadioButton("Disagree")
        self.option143 = QRadioButton("Neither agree or disagree")
        self.option144 = QRadioButton("Agree")
        self.option145 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option141)
        hbox.addWidget(self.option142)
        hbox.addWidget(self.option143)
        hbox.addWidget(self.option144)
        hbox.addWidget(self.option145)
        self.option141.setStyleSheet(stylesheet_QRadioButton)
        self.option142.setStyleSheet(stylesheet_QRadioButton)
        self.option143.setStyleSheet(stylesheet_QRadioButton)
        self.option144.setStyleSheet(stylesheet_QRadioButton)
        self.option145.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox14.setLayout(hbox)
        groupbox_layout.addWidget(groupbox14)

        groupbox15 = QGroupBox(
            "The teacher is available and accessible in the department")
        hbox = QHBoxLayout()
        self.option151 = QRadioButton("Strongly Disagree")
        self.option152 = QRadioButton("Disagree")
        self.option153 = QRadioButton("Neither agree or disagree")
        self.option154 = QRadioButton("Agree")
        self.option155 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option151)
        hbox.addWidget(self.option152)
        hbox.addWidget(self.option153)
        hbox.addWidget(self.option154)
        hbox.addWidget(self.option155)
        self.option151.setStyleSheet(stylesheet_QRadioButton)
        self.option152.setStyleSheet(stylesheet_QRadioButton)
        self.option153.setStyleSheet(stylesheet_QRadioButton)
        self.option154.setStyleSheet(stylesheet_QRadioButton)
        self.option155.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox15.setLayout(hbox)
        groupbox_layout.addWidget(groupbox15)

        groupbox16 = QGroupBox(
            "The evaluation process is fair and unbiased")
        hbox = QHBoxLayout()
        self.option161 = QRadioButton("Strongly Disagree")
        self.option162 = QRadioButton("Disagree")
        self.option163 = QRadioButton("Neither agree or disagree")
        self.option164 = QRadioButton("Agree")
        self.option165 = QRadioButton("Strongly agree")
        hbox.addWidget(self.option161)
        hbox.addWidget(self.option162)
        hbox.addWidget(self.option163)
        hbox.addWidget(self.option164)
        hbox.addWidget(self.option165)
        self.option161.setStyleSheet(stylesheet_QRadioButton)
        self.option162.setStyleSheet(stylesheet_QRadioButton)
        self.option163.setStyleSheet(stylesheet_QRadioButton)
        self.option164.setStyleSheet(stylesheet_QRadioButton)
        self.option165.setStyleSheet(stylesheet_QRadioButton)
        hbox.setContentsMargins(10, 20, 10,20)      
        groupbox16.setLayout(hbox)
        groupbox_layout.addWidget(groupbox16)

        sbox_layout = QVBoxLayout()
        self.form_submit = QPushButton("SUBMIT")
        self.form_submit.setStyleSheet(stylesheet_submit_button)

        self.form_submit.clicked.connect(lambda: self.submit_form())

        sbox_layout.addWidget(self.form_submit)
        sbox_layout.setContentsMargins(820, 40, 820,20)

        groupbox_layout.setSpacing(30)
        layout.addLayout(groupbox_layout)
        layout.addLayout(sbox_layout)

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
        groupbox13.setStyleSheet(stylesheet_QGroupBox)
        groupbox14.setStyleSheet(stylesheet_QGroupBox)
        groupbox15.setStyleSheet(stylesheet_QGroupBox)
        groupbox16.setStyleSheet(stylesheet_QGroupBox)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(win)

        layout_All = QVBoxLayout()
        layout_All.addWidget(self.scrollArea)

        self.setLayout(layout_All)
        self.setWindowTitle("Feedback Form")

    def option_number1(self, button1, button2, button3, button4):
        answer = 0
        if button1.isChecked() == True:
            answer = 1
        if button2.isChecked() == True:
            answer = 2
        if button3.isChecked() == True:
            answer = 3
        if button4.isChecked() == True:
            answer = 4
        return answer

    def option_number2(self, button1, button2, button3, button4, button5):
        answer = 0
        if button1.isChecked() == True:
            answer = 1
        if button2.isChecked() == True:
            answer = 2
        if button3.isChecked() == True:
            answer = 3
        if button4.isChecked() == True:
            answer = 4
        if button5.isChecked() == True:
            answer = 5
        return answer

    def submit_form(self):
        ans1 = self.option_number1(
            self.option11, self.option12, self.option13, self.option14)
        ans2 = self.option_number1(
            self.option21, self.option22, self.option23, self.option24)
        ans3 = self.option_number1(
            self.option31, self.option32, self.option33, self.option34)
        ans4 = self.option_number1(
            self.option41, self.option42, self.option43, self.option44)
        ans5 = self.option_number1(
            self.option51, self.option52, self.option53, self.option54)
        ans6 = self.option_number1(
            self.option61, self.option62, self.option63, self.option64)
        ans7 = self.option_number2(
            self.option71, self.option72, self.option73, self.option74, self.option75)
        ans8 = self.option_number2(
            self.option81, self.option82, self.option83, self.option84, self.option85)
        ans9 = self.option_number2(
            self.option91, self.option92, self.option93, self.option94, self.option95)
        ans10 = self.option_number2(
            self.option101, self.option102, self.option103, self.option104, self.option105)
        ans11 = self.option_number2(
            self.option111, self.option112, self.option113, self.option114, self.option115)
        ans12 = self.option_number2(
            self.option121, self.option122, self.option123, self.option124, self.option125)
        ans13 = self.option_number2(
            self.option131, self.option132, self.option133, self.option134, self.option135)
        ans14 = self.option_number2(
            self.option141, self.option142, self.option143, self.option144, self.option145)
        ans15 = self.option_number2(
            self.option151, self.option152, self.option153, self.option154, self.option155)
        ans16 = self.option_number2(
            self.option161, self.option162, self.option163, self.option164, self.option165)
        teacher_name = self.cb.currentText()
        course_name = self.course_cb.currentText()

        array_selected_answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15, ans16]

        if 0 in array_selected_answers:
            errorMessage("Fill Form")
        else:

            self.form_submit.setEnabled(False)

            new_teacher_name = teacher_name.replace(".", " ")
            new_string = '/' + new_teacher_name + "/" + course_name

            answer1_array = [[0 for i in range(4)] for j in range(6)] + [[0 for k in range(5)] for l in range(10)]
            answer1_array[0][ans1-1] += 1
            answer1_array[1][ans2-1] += 1
            answer1_array[2][ans3-1] += 1
            answer1_array[3][ans4-1] += 1
            answer1_array[4][ans5-1] += 1
            answer1_array[5][ans6-1] += 1
            answer1_array[6][ans7-1] += 1
            answer1_array[7][ans8-1] += 1
            answer1_array[8][ans9-1] += 1
            answer1_array[9][ans10-1] += 1
            answer1_array[10][ans11-1] += 1
            answer1_array[11][ans12-1] += 1
            answer1_array[12][ans13-1] += 1
            answer1_array[13][ans14-1] += 1
            answer1_array[14][ans15-1] += 1
            answer1_array[15][ans16-1] += 1
            fire.post(new_string, answer1_array)

            errorMessage("Thank you for giving this test, close this window.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    start = MainWindow()

    start.setFixedSize(450, 230)

    # Icon
    app_icon = QIcon()
    app_icon.addFile('icon.png', QSize(256, 256))
    app.setWindowIcon(app_icon)

    start.show()
    sys.exit(app.exec_())
