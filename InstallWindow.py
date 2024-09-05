from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from LoginWindow import LoginScreen
import json
from DataBaseOperation import DBOperation


# noinspection PyUnresolvedReferences
class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.login = None
        self.setWindowTitle("Configure Easy Parking")
        # self.resize(400, 200)

        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QWidget().screen().availableGeometry().top()
        self.qtRectangle.moveTop(self.centerPoint)
        self.move(self.qtRectangle.topRight())

        layout = QVBoxLayout()

        label_db_name = QLabel("Database Name : ")
        label_db_name.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_db_username = QLabel("Database Username : ")
        label_db_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_db_password = QLabel("Database Password : ")
        label_db_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_admin_username = QLabel("Easy Parking Username : ")
        label_admin_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_admin_password = QLabel("Easy Parking Password : ")
        label_admin_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_no_of_two_seater = QLabel("No of Two Wheeler Slots : ")
        label_no_of_two_seater.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_no_of_four_seater = QLabel("No. of Four Wheeler Slots : ")
        label_no_of_four_seater.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_db_name = QLineEdit()
        self.input_db_name.setText("parking")
        self.input_db_name.setStyleSheet("padding:5px;font-size:17px")
        self.input_db_name.setEnabled(False)

        self.input_db_username = QLineEdit()
        self.input_db_username.setText("")
        self.input_db_username.setStyleSheet("padding:5px;font-size:17px")
        self.input_db_username.setMaxLength(8)

        self.input_db_password = QLineEdit()
        self.input_db_password.setText("")
        self.input_db_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_db_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_db_password.setMaxLength(8)

        self.input_admin_username = QLineEdit()
        self.input_admin_username.setStyleSheet("padding:5px;font-size:17px")
        self.input_db_password.setMaxLength(30)

        self.input_admin_password = QLineEdit()
        self.input_admin_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_admin_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_admin_password.setMaxLength(30)

        self.input_two_wheeler = QLineEdit()
        self.input_two_wheeler.setStyleSheet("padding:5px;font-size:17px")
        self.input_two_wheeler.setMaxLength(5)
        self.input_four_wheeler = QLineEdit()
        self.input_four_wheeler.setStyleSheet("padding:5px;font-size:17px")
        self.input_four_wheeler.setMaxLength(5)
        self.save = QPushButton("Save")
        self.save.setShortcut("Return")
        self.save.setStyleSheet("padding:5px;font-size:17px;background:green;color:#fff")

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color:red;padding:8px 0px;font-size:18px;")

        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(self.input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(self.input_admin_password)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(self.input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(self.input_four_wheeler)
        layout.addWidget(self.save)
        layout.addWidget(self.error_label)

        self.save.clicked.connect(self.step)
        self.setLayout(layout)

    def step(self):
        if self.input_db_username.text() == "":
            self.error_label.setText("Please Enter Database Username")
            self.input_db_username.setFocus()
            return

        if self.input_db_password.text() == "":
            self.error_label.setText("Please Enter Database Password")
            self.input_db_password.setFocus()
            return

        if self.input_admin_username.text() == "":
            self.error_label.setText("Please Enter Easy Parking Username")
            self.input_admin_username.setFocus()
            return

        if self.input_admin_password.text() == "":
            self.error_label.setText("Please Enter Easy Parking Password")
            self.input_admin_password.setFocus()
            return

        if self.input_two_wheeler.text() == "":
            self.error_label.setText("Please Enter Number of Two Wheeler Slots")
            self.input_two_wheeler.setFocus()
            return

        if self.input_four_wheeler.text() == "":
            self.error_label.setText("Please Enter Number of Four Wheeler Slots")
            self.input_four_wheeler.setFocus()
            return

        data = {"host": "localhost", "user": self.input_db_username.text(),
                "passwd": self.input_db_password.text(),
                "database": self.input_db_name.text()}
        file = open("./config.json", "w")
        file.write(json.dumps(data))
        file.close()

        dboperation = DBOperation()
        dboperation.create_tables()
        dboperation.insert_admin(self.input_admin_username.text(), self.input_admin_password.text())
        dboperation.insert_onetime_data(int(self.input_two_wheeler.text()), int(self.input_four_wheeler.text()))

        self.close()
        self.login = LoginScreen()
        self.login.signin()
        print("Save")
