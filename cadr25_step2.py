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
        MainWindow.resize(759, 519)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_for_progressBar_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_progressBar_2.setGeometry(QtCore.QRect(620, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_for_progressBar_2.setFont(font)
        self.label_for_progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_progressBar_2.setObjectName("label_for_progressBar_2")
        self.checkBox_show_hsk1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_hsk1.setGeometry(QtCore.QRect(620, 350, 81, 17))
        self.checkBox_show_hsk1.setChecked(True)
        self.checkBox_show_hsk1.setTristate(False)
        self.checkBox_show_hsk1.setObjectName("checkBox_show_hsk1")
        self.horizontalSlider_speed = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_speed.setGeometry(QtCore.QRect(600, 280, 131, 22))
        self.horizontalSlider_speed.setMinimum(100)
        self.horizontalSlider_speed.setMaximum(10000)
        self.horizontalSlider_speed.setSingleStep(100)
        self.horizontalSlider_speed.setPageStep(500)
        self.horizontalSlider_speed.setProperty("value", 2000)
        self.horizontalSlider_speed.setSliderPosition(2000)
        self.horizontalSlider_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_speed.setObjectName("horizontalSlider_speed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_for_horizontalSlider_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_for_horizontalSlider_speed.setGeometry(QtCore.QRect(608, 210, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_for_horizontalSlider_speed.setFont(font)
        self.label_for_horizontalSlider_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_horizontalSlider_speed.setObjectName("label_for_horizontalSlider_speed")
        self.horizontalSlider_size = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_size.setGeometry(QtCore.QRect(380, 280, 161, 22))
        self.horizontalSlider_size.setMinimum(12)
        self.horizontalSlider_size.setMaximum(48)
        self.horizontalSlider_size.setSingleStep(2)
        self.horizontalSlider_size.setSliderPosition(48)
        self.horizontalSlider_size.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_size.setObjectName("horizontalSlider_size")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(370, 80, 201, 21))
        self.progressBar.setMinimum(1)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(370, 50, 191, 31))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.radioButton_red = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_red.setGeometry(QtCore.QRect(410, 440, 101, 17))
        self.radioButton_red.setObjectName("radioButton_red")
        self.checkBox_show_translation = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_translation.setGeometry(QtCore.QRect(610, 110, 81, 16))
        self.checkBox_show_translation.setChecked(True)
        self.checkBox_show_translation.setObjectName("checkBox_show_translation")
        self.label_show_new_start_point = QtWidgets.QLabel(self.centralwidget)
        self.label_show_new_start_point.setGeometry(QtCore.QRect(370, 110, 191, 20))
        self.label_show_new_start_point.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_new_start_point.setObjectName("label_show_new_start_point")
        self.radioButton_blue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_blue.setGeometry(QtCore.QRect(410, 410, 101, 17))
        self.radioButton_blue.setObjectName("radioButton_blue")
        self.pushButton_start_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_all.setGeometry(QtCore.QRect(370, 20, 91, 31))
        self.pushButton_start_all.setObjectName("pushButton_start_all")
        self.label_check_new_start_point = QtWidgets.QLabel(self.centralwidget)
        self.label_check_new_start_point.setGeometry(QtCore.QRect(520, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_check_new_start_point.setFont(font)
        self.label_check_new_start_point.setObjectName("label_check_new_start_point")
        self.horizontalSlider_show_new_start_point = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_show_new_start_point.setGeometry(QtCore.QRect(370, 140, 131, 21))
        self.horizontalSlider_show_new_start_point.setMinimum(-1)
        self.horizontalSlider_show_new_start_point.setMaximum(99)
        self.horizontalSlider_show_new_start_point.setSliderPosition(-1)
        self.horizontalSlider_show_new_start_point.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_show_new_start_point.setObjectName("horizontalSlider_show_new_start_point")
        self.checkBox_show_hieroglyph = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_hieroglyph.setGeometry(QtCore.QRect(610, 50, 81, 17))
        self.checkBox_show_hieroglyph.setChecked(True)
        self.checkBox_show_hieroglyph.setObjectName("checkBox_show_hieroglyph")
        self.label_for_horlSlider_size = QtWidgets.QLabel(self.centralwidget)
        self.label_for_horlSlider_size.setGeometry(QtCore.QRect(380, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_for_horlSlider_size.setFont(font)
        self.label_for_horlSlider_size.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_horlSlider_size.setObjectName("label_for_horlSlider_size")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox_show_pinin = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_pinin.setGeometry(QtCore.QRect(610, 80, 81, 16))
        self.checkBox_show_pinin.setChecked(True)
        self.checkBox_show_pinin.setObjectName("checkBox_show_pinin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_for_horizontalSlider_size = QtWidgets.QLabel(self.centralwidget)
        self.label_for_horizontalSlider_size.setGeometry(QtCore.QRect(380, 210, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_for_horizontalSlider_size.setFont(font)
        self.label_for_horizontalSlider_size.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_horizontalSlider_size.setObjectName("label_for_horizontalSlider_size")
        self.radioButton_green = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_green.setGeometry(QtCore.QRect(410, 380, 101, 17))
        self.radioButton_green.setChecked(True)
        self.radioButton_green.setObjectName("radioButton_green")
        self.radioButton_black = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_black.setGeometry(QtCore.QRect(410, 350, 101, 17))
        self.radioButton_black.setChecked(False)
        self.radioButton_black.setObjectName("radioButton_black")
        self.pushButton_end = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_end.setGeometry(QtCore.QRect(470, 20, 101, 31))
        self.pushButton_end.setObjectName("pushButton_end")
        self.checkBox_show_phrase = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_phrase.setGeometry(QtCore.QRect(610, 140, 81, 16))
        self.checkBox_show_phrase.setChecked(True)
        self.checkBox_show_phrase.setObjectName("checkBox_show_phrase")
        self.label_HSK = QtWidgets.QLabel(self.centralwidget)
        self.label_HSK.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.label_HSK.setObjectName("label_HSK")
        self.label_hieroglyph = QtWidgets.QLabel(self.centralwidget)
        self.label_hieroglyph.setGeometry(QtCore.QRect(10, 40, 341, 101))
        self.label_hieroglyph.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_hieroglyph.setFont(font)
        self.label_hieroglyph.setStyleSheet("")
        self.label_hieroglyph.setScaledContents(True)
        self.label_hieroglyph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hieroglyph.setWordWrap(True)
        self.label_hieroglyph.setObjectName("label_hieroglyph")
        self.label_pinin = QtWidgets.QLabel(self.centralwidget)
        self.label_pinin.setGeometry(QtCore.QRect(10, 180, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pinin.setFont(font)
        self.label_pinin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pinin.setObjectName("label_pinin")
        self.label_translation = QtWidgets.QLabel(self.centralwidget)
        self.label_translation.setGeometry(QtCore.QRect(10, 230, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_translation.setFont(font)
        self.label_translation.setScaledContents(True)
        self.label_translation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_translation.setWordWrap(True)
        self.label_translation.setObjectName("label_translation")
        self.label_phrase = QtWidgets.QLabel(self.centralwidget)
        self.label_phrase.setGeometry(QtCore.QRect(10, 310, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_phrase.setFont(font)
        self.label_phrase.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phrase.setWordWrap(True)
        self.label_phrase.setObjectName("label_phrase")
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(310, 20, 31, 31))
        self.label_number.setObjectName("label_number")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(343, 20, 20, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(370, 170, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 759, 21))
        self.menuBar.setAutoFillBackground(True)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkBox_show_hieroglyph, self.checkBox_show_pinin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "25-й кадр (китайский язык)"))
        self.label_for_progressBar_2.setText(_translate("MainWindow", "Схема показа"))
        self.checkBox_show_hsk1.setText(_translate("MainWindow", "HSK1234"))
        self.label.setText(_translate("MainWindow", "Скорость показа"))
        self.label_for_horizontalSlider_speed.setText(_translate("MainWindow", "2.0 сек"))
        self.label_status.setText(_translate("MainWindow", "Статус"))
        self.radioButton_red.setText(_translate("MainWindow", "Красный цвет"))
        self.checkBox_show_translation.setText(_translate("MainWindow", "Перевод"))
        self.label_show_new_start_point.setText(_translate("MainWindow", "Начать с иероглифа под номером:"))
        self.radioButton_blue.setText(_translate("MainWindow", "Синий цвет"))
        self.pushButton_start_all.setText(_translate("MainWindow", "Старт показа"))
        self.label_check_new_start_point.setText(_translate("MainWindow", "#"))
        self.checkBox_show_hieroglyph.setText(_translate("MainWindow", "Иероглиф"))
        self.label_for_horlSlider_size.setText(_translate("MainWindow", "Размер иероглифа"))
        self.label_4.setText(_translate("MainWindow", "Показать"))
        self.checkBox_show_pinin.setText(_translate("MainWindow", "Пиньин"))
        self.label_2.setText(_translate("MainWindow", "Цвет показа"))
        self.label_for_horizontalSlider_size.setText(_translate("MainWindow", "电脑"))
        self.radioButton_green.setText(_translate("MainWindow", "Зеленый цвет"))
        self.radioButton_black.setText(_translate("MainWindow", "Черный цвет"))
        self.pushButton_end.setText(_translate("MainWindow", "Закрыть"))
        self.checkBox_show_phrase.setText(_translate("MainWindow", "Фраза"))
        self.label_HSK.setText(_translate("MainWindow", "HSK"))
        self.label_hieroglyph.setText(_translate("MainWindow", "文字 "))
        self.label_pinin.setText(_translate("MainWindow", "pinin"))
        self.label_translation.setText(_translate("MainWindow", "Перевод"))
        self.label_phrase.setText(_translate("MainWindow", "Фраза"))
        self.label_number.setText(_translate("MainWindow", "№"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())