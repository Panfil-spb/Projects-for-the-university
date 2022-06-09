from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 771, 511))
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
        self.adress_der = QtWidgets.QLineEdit(self.widget)
        self.adress_der.setObjectName("adress_der")
        self.horizontalLayout_2.addWidget(self.adress_der)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.load_files_names_btn = QtWidgets.QPushButton(self.widget)
        self.load_files_names_btn.setObjectName("load_files_names_btn")
        self.verticalLayout.addWidget(self.load_files_names_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.choise_old_files = QtWidgets.QComboBox(self.widget)
        self.choise_old_files.setObjectName("choise_old_files")
        self.horizontalLayout.addWidget(self.choise_old_files)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.name_new_file = QtWidgets.QLineEdit(self.widget)
        self.name_new_file.setObjectName("name_new_file")
        self.horizontalLayout_3.addWidget(self.name_new_file)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.text_tosave = QtWidgets.QTextEdit(self.widget)
        self.text_tosave.setObjectName("text_tosave")
        self.horizontalLayout_5.addWidget(self.text_tosave)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.new_file_save_btn = QtWidgets.QPushButton(self.widget)
        self.new_file_save_btn.setObjectName("new_file_save_btn")
        self.horizontalLayout_4.addWidget(self.new_file_save_btn)
        self.save_file_choise_btn = QtWidgets.QPushButton(self.widget)
        self.save_file_choise_btn.setObjectName("save_file_choise_btn")
        self.horizontalLayout_4.addWidget(self.save_file_choise_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def add_function(self):
        self.load_files_names_btn.clicked.connect(lambda: self.check_adr())
        self.new_file_save_btn.clicked.connect(lambda: self.check_name_new_file())
        self.save_file_choise_btn.clicked.connect(lambda: self.save_text_to_file())

    def save_text_to_file(self):
        file_adr = self.adress_der.text() + "\\" + self.choise_old_files.currentText()
        file = open(file_adr, "a")
        file.write("\n")
        for i in self.text_tosave.toPlainText():
            file.write(i)

    def check_name_new_file(self):
        if self.name_new_file.text() == "":
            self.error_box("Вы не ввели имя файла")
        else:
            file_adr = self.adress_der.text() + "\\" +self.name_new_file.text() + ".txt"
            file = open(file_adr, "w")
            print(self.text_tosave.toPlainText())
            for i in self.text_tosave.toPlainText():
                file.write(i)

    def check_adr(self):
        path = self.adress_der.text()
        if not os.path.isdir(path):
            self.error_box("Такой папки не существует!")
        else:
            files = []
            for i in os.listdir(path):
                if ".txt" in i:
                    files.append(i)
            self.choise_old_files.addItems(files)

    def error_box(self, text):
        err = QtWidgets.QMessageBox()
        err.setWindowTitle("Ошибка")
        err.setIcon(QtWidgets.QMessageBox.Warning)
        err.setText(text)
        err.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовые файлы"))
        self.label.setText(_translate("MainWindow", "Адрес папки:"))
        self.load_files_names_btn.setText(_translate("MainWindow", "Загрузить файлы"))
        self.label_2.setText(_translate("MainWindow", "Файлы в папке:"))
        self.label_3.setText(_translate("MainWindow", "Новый файл:"))
        self.label_4.setText(_translate("MainWindow", "Текст:"))
        self.new_file_save_btn.setText(_translate("MainWindow", "Сохранить в новый файл"))
        self.save_file_choise_btn.setText(_translate("MainWindow", "Сохранить в выбранный файл"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
