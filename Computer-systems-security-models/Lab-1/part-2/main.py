import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 188)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 12, 344, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.adr_der = QtWidgets.QLineEdit(self.widget)
        self.adr_der.setObjectName("adr_der")
        self.horizontalLayout_2.addWidget(self.adr_der)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.adr_der_2 = QtWidgets.QLineEdit(self.widget)
        self.adr_der_2.setObjectName("adr_der_2")
        self.horizontalLayout.addWidget(self.adr_der_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.start_btn = QtWidgets.QPushButton(self.widget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def add_function(self):
        self.start_btn.clicked.connect(lambda: self.start())

    def start(self):
        adr = self.adr_der.text()
        adr_to_save = self.adr_der_2.text()
        if not os.path.isdir(adr):
            self.error_box("Папки для слежки не существует!")
        elif not os.path.isdir(adr_to_save):
            self.error_box("Папки для копирования не существует")
        else:
            files = []
            for i in os.listdir(adr):
                if ".txt" in i:
                    files.append(i)
            while True:
                time.sleep(60)
                for i in os.listdir(adr):
                    if ".txt" in i:
                        if i not in files:
                            file = open(adr + "\\" + i, "r")
                            shutil.copyfile(adr + "\\" + i, adr_to_save + "\\" + i)







    def error_box(self, text):
        err = QtWidgets.QMessageBox()
        err.setWindowTitle("Ошибка")
        err.setIcon(QtWidgets.QMessageBox.Warning)
        err.setText(text)
        err.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение нарушителя"))
        self.label.setText(_translate("MainWindow", "Папка слежки:"))
        self.label_2.setText(_translate("MainWindow", "Папка копирования:"))
        self.start_btn.setText(_translate("MainWindow", "Старт"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
