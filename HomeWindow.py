from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QGridLayout, \
    QTableWidget, QTableWidgetItem, QMainWindow, QFrame, QComboBox, QHeaderView, QMessageBox
from DataBaseOperation import DBOperation

# noinspection PyUnresolvedReferences


class HomeScreen(QMainWindow):
    # noinspection PyUnresolvedReferences
    def __init__(self):
        super().__init__()
        self.layout1 = None
        self.frame5 = None
        self.table1 = None
        self.button_exit = None
        self.table = None
        self.gridLayout = None
        self.error_label = None
        self.vehicle_type_cbo = None
        self.slot_no_cbo = None
        self.setWindowTitle("Easy Parking System")

        self.dbOperation = DBOperation()

        widget = QWidget()
        layout_horizontal = QHBoxLayout()
        menu_vertical_layout = QVBoxLayout()

        self.btn_home = QPushButton("Home")
        self.btn_add = QPushButton("Book Slot")
        self.btn_manage = QPushButton("Manage Slot")
        self.btn_history = QPushButton("History")

        menu_vertical_layout.setContentsMargins(0, 0, 0, 0)
        menu_vertical_layout.setSpacing(0)
        self.btn_home.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_add.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_manage.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_history.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")

        self.btn_home.clicked.connect(self.show_home)
        self.btn_add.clicked.connect(self.add_layouts)
        self.btn_manage.clicked.connect(self.show_manage)
        self.btn_history.clicked.connect(self.show_history)

        menu_frame = QFrame()
        menu_vertical_layout.addWidget(self.btn_home)
        menu_vertical_layout.addWidget(self.btn_add)
        menu_vertical_layout.addWidget(self.btn_manage)
        menu_vertical_layout.addWidget(self.btn_history)
        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        # menu_frame.setMinimumWidth(200)
        # menu_frame.setMaximumHeight(200)

        parent_vertical = QVBoxLayout()
        parent_vertical.setContentsMargins(0, 0, 0, 0)
        self.vertical_1 = QVBoxLayout()
        self.add_home_layout()

        self.vertical_2 = QVBoxLayout()
        self.vertical_2.setContentsMargins(0, 0, 0, 0)
        self.add_book_slot_layout()

        self.vertical_3 = QVBoxLayout()
        self.vertical_3.setContentsMargins(0, 0, 0, 0)
        self.add_manage_slot_layout()

        self.vertical_4 = QVBoxLayout()
        self.add_history_layout()

        self.frame_1 = QFrame()
        self.frame_1.setMinimumWidth(self.width())
        self.frame_1.setMaximumWidth(self.width())
        self.frame_1.setMaximumHeight(self.width())
        self.frame_1.setMaximumHeight(self.width())

        self.frame_1.setLayout(self.vertical_1)
        self.frame_2 = QFrame()
        self.frame_2.setLayout(self.vertical_2)
        self.frame_3 = QFrame()
        self.frame_3.setLayout(self.vertical_3)
        self.frame_4 = QFrame()
        self.frame_4.setLayout(self.vertical_4)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)

        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        layout_horizontal.setContentsMargins(0, 0, 0, 0)
        parent_vertical.setContentsMargins(0, 0, 0, 0)
        parent_vertical.addStretch()
        # menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal)

        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()

        self.setCentralWidget(widget)

    def show_history(self):
        self.btn_home.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_add.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_manage.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_history.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;border:1px solid "
            "white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()
        self.refresh_history()

    def show_manage(self):
        self.btn_home.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_add.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_manage.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_history.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_3.show()
        self.refresh_manage_slot()

    def add_layouts(self):
        self.btn_home.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_add.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_manage.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")
        self.btn_history.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid "
            "white")

        self.frame_1.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_2.show()
        if self.error_label is not None:
            self.error_label.setText("")

    def show_home(self):
        self.btn_home.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;"
            "border:1px solid white")
        self.btn_add.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;"
            "border:1px solid white")
        self.btn_manage.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;"
            "border:1px solid white")
        self.btn_history.setStyleSheet(
            "width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;"
            "border:1px solid white")

        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_1.show()
        self.refresh_home()

    def refresh_home(self):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        row = 0
        i = 0
        alldata = self.dbOperation.get_slot_space()
        for data in alldata:
            label = QPushButton("Slot " + str(data[0]) + " \n " + str(data[2]) + " Wheeler" + "\n" + str(data[1]))

            if data[3] == 1:
                label.setStyleSheet(
                    "background-color:green;color:white;padding:5px;width:100px;height:100px;"
                    "border:1px solid white;text-align:center;font-weight:bold")
                label.clicked.connect(lambda _, slot_no=data[0], vehicle_type=str(data[2]):
                                      self.book_slot(slot_no, vehicle_type))
            else:
                label.setStyleSheet(
                    "background-color:red;color:white;padding:5px;width:100px;height:100px;"
                    "border:1px solid white;text-align:center;font-weight:bold")
                # label.clicked.connect(lambda _, slot_no=data[0]: self.show_confirm_exit(slot_no))

            if i % 5 == 0:
                i = 0
                row = row + 1

            self.gridLayout.addWidget(label, row, i)
            i = i + 1

    def add_home_layout(self):
        self.vertical_1.setContentsMargins(0, 0, 0, 0)

        button = QPushButton("Refresh Slot")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:#696969;border:1px solid white")
        button.clicked.connect(self.refresh_home)
        button.setShortcut("Enter")

        vertical_layout = QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        frame = QFrame()

        horizontal = QHBoxLayout()
        horizontal.setContentsMargins(0, 0, 0, 0)
        vertical_layout.addLayout(horizontal)

        alldata = self.dbOperation.get_slot_space()
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        vertical_layout.addWidget(button)
        vertical_layout.addLayout(self.gridLayout)

        row = 0
        i = 0
        for data in alldata:
            label = QPushButton("Slot " + str(data[0]) + " \n " + str(data[2]) + " Wheeler" + "\n" + str(data[1]))

            if data[3] == 1:
                label.setStyleSheet(
                    "background-color:green;color:white;padding:5px;width:100px;height:100px;"
                    "border:1px solid white;text-align:center;font-weight:bold")
                label.clicked.connect(lambda _, slot_no=data[0], vehicle_type=str(data[2]):
                                      self.book_slot(slot_no, vehicle_type))
            else:
                label.setStyleSheet(
                    "background-color:red;color:white;padding:5px;width:100px;height:100px;"
                    "border:1px solid white;text-align:center;font-weight:bold")
                # label.clicked.connect(lambda _, slot_no=data[0]: self.show_confirm_exit(slot_no))

            if i % 5 == 0:
                i = 0
                row = row + 1

            self.gridLayout.addWidget(label, row, i)
            i = i + 1

        frame.setLayout(vertical_layout)
        self.vertical_1.addWidget(frame)
        self.vertical_1.addStretch()

    def book_slot(self, slot_no, vehicle_type):
        if vehicle_type == "2":
            self.vehicle_type_cbo.setCurrentIndex(0)
        else:
            self.vehicle_type_cbo.setCurrentIndex(1)
        if self.slot_no_cbo.findText(str(slot_no)) != -1:
            self.slot_no_cbo.setCurrentText(str(slot_no))
        self.add_layouts()

    def show_confirm_exit(self, slot_no):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Exit Vehicle")
        dlg.setText("Do you want to exit vehicle from slot " + str(slot_no) + "?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            self.dbOperation.exit_vehicle(str(slot_no))
            self.refresh_home()

    def add_book_slot_layout(self):
        layout = QVBoxLayout()
        frame = QFrame()

        vehicle_type = QLabel("Vehicle Type : ")
        vehicle_type.setStyleSheet("color:#000;padding:8px 0px;font-size:20px")
        slot_no_label = QLabel("Slot : ")
        slot_no_label.setStyleSheet("color:#000;padding:8px 0px;font-size:20px")
        name_label = QLabel("Name : ")
        name_label.setStyleSheet("color:#000;padding:8px 0px;font-size:20px")
        mobile_label = QLabel("Mobile : ")
        mobile_label.setStyleSheet("color:#000;padding:8px 0px;font-size:20px")
        vehicle_label = QLabel("Vehicle No : ")
        vehicle_label.setStyleSheet("color:#000;padding:8px 0px;font-size:20px")
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color:red;padding:8px 0px;font-size:20px")

        self.vehicle_type_cbo = QComboBox()
        self.vehicle_type_cbo.setStyleSheet("padding:8px 0px;font-size:20px;border:1px solid white")
        self.vehicle_type_cbo.addItem("2 Wheeler")
        self.vehicle_type_cbo.addItem("4 Wheeler")
        self.slot_no_cbo = QComboBox()
        self.slot_no_cbo.setStyleSheet("padding:8px 0px;font-size:20px;border:1px solid white")
        name_input = QLineEdit()
        name_input.setStyleSheet("padding:8px 0px;font-size:20px")
        name_input.setMaxLength(30)
        mobile_input = QLineEdit()
        mobile_input.setStyleSheet("padding:8px 0px;font-size:20px")
        mobile_input.setMaxLength(30)
        vehicle_input = QLineEdit()
        vehicle_input.setStyleSheet("padding:8px 0px;font-size:20px")
        vehicle_input.setMaxLength(30)

        button = QPushButton("Book Slot")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.setShortcut("Enter")

        layout.addWidget(vehicle_type)
        layout.addWidget(self.vehicle_type_cbo)
        layout.addWidget(slot_no_label)
        layout.addWidget(self.slot_no_cbo)
        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(mobile_label)
        layout.addWidget(mobile_input)
        layout.addWidget(vehicle_label)
        layout.addWidget(vehicle_input)
        layout.addWidget(button)
        layout.addWidget(self.error_label)

        layout.setContentsMargins(0, 0, 0, 0)
        frame.setMinimumHeight(self.height())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.width())
        frame.setMaximumWidth(self.width())

        layout.addStretch()
        frame.setLayout(layout)
        button.clicked.connect(
            lambda: self.add_vehicle(name_input, vehicle_input, mobile_input, self.vehicle_type_cbo, self.slot_no_cbo,
                                     self.error_label))
        self.vehicle_type_cbo.currentIndexChanged.connect(lambda: self.add_available_slots(self.vehicle_type_cbo, self.slot_no_cbo))
        self.add_available_slots(self.vehicle_type_cbo, self.slot_no_cbo)
        self.vertical_2.addWidget(frame)

    def add_available_slots(self, vehicle_type, slot_no):
        vtp = 2
        if vehicle_type.currentIndex() == 0:
            vtp = 2
        else:
            vtp = 4
        data = self.dbOperation.get_available_slots(vtp)
        slot_no.clear()
        slot_no.addItems(data)
        slot_no.setCurrentIndex(0)

    def add_vehicle(self, name, vehicle, mobile, index, slot_no, error_label):
        if name.text() == "":
            error_label.setText("Please Enter Vehicle Name")
            name.setFocus()
            return

        if mobile.text() == "":
            error_label.setText("Please Enter Mobile No")
            mobile.setFocus()
            return

        if vehicle.text() == "":
            error_label.setText("Please Enter Vehicle No")
            vehicle.setFocus()
            return

        vtp = "2"
        if index.currentIndex() == 0:
            vtp = "2"
        else:
            vtp = "4"

        ret_value = self.dbOperation.check_already_booked(vehicle.text())
        if ret_value == -1:
            data = self.dbOperation.add_vehicles(name.text(), vehicle.text(), mobile.text(), vtp, slot_no.currentText())
            if data:
                error_label.setText("Slot Booked Successfully")
                name.setText("")
                vehicle.setText("")
                mobile.setText("")
                index.setCurrentIndex(0)
                self.add_available_slots(self.vehicle_type_cbo, self.slot_no_cbo)
            else:
                error_label.setText("Failed to Book Slot : " + str(data))
        else:
            error_label.setText("Vehicle No " + vehicle.text() + " already booked in Slot " + str(ret_value))

    def add_manage_slot_layout(self):
        data = self.dbOperation.get_current_vehicle()
        self.table = QTableWidget()
        self.table.setStyleSheet("background:#fff")
        self.table.resize(self.width(), self.height())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(8)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Slot No"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("VEHICLE No"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("MOBILE"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("VEHICLE TYPE"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("ENTRY TIME"))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem("ACTION"))

        if len(data) > 0:
            loop = 0
            for smalldata in data:
                self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
                self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[10])))
                self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[1])))
                self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[6])))
                self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[2])))
                self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[7])))
                self.table.setItem(loop, 6, QTableWidgetItem(str(smalldata[3])))
                self.button_exit = QPushButton("Exit")
                self.button_exit.setStyleSheet(
                    "color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
                self.table.setCellWidget(loop, 7, self.button_exit)
                self.button_exit.clicked.connect(self.exit_vehicle)
                loop = loop + 1

        frame = QFrame()
        layout = QVBoxLayout()
        button = QPushButton("Refresh")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refresh_manage_slot)
        button.setShortcut("Enter")

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(button)
        layout.addWidget(self.table)
        frame.setLayout(layout)
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setMaximumWidth(self.width())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.height())
        frame.setMinimumHeight(self.height())
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()

    def refresh_manage_slot(self):
        data = self.dbOperation.get_current_vehicle()
        self.table.setColumnCount(8)
        self.table.setRowCount(len(data))
        if len(data) > 0:
            loop = 0
            for smalldata in data:
                self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
                self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[10])))
                self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[1])))
                self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[6])))
                self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[2])))
                self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[7])))
                self.table.setItem(loop, 6, QTableWidgetItem(str(smalldata[3])))
                self.button_exit = QPushButton("Exit")
                self.table.setCellWidget(loop, 7, self.button_exit)
                self.button_exit.clicked.connect(self.exit_vehicle)
                loop = loop + 1

    def refresh_history(self):
        self.table1.clearContents()
        self.table1.setStyleSheet("background:#fff")
        data = self.dbOperation.get_all_vehicles()
        loop = 0
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)
        if len(data) > 0:
            for smalldata in data:
                self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
                self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
                self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
                self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
                self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
                self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
                self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
                loop = loop + 1

    def add_history_layout(self):
        data = self.dbOperation.get_all_vehicles()
        self.table1 = QTableWidget()
        self.table1.resize(self.width(), self.height())
        self.table1.setRowCount(len(data))
        self.table1.setStyleSheet("background:#fff")
        self.table1.setColumnCount(7)

        button = QPushButton("Refresh")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refresh_history)
        button.setShortcut("Enter")

        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("VEHICLE No"))
        self.table1.setHorizontalHeaderItem(3, QTableWidgetItem("MOBILE"))
        self.table1.setHorizontalHeaderItem(4, QTableWidgetItem("VEHICLE TYPE"))
        self.table1.setHorizontalHeaderItem(5, QTableWidgetItem("ENTRY TIME"))
        self.table1.setHorizontalHeaderItem(6, QTableWidgetItem("EXIT TIME"))

        loop = 0
        if len(data) > 0:
            for smalldata in data:
                self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
                self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
                self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
                self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
                self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
                self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
                self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
                loop = loop + 1

        self.frame5 = QFrame()
        self.layout1 = QVBoxLayout()
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.setSpacing(0)
        self.layout1.addWidget(button)
        self.layout1.addWidget(self.table1)
        self.frame5.setLayout(self.layout1)
        self.frame5.setContentsMargins(0, 0, 0, 0)
        self.frame5.setMaximumWidth(self.width())
        self.frame5.setMinimumWidth(self.width())
        self.frame5.setMaximumHeight(self.height())
        self.frame5.setMinimumHeight(self.height())
        self.vertical_4.addWidget(self.frame5)
        self.vertical_4.addStretch()

    def exit_vehicle(self):
        sender = self.sender()
        if sender:
            row = self.table.indexAt(sender.pos()).row()
            vehicle = str(self.table.item(row, 0).text())
            self.dbOperation.exit_vehicle(vehicle)
            self.table.removeRow(row)
