from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys

class Ui_MainWindow(object):
    names = {}
    def __init__(self):
        file = open("C:\\Users\\Feelan\\Desktop\\Prakt2\\names.txt", "r")
        for i in file.readlines():
            line = i.split()
            self.names[line[0]] = line[1:]
        file.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 331, 96))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.new_name = QtWidgets.QLineEdit(self.widget)
        self.new_name.setObjectName("new_name")
        self.horizontalLayout_3.addWidget(self.new_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_new_name_btn = QtWidgets.QPushButton(self.widget)
        self.add_new_name_btn.setObjectName("add_new_name_btn")
        self.horizontalLayout_2.addWidget(self.add_new_name_btn)
        self.clear_new_name_btn = QtWidgets.QPushButton(self.widget)
        self.clear_new_name_btn.setObjectName("clear_new_name_btn")
        self.horizontalLayout_2.addWidget(self.clear_new_name_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.names_combo_box = QtWidgets.QComboBox(self.widget)

        self.names_combo_box.setObjectName("names_combo_box")
        self.names_combo_box.addItems(self.names.keys())

        self.horizontalLayout.addWidget(self.names_combo_box)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 120, 331, 271))
        self.widget1.setObjectName("widget1")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        if self.names[self.names_combo_box.currentText()][0] == '1':
            self.checkBox.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        if self.names[self.names_combo_box.currentText()][1] == '1':
            self.checkBox_2.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        if self.names[self.names_combo_box.currentText()][2] == '1':
            self.checkBox_3.setChecked(True)
        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_4 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        if self.names[self.names_combo_box.currentText()][3] == '1':
            self.checkBox_4.setChecked(True)
        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        if self.names[self.names_combo_box.currentText()][4] == '1':
            self.checkBox_5.setChecked(True)
        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.checkBox_6 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        if self.names[self.names_combo_box.currentText()][5] == '1':
            self.checkBox_6.setChecked(True)
        self.verticalLayout_4.addWidget(self.checkBox_6)

        self.checkBox_7 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        if self.names[self.names_combo_box.currentText()][6] == '1':
            self.checkBox_7.setChecked(True)
        self.verticalLayout_4.addWidget(self.checkBox_7)

        self.checkBox_8 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        if self.names[self.names_combo_box.currentText()][7] == '1':
            self.checkBox_8.setChecked(True)
        self.verticalLayout_4.addWidget(self.checkBox_8)

        self.checkBox_9 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        if self.names[self.names_combo_box.currentText()][8] == '1':
            self.checkBox_9.setChecked(True)
        self.verticalLayout_4.addWidget(self.checkBox_9)

        self.checkBox_10 = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        if self.names[self.names_combo_box.currentText()][9] == '1':
            self.checkBox_10.setChecked(True)
        self.verticalLayout_4.addWidget(self.checkBox_10)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.save_btn = QtWidgets.QPushButton(self.widget1)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_5.addWidget(self.save_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def add_function(self):
        self.clear_new_name_btn.clicked.connect(lambda: self.clear_name())
        self.names_combo_box.currentTextChanged.connect(lambda: self.change_checkBoxs())
        self.save_btn.clicked.connect(lambda: self.save_change())
        self.add_new_name_btn.clicked.connect(lambda: self.add_new_name())


    def add_new_name(self):
        self.names[self.new_name.text()] = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.names_combo_box.addItem(self.new_name.text())

    def save_change(self):
        new_dost = []
        if self.checkBox.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_2.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_3.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_4.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_5.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_6.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_7.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_8.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_9.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        if self.checkBox_10.isChecked():
            new_dost.append('1')
        else:
            new_dost.append('0')

        self.names[self.names_combo_box.currentText()] = new_dost

        file = open("C:\\Users\\Feelan\\Desktop\\Prakt2\\names.txt", "w")
        for key in self.names.keys():
            file.write(key + ' ' + ' '.join(self.names[key]) + '\n')
        file.close()

        file = open("C:\\Users\\Feelan\\Desktop\\Prakt2\\names.txt", "r")
        for i in file.readlines():
            line = i.split()
            self.names[line[0]] = line[1:]
        file.close()



    def change_checkBoxs(self):

        if self.names[self.names_combo_box.currentText()][0] == '1':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        if self.names[self.names_combo_box.currentText()][1] == '1':
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)

        if self.names[self.names_combo_box.currentText()][2] == '1':
            self.checkBox_3.setChecked(True)
        else:
            self.checkBox_3.setChecked(False)

        if self.names[self.names_combo_box.currentText()][3] == '1':
            self.checkBox_4.setChecked(True)
        else:
            self.checkBox_4.setChecked(False)

        if self.names[self.names_combo_box.currentText()][4] == '1':
            self.checkBox_5.setChecked(True)
        else:
            self.checkBox_5.setChecked(False)

        if self.names[self.names_combo_box.currentText()][5] == '1':
            self.checkBox_6.setChecked(True)
        else:
            self.checkBox_6.setChecked(False)

        if self.names[self.names_combo_box.currentText()][6] == '1':
            self.checkBox_7.setChecked(True)
        else:
            self.checkBox_7.setChecked(False)

        if self.names[self.names_combo_box.currentText()][7] == '1':
            self.checkBox_8.setChecked(True)
        else:
            self.checkBox_8.setChecked(False)

        if self.names[self.names_combo_box.currentText()][8] == '1':
            self.checkBox_9.setChecked(True)
        else:
            self.checkBox_9.setChecked(False)

        if self.names[self.names_combo_box.currentText()][9] == '1':
            self.checkBox_10.setChecked(True)
        else:
            self.checkBox_10.setChecked(False)

    def clear_name(self):
        self.new_name.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Имя:"))
        self.add_new_name_btn.setText(_translate("MainWindow", "Добавить"))
        self.clear_new_name_btn.setText(_translate("MainWindow", "Очистить"))
        self.label.setText(_translate("MainWindow", "Пользователь:"))
        self.checkBox.setText(_translate("MainWindow", "Ё"))
        self.checkBox_2.setText(_translate("MainWindow", "У"))
        self.checkBox_3.setText(_translate("MainWindow", "Е"))
        self.checkBox_4.setText(_translate("MainWindow", "Ы"))
        self.checkBox_5.setText(_translate("MainWindow", "А"))
        self.checkBox_6.setText(_translate("MainWindow", "О"))
        self.checkBox_7.setText(_translate("MainWindow", "Э"))
        self.checkBox_8.setText(_translate("MainWindow", "Я"))
        self.checkBox_9.setText(_translate("MainWindow", "И"))
        self.checkBox_10.setText(_translate("MainWindow", "Ю"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить изменения"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()