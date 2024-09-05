import sys
import os
from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer


class MainScreen:
    def __init__(self):
        self.splash = None
        self.pix = None

    def splashscreen(self):
        self.pix = QPixmap("splash_screen.jpg")
        self.splash = QSplashScreen(self.pix, Qt.WindowType.WindowStaysOnTopHint)
        self.splash.show()


def setup():
    mainScreen.splash.close()
    installWindow.show()


def signin():
    mainScreen.splash.close()
    login.signin()


app = QApplication(sys.argv)

login = LoginScreen()
mainScreen = MainScreen()
mainScreen.splashscreen()
installWindow = InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(3000, signin)
else:
    QTimer.singleShot(3000, setup)

app.setWindowIcon(QIcon("./icon.ico"))
sys.exit(app.exec())
