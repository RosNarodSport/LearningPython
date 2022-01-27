from functools import partial

from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QTime, QDate, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import time

# pyuic5 -x Python_bigtest_all.ui -o Python_bigtest.py - для
# обновления кода моего окна надо выполнять регулярно

From, Window = uic.loadUiType("Python_bigtest_all.ui")

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()


# Весь новый код размещать здесь

def on_click_setBack():
    form.label_main_pushButton.setText("Текст")
    form.label_for_horizontalSlider1.setText('1')
    form.label_main_pushButton.setFont(QFont('Arial', 12))
    form.label_for_spinBox.setText('1')
    form.progressBar.setProperty("value", 1)
    form.horizontalSlider1.setProperty("value", 1)
    form.spinBox.setProperty("value", 1)
    form.dateEdit.setDateTime(QtCore.QDateTime(QDate.currentDate()))
    form.label_in_groupBox1.setText('我')


def on_click():
    form.label_main_pushButton.setText("Ясно")


def on_click_replace():
    form.label_main_pushButton.setText("replace")


def horizontalSlider1_sliderValue():
    form.progressBar.setValue(form.horizontalSlider1.value())
    yyy = form.progressBar.value()

    zzz = form.horizontalSlider1.value()
    form.label_for_horizontalSlider1.setText(str(zzz))

    form.label_for_progressBar.setText(str(yyy))

    if yyy > 6 and yyy < 50:
        form.label_main_pushButton.setFont(QFont('Arial', yyy))
        form.label_in_groupBox1.setFont(QFont('Arial', yyy))


def spinBox_detail():
    aaa = form.spinBox.value()
    form.label_for_spinBox.setText(str(aaa))


def dateEdit_use():
    pass
    # form.dateEdit
    # www = str(form.dateEdit.value())
    # form.label_for_dateEdit.setText(www)


full_list_of_hieroglyphs = [
    [1, '爱', 'ài', 'любить', '妈妈，我爱你。', 'HSK1'],
    [2, '八', 'bā', 'восемь', '他儿子今年八岁了。', 'HSK1'],
    [3, '爸爸', 'bàba', 'отец', '我爸爸是医生。', 'HSK1'],
    [4, '杯子', 'bēizi', 'стакан, чашка', '杯子里有茶。', 'HSK1']
]


def hieroglyphs():
    form.label_in_groupBox1.setText('我是')

def show_me_hieroglyphs():
    for i in range(0, len(full_list_of_hieroglyphs)):
            QtCore.QTimer.singleShot(2000*i, partial(update, full_list_of_hieroglyphs, i))

def update(sss, i):
    ddd = full_list_of_hieroglyphs[i]
    print(*ddd, sep='\n')
    # form.label_in_groupBox1.setText(str(ddd))
    for i in full_list_of_hieroglyphs:
        form.label_in_groupBox1.setText(" \n".join(str(ddd))) # не совсем то! Мне надо выводить по инндексу

# show_me_hieroglyphs()

form.main_pushButton.clicked.connect(on_click)
# form.pushButton_replace.clicked.connect(hieroglyphs)
form.pushButton_replace.clicked.connect(show_me_hieroglyphs)

form.pushButton_setBack.clicked.connect(on_click_setBack)
form.horizontalSlider1.valueChanged.connect(horizontalSlider1_sliderValue)
form.spinBox.valueChanged.connect(spinBox_detail)
form.dateEdit.dateTimeChanged.connect(dateEdit_use)

app.exec_()
