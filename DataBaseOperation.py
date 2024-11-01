import mysql.connector
import json
from datetime import datetime


class DBOperation:

    def __init__(self):

        # Read JSON data from a file
        with open("./config.json", "r") as f:
            config = json.load(f)

        # Extract connection parameters from JSON
        host = config["host"]
        user = config["user"]
        password = config["passwd"]
        database = config["database"]

        self.mydb = mysql.connector.connect(host=host, user=user, passwd=password, database=database)

    def create_tables(self):
        cursor = self.mydb.cursor()
        cursor.execute("DROP TABLE if exists admin")
        cursor.execute("DROP TABLE if exists slot")
        cursor.execute("DROP TABLE if exists vehicle")
        cursor.execute("DROP TABLE if exists vehicle_history")
        cursor.execute(
            "CREATE TABLE admin (id int(255) AUTO_INCREMENT PRIMARY KEY,username varchar(30),"
            "password varchar(30),created_at varchar(30))")
        cursor.execute(
            "CREATE TABLE slot (id int(255) AUTO_INCREMENT PRIMARY KEY,vehicle_id varchar(30),"
            "space_for int(25),is_empty int(25))")
        cursor.execute(
            "CREATE TABLE vehicle (id int(255) AUTO_INCREMENT PRIMARY KEY,name varchar(30),"
            "mobile varchar(30),entry_time varchar(30),exit_time varchar(30),is_exit varchar(30),"
            "vehicle_no varchar(30),vehicle_type varchar(30),created_at varchar(30),updated_at varchar(30))")
        cursor.execute(
            "CREATE TABLE vehicle_history (id int(255) AUTO_INCREMENT PRIMARY KEY,name varchar(30),"
            "mobile varchar(30),entry_time varchar(30),exit_time varchar(30),is_exit varchar(30),"
            "vehicle_no varchar(30),vehicle_type varchar(30),created_at varchar(30),updated_at varchar(30))")
        cursor.close()

    def insert_onetime_data(self, space_for_two, space_for_four):
        cursor = self.mydb.cursor()
        for x in range(space_for_two):
            cursor.execute("INSERT into slot (space_for,is_empty) values ('2','1')")
            self.mydb.commit()

        for x in range(space_for_four):
            cursor.execute("INSERT into slot (space_for,is_empty) values ('4','1')")
            self.mydb.commit()
        cursor.close()

    def insert_admin(self, username, password):
        cursor = self.mydb.cursor()
        val = (username, password)
        cursor.execute("INSERT into admin (username,password) values (%s,%s)", val)
        self.mydb.commit()
        cursor.close()

    def do_admin_login(self, username, password):
        cursor = self.mydb.cursor()
        cursor.execute("select * from admin where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return True
        else:
            return False

    def get_slot_space(self):
        cursor = self.mydb.cursor()
        cursor.execute(
            "select s.id, vehicle_no, space_for, is_empty from slot s left outer join vehicle v "
            "on s.vehicle_id = v.id")
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_current_vehicle(self):
        cursor = self.mydb.cursor()
        row_count = cursor.execute(
            "select v.*, slot.id from vehicle v join slot where v.id = slot.vehicle_id and is_exit='0'")
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_all_vehicles(self):
        cursor = self.mydb.cursor()
        cursor.execute("select * from vehicle_history order by updated_at desc")
        data = cursor.fetchall()
        cursor.close()
        return data

    def add_vehicles(self, name, vehicle_no, mobile, vehicle_type, slot_no):
        space_id = self.space_available(vehicle_type, slot_no)
        if space_id:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = (name, mobile, str(current_date), '', '0', vehicle_no, str(current_date), str(current_date),
                    vehicle_type)
            cursor = self.mydb.cursor()
            cursor.execute(
                "INSERT into vehicle (name,mobile,entry_time,exit_time,is_exit,vehicle_no,"
                "created_at,updated_at,vehicle_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                data)
            self.mydb.commit()
            last_id = cursor.lastrowid
            cursor.execute(
                "UPDATE slot set vehicle_id='" + str(last_id) + "',is_empty='0' where id='" + str(space_id) + "'")
            self.mydb.commit()
            cursor.close()
            return True
        else:
            return "No Space Available for Parking"

    def space_available(self, v_type, slot_no):
        cursor = self.mydb.cursor()
        cursor.execute("select * from slot where is_empty='1' and space_for='" + str(v_type) + "' and id='"+slot_no+"'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return data[0][0]
        else:
            return False

    def get_available_slots(self, v_type):
        cursor = self.mydb.cursor()
        cursor.execute("select id from slot where is_empty='1' and space_for='" + str(v_type) + "'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return [str(item[0]) for item in data]
        else:
            return []

    def check_already_booked(self, v_no):
        cursor = self.mydb.cursor()
        cursor.execute("select s.id from slot s, vehicle v where v.id=s.vehicle_id "
                       "and is_exit='0' and vehicle_no='" + str(v_no) + "'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) == 0:
            return -1
        else:
            return data[0][0]

    def exit_vehicle(self, vehicle_id):
        cursor = self.mydb.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("UPDATE slot set is_empty='1',vehicle_id=NULL where vehicle_id='" + vehicle_id + "'")
        self.mydb.commit()
        cursor.execute("UPDATE vehicle set is_exit='1',exit_time='" + current_date + "' where id='" + vehicle_id + "'")
        self.mydb.commit()
        cursor.execute("INSERT into vehicle_history (name,mobile,entry_time,exit_time,is_exit,vehicle_no,"
                       "vehicle_type,created_at,updated_at) SELECT name,mobile,entry_time,exit_time,is_exit,"
                       "vehicle_no,vehicle_type,created_at,updated_at FROM vehicle WHERE  id='" + vehicle_id + "'")
        self.mydb.commit()
