import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(500, 300) #window size (h,w)
    w.move(300, 300)   #window location on screen (h,w)
    w.setWindowTitle('Text Editor') #window tite
    w.show() #shows the window on screen
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()