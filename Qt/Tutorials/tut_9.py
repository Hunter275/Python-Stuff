import sys
from PyQt4 import QtGui

import os
import subprocess


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Save', self)
        self.btn.move(320, 110)
        self.btn.clicked.connect(self.open)

        self.label = QtGui.QLabel("Filename", self)
        self.label.move(70, 23)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Text Editor')
        self.show()

	def open():
		global target
		target = open(str(file_name), "w+")

	def write():
		#target.open(file_name, "w")
		target.write(text_write.get())
		#target.write(file_name.get())
		target.close()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()