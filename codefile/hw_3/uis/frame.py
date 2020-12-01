from PyQt5.QtWidgets import QDialog,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QPainter,QPen,QColor
from PyQt5.QtCore import Qt,pyqtSignal
from fish import Fish
class myFrame(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1024,768)
        self.usernametag=QLabel("username",self)
        self.passwordtag=QLabel("password",self)
        self.username_value=QLineEdit(self)
        self.username_value=QLineEdit(self)
        self.login_btn=QPushButton('login',self)
        self.usernametg.move(300,400)
        self.passwordtag.move(300,500)
        self.username_input.move(400,400)
        self.username_input.move(400,500)
        self.login_btn.move(450,500)

