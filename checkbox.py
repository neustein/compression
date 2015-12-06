import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

def print_state(state):
    if state == 0: 
        print("Unchecked")
    else:
        print("Checked")

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    check_box = QtGui.QCheckBox("Check box")

    check_box.stateChanged.connect(print_state)

    main_window.setCentralWidget(check_box)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
