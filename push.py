import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

def on_click():
    print("Hello World")

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    hello_button = QtGui.QPushButton("Hello World")

    hello_button.clicked.connect(on_click)

    main_window.setCentralWidget(hello_button)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
