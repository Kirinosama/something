from PyQt5.QtWidgets import QApplication
from frame import myFrame
class myApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window=myFrame()
        self.window.show()

