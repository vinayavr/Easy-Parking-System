# Easy-Parking-System
This Python application manages vehicle parking, including slot allocation, vehicle entry/exit, and admin management. Features a user-friendly GUI for efficient operations. Built with PyQt6 for UI and MySQL for database interactions.

Follow these steps to setup development environment:

1. Download the Easy Parking System source code from Git 
2. Create a MySQL database with Database name "parking". This Empty database must be created for successfully running this project.
3. Use python version 3.* or more in PyCharm IDE.
4. Install the python packages PyQt6, PyQt6-Qt6, PyQt6_sip, mysql-connector-python, mysql-connector-python-rf
5. Run the MainProgram.py
6. If the Database is empty, InstallWindow.py will be shown (onetime) where the database details needs to be configured. In this screen, the Admin username and password needs to be set for Easy Parking System login.
7. config.json file will be created in the project folder if the database is correctly configured.
Then LoginWindow.py will be shown where the user can login with username and password set for Easy Parking System.
Now Easy Parking System is setup for use.
