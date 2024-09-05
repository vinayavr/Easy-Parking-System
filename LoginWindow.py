from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from DataBaseOperation import DBOperation
from HomeWindow import HomeScreen


# noinspection PyUnresolvedReferences
class LoginScreen(QWidget):
    # noinspection PyUnresolvedReferences
    def __init__(self):
        super().__init__()
        self.home = None
        self.setWindowTitle("Easy Parking Login")
        self.resize(300, 100)

        layout = QVBoxLayout()

        label_username = QLabel("Username : ")
        label_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        self.input_username = QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")
        self.input_username.setMaxLength(30)
        label_password = QLabel("Password : ")
        label_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        self.error_msg = QLabel()
        self.error_msg.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center")
        self.input_password = QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setMaxLength(30)
        btn_login = QPushButton("Login")
        btn_login.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.setShortcut("Return")
        btn_login.clicked.connect(self.homepage)
        self.setLayout(layout)

    def signin(self):
        self.show()

    def homepage(self):
        if self.input_username.text() == "":
            self.error_msg.setText("Please Enter Username")
            self.input_username.setFocus()
            return

        if self.input_password.text() == "":
            self.error_msg.setText("Please Enter Password")
            self.input_password.setFocus()
            return

        dboperation = DBOperation()
        result = dboperation.do_admin_login(self.input_username.text(), self.input_password.text())
        if result:
            self.error_msg.setText("Login Successful")
            self.close()
            self.home = HomeScreen()
            self.home.show()
        else:
            self.error_msg.setText("Invalid Credentials. Try Again")
            self.input_username.setText("")
            self.input_password.setText("")
            self.input_username.setFocus()
