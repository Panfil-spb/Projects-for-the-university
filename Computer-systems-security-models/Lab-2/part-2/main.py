from PyQt5 import QtCore, QtGui, QtWidgets
import sys, openpyxl



class Ui_MainWindow(object):

    users = []
    users_name = []
    litters = []
    sheet = 0

    def __init__(self):
        file = "rules.xlsx"
        wb = openpyxl.load_workbook(file)
        self.sheet = wb['rule']
        self.users = self.sheet['A'][1:]
        self.users_name = [name.value for name in self.users]
        self.litters = []


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 14, 351, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.names_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.names_comboBox.setObjectName("names_comboBox")
        self.names_comboBox.addItems(self.users_name)

        self.horizontalLayout.addWidget(self.names_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Start_text = QtWidgets.QTextEdit(self.layoutWidget)
        self.Start_text.setObjectName("Start_text")
        self.verticalLayout.addWidget(self.Start_text)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.clear_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.New_text = QtWidgets.QTextEdit(self.centralwidget)
        self.New_text.setGeometry(QtCore.QRect(20, 310, 349, 218))
        self.New_text.setObjectName("New_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def add_function(self):
        self.clear_btn.clicked.connect(lambda: self.clear())
        self.start_btn.clicked.connect(lambda: self.start())

    def clear(self):
        self.Start_text.setText("")
        self.New_text.setText("")

    def start(self):
        input = self.Start_text.toPlainText()
        forbidden = set()
        users = self.users
        exists = False
        output = ""

        for user in users:
            if user.value == self.names_comboBox.currentText():
                exists = True
                for rule in self.sheet[user.row][1:]:
                    if rule.value == 0:
                        forbidden.add(self.sheet['1'][rule.column - 1].value.lower())
        if exists:
            for symbol in input:
                if symbol.lower() not in forbidden:
                    output += symbol
            self.New_text.setText(output)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение пользователя"))
        self.label.setText(_translate("MainWindow", "Пользователь:"))
        self.start_btn.setText(_translate("MainWindow", "Обработать"))
        self.clear_btn.setText(_translate("MainWindow", "Очистиь"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()