# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Python_bigtest_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(566, 574)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.main_pushButton.setGeometry(QtCore.QRect(380, 330, 171, 23))
        self.main_pushButton.setObjectName("main_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 370, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.single_big_label = QtWidgets.QLabel(self.centralwidget)
        self.single_big_label.setGeometry(QtCore.QRect(20, 270, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.single_big_label.setFont(font)
        self.single_big_label.setObjectName("single_big_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 10, 171, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_for_spinBox = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_for_spinBox.setObjectName("label_for_spinBox")
        self.horizontalLayout.addWidget(self.label_for_spinBox)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(380, 50, 171, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_for_dateEdit = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_for_dateEdit.setObjectName("label_for_dateEdit")
        self.horizontalLayout_2.addWidget(self.label_for_dateEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 27), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(380, 90, 171, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_for_progressBar = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_for_progressBar.setFont(font)
        self.label_for_progressBar.setObjectName("label_for_progressBar")
        self.verticalLayout.addWidget(self.label_for_progressBar)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(99)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.frame_with_label1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_with_label1.setGeometry(QtCore.QRect(10, 200, 141, 78))
        self.frame_with_label1.setAcceptDrops(True)
        self.frame_with_label1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_with_label1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_with_label1.setObjectName("frame_with_label1")
        self.label_in_frame1 = QtWidgets.QLabel(self.frame_with_label1)
        self.label_in_frame1.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.label_in_frame1.setObjectName("label_in_frame1")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(380, 180, 171, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_for_horizontalSlider1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_for_horizontalSlider1.setObjectName("label_for_horizontalSlider1")
        self.horizontalLayout_3.addWidget(self.label_for_horizontalSlider1)
        self.horizontalSlider1 = QtWidgets.QSlider(self.horizontalLayoutWidget_3)
        self.horizontalSlider1.setMinimum(1)
        self.horizontalSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider1.setObjectName("horizontalSlider1")
        self.horizontalLayout_3.addWidget(self.horizontalSlider1)
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(190, 0, 171, 371))
        self.groupBox1.setObjectName("groupBox1")
        self.label_in_groupBox1 = QtWidgets.QLabel(self.groupBox1)
        self.label_in_groupBox1.setGeometry(QtCore.QRect(16, 22, 141, 331))
        self.label_in_groupBox1.setObjectName("label_in_groupBox1")
        self.label_RadBtn1 = QtWidgets.QLabel(self.centralwidget)
        self.label_RadBtn1.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_RadBtn1.setObjectName("label_RadBtn1")
        self.label_RadBtn2 = QtWidgets.QLabel(self.centralwidget)
        self.label_RadBtn2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_RadBtn2.setObjectName("label_RadBtn2")
        self.label_ChBox1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ChBox1.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.label_ChBox1.setObjectName("label_ChBox1")
        self.label_ChBox2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ChBox2.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.label_ChBox2.setObjectName("label_ChBox2")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(70, 20, 82, 17))
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(70, 60, 82, 17))
        self.radioButton2.setChecked(True)
        self.radioButton2.setObjectName("radioButton2")
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(70, 100, 81, 17))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(70, 140, 81, 16))
        self.checkBox2.setChecked(True)
        self.checkBox2.setObjectName("checkBox2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 80, 161, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 120, 161, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 160, 161, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 0, 161, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 370, 201, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/我.JPG"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.dialog_buttonBox_OK_Cancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.dialog_buttonBox_OK_Cancel.setGeometry(QtCore.QRect(10, 470, 156, 23))
        self.dialog_buttonBox_OK_Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttonBox_OK_Cancel.setCenterButtons(True)
        self.dialog_buttonBox_OK_Cancel.setObjectName("dialog_buttonBox_OK_Cancel")
        self.label_dialog_btnOK = QtWidgets.QLabel(self.centralwidget)
        self.label_dialog_btnOK.setGeometry(QtCore.QRect(20, 450, 47, 13))
        self.label_dialog_btnOK.setObjectName("label_dialog_btnOK")
        self.label_dialog_btn_Cancel = QtWidgets.QLabel(self.centralwidget)
        self.label_dialog_btn_Cancel.setGeometry(QtCore.QRect(100, 450, 47, 13))
        self.label_dialog_btn_Cancel.setObjectName("label_dialog_btn_Cancel")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(173, 420, 20, 101))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_main_pushButton = QtWidgets.QLabel(self.centralwidget)
        self.label_main_pushButton.setGeometry(QtCore.QRect(386, 242, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_main_pushButton.setFont(font)
        self.label_main_pushButton.setObjectName("label_main_pushButton")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(335, 430, 201, 51))
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 420, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_dialog_buttonBox_OK_Cancel = QtWidgets.QLabel(self.centralwidget)
        self.label_dialog_buttonBox_OK_Cancel.setGeometry(QtCore.QRect(20, 490, 151, 31))
        self.label_dialog_buttonBox_OK_Cancel.setObjectName("label_dialog_buttonBox_OK_Cancel")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(250, 470, 50, 64))
        self.dial.setObjectName("dial")
        self.label_dial = QtWidgets.QLabel(self.centralwidget)
        self.label_dial.setGeometry(QtCore.QRect(190, 480, 61, 41))
        self.label_dial.setObjectName("label_dial")
        self.pushButton_setBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setBack.setGeometry(QtCore.QRect(424, 490, 111, 41))
        self.pushButton_setBack.setObjectName("pushButton_setBack")
        self.pushButton_replace = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_replace.setGeometry(QtCore.QRect(340, 492, 75, 41))
        self.pushButton_replace.setObjectName("pushButton_replace")
        self.label.raise_()
        self.main_pushButton.raise_()
        self.line.raise_()
        self.single_big_label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.frame_with_label1.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.groupBox1.raise_()
        self.label_RadBtn1.raise_()
        self.label_RadBtn2.raise_()
        self.label_ChBox1.raise_()
        self.label_ChBox2.raise_()
        self.radioButton1.raise_()
        self.radioButton2.raise_()
        self.checkBox1.raise_()
        self.checkBox2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.dialog_buttonBox_OK_Cancel.raise_()
        self.label_dialog_btnOK.raise_()
        self.label_dialog_btn_Cancel.raise_()
        self.line_7.raise_()
        self.label_main_pushButton.raise_()
        self.listView.raise_()
        self.lineEdit.raise_()
        self.label_dialog_buttonBox_OK_Cancel.raise_()
        self.dial.raise_()
        self.label_dial.raise_()
        self.pushButton_setBack.raise_()
        self.pushButton_replace.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menuBar.setAutoFillBackground(True)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.main_pushButton, self.listView)
        MainWindow.setTabOrder(self.listView, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.dial)
        MainWindow.setTabOrder(self.dial, self.radioButton1)
        MainWindow.setTabOrder(self.radioButton1, self.radioButton2)
        MainWindow.setTabOrder(self.radioButton2, self.checkBox1)
        MainWindow.setTabOrder(self.checkBox1, self.checkBox2)
        MainWindow.setTabOrder(self.checkBox2, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.dateEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_pushButton.setText(_translate("MainWindow", "main_pushButton"))
        self.single_big_label.setText(_translate("MainWindow", "single_big_label"))
        self.label_for_spinBox.setText(_translate("MainWindow", "TextLabel"))
        self.label_for_dateEdit.setText(_translate("MainWindow", "TextLabel"))
        self.label_for_progressBar.setText(_translate("MainWindow", "label_for_prBar"))
        self.label_in_frame1.setText(_translate("MainWindow", "label_in_frame1"))
        self.label_for_horizontalSlider1.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox1.setTitle(_translate("MainWindow", "Группа 1"))
        self.label_in_groupBox1.setText(_translate("MainWindow", "str(zzz)"))
        self.label_RadBtn1.setText(_translate("MainWindow", "Пункт 1"))
        self.label_RadBtn2.setText(_translate("MainWindow", "Пункт 2"))
        self.label_ChBox1.setText(_translate("MainWindow", "Пункт 3"))
        self.label_ChBox2.setText(_translate("MainWindow", "Пункт 4"))
        self.radioButton1.setText(_translate("MainWindow", "Пункт 1"))
        self.radioButton2.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox2.setText(_translate("MainWindow", "CheckBox"))
        self.label_dialog_btnOK.setText(_translate("MainWindow", "TextLabel"))
        self.label_dialog_btn_Cancel.setText(_translate("MainWindow", "TextLabel"))
        self.label_main_pushButton.setText(_translate("MainWindow", "Текст"))
        self.label_dialog_buttonBox_OK_Cancel.setText(_translate("MainWindow", "TextLabel"))
        self.label_dial.setText(_translate("MainWindow", "label_dial"))
        self.pushButton_setBack.setText(_translate("MainWindow", "Вернуть все назад"))
        self.pushButton_replace.setText(_translate("MainWindow", "Залезть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
