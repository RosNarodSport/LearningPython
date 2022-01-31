from functools import partial
from hieroglyphs import *
from hsk_selection_options import *

from PyQt5 import QtCore, Qt, QtGui
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import datetime

# pyuic5 -x Python_bigtest_all.ui -o Python_bigtest.py - для
# обновления кода моего окна надо выполнять регулярно

From, Window = uic.loadUiType("Python_bigtest_all.ui")

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()


# вызывать метод get_my_number_for_start_hsk(number). Или делать это прямо в методе!

def label_status_text_show_group():
    form.label_status.setText("<span style='color: #008000;'>Идет показ...</span>")
    form.label_status.setFont(QFont('Arial', 12))


def label_status_text_no_group():
    form.label_status.setText("<span style='color: #f00;'>Не выбрана группа HSK</span>")
    form.label_status.setFont(QFont('Arial', 12))


def label_status_text_show_is_done():
    form.label_status.setText("<span style='color: #0000ff;'>Показ завершен!</span>")
    form.label_status.setFont(QFont('Arial', 12))


def get_my_number_for_start_hsk():
    global start_hsk_show
    start_hsk_show_temporary = []
    if form.checkBox_show_hsk1.isChecked():
        start_hsk_show_temporary.extend(hsk1)
        start_hsk_show = start_hsk_show_temporary
        label_status_text_show_group()
    else:
        start_hsk_show = []
        label_status_text_no_group()

    return start_hsk_show

    if form.checkBox_show_hsk2.isChecked() == True:
        pass


def get_my_number_for_start_hsk2():
    global start_hsk_show
    start_hsk_show_temporary = []
    if form.checkBox_show_hsk2.isChecked() == True:
        start_hsk_show_temporary.extend(hsk2)
        start_hsk_show = start_hsk_show_temporary
        label_status_text_show_group()
    else:
        start_hsk_show = []
        label_status_text_no_group()
    return start_hsk_show

    # if form.checkBox_show_hsk3.isChecked() == True:
    #     pass
    #
    # if form.checkBox_show_hsk4.isChecked() == True:
    #     pass


# Отработка показа с управляемой задержкой speed. Прыгают цифры (не могу понять)
def show_me_hieroglyphs():
    if form.checkBox_show_hsk1.isChecked() == True:
        get_my_number_for_start_hsk()
        print('HSK1\n_________________\n', start_hsk_show)
    elif form.checkBox_show_hsk2.isChecked() == True:
        get_my_number_for_start_hsk2()
        print('HSK2\n_________________\n', start_hsk_show)
    else:
        label_status_text_no_group()

    # get_my_number_for_start_hsk()
    for i in range(0, len(start_hsk_show)):
        one_dictionary_entry = start_hsk_show[i]
        speed = increase_speed_show()
        QtCore.QTimer.singleShot(speed * i, partial(update, one_dictionary_entry, i))


def update(one_dictionary_entry, i):
    if i >= len(start_hsk_show):
        label_status_text_show_is_done()
    else:
        pass

    y = 0
    while y < len(one_dictionary_entry):
        form.label_number.setText(str(one_dictionary_entry[0]))
        checkbox_hieroglyph(str(one_dictionary_entry[1]))
        form.label_pinin.setText(str(one_dictionary_entry[2]))
        form.label_translation.setText(str(one_dictionary_entry[3]))
        form.label_phrase.setText(str(one_dictionary_entry[4]))
        form.label_HSK.setText(str(one_dictionary_entry[5]))
        y += 1

    form.progressBar.setMaximum(len(start_hsk_show))
    form.progressBar.setValue(i)

    set_time_end = datetime.datetime.now()  # Котроль выхода статьи (удалить)
    print(one_dictionary_entry[0], '-->', one_dictionary_entry[1], '-->', set_time_end)  # Котроль выхода статьи (удалить)


# Отработка показа - не показа элемента словарной статьи по checkBox нажатию
def checkbox_hieroglyph(value):
    form.label_hieroglyph.setText(str(value))  # Поставить в зависмиость от checkBox_show_hieroglyph


# Откат к начальным настройкам
def on_click_setBack():
    form.label_for_horizontalSlider_size.setText('1')
    form.horizontalSlider_size.setProperty("value", 12)

    form.label_hieroglyph.setFont(QFont('Arial', 12))

    form.label_for_spinBox.setText('1')
    form.progressBar.setProperty("value", 1)
    form.spinBox.setProperty("value", 1)
    form.dateEdit.setDateTime(QtCore.QDateTime(QDate.currentDate()))
    form.label_for_horizontalSlider_speed.setText('Задержка показа: 2.5 сек.')
    form.horizontalSlider_speed.setProperty("value", 2500)


def on_click():  # Проверка. Удалить
    form.label_main_pushButton.setText("Ясно")


def on_click_replace():  # Проверка. Удалить
    form.label_main_pushButton.setText("replace")


def horizontalSlider_size_Value():
    zzz = form.horizontalSlider_size.value()
    form.label_for_horizontalSlider_size.setText(str(zzz))

    if zzz > 6 and zzz < 50:
        form.label_for_horizontalSlider_size.setFont(QFont('Arial', zzz))
        form.label_hieroglyph.setFont(QFont('Arial', zzz))


def increase_character_size():
    aaa = form.spinBox.value()
    form.label_hieroglyph.setFont(QFont('Arial', aaa))


# def dateEdit_use():  # Проверка. Удалить
#     pass


# Метод управляет изменением скорости показа иероглифа
def increase_speed_show():
    speed_value = form.horizontalSlider_speed.value()
    speed_value = int(speed_value)
    form.label_for_horizontalSlider_speed.setText(f'{round(speed_value / 1000, 1)} сек')
    return speed_value


# Запуск прогона со списка конкретного HSK. Это тестирование работы checkBox'ов (потом удалить)

def checkBox_start_show_hsk1_method(value):
    if value == 2:
        print('Поставил метку HSK1')
        print(f'Должно быть 2. По факту: {form.checkBox_show_hsk1.checkState()}')
    else:
        print('______Снял метку HSK1')
        print(f'Должен быть 0. По факту: {form.checkBox_show_hsk1.checkState()}')


def checkBox_start_show_hsk2_method(value):
    if value == 2:
        print('Поставил метку HSK2')
        print(f'Должно быть 2. По факту: {form.checkBox_show_hsk2.checkState()}')
    else:
        print('______Снял метку HSK2')
        print(f'Должен быть 0. По факту: {form.checkBox_show_hsk2.checkState()}')


def checkBox_start_show_hsk3_method(value):
    if value == 2:
        print('Поставил метку HSK3')
        print(f'Должно быть 2. По факту: {form.checkBox_show_hsk3.checkState()}')
    else:
        print('______Снял метку HSK3')
        print(f'Должен быть 0. По факту: {form.checkBox_show_hsk3.checkState()}')


def checkBox_start_show_hsk4_method(value):
    if value == 2:
        print('Поставил метку HSK4')
        print(f'Должно быть 2. По факту: {form.checkBox_show_hsk4.checkState()}')
    else:
        print('______Снял метку HSK4')
        print(f'Должен быть 0. По факту: {form.checkBox_show_hsk4.checkState()}')

# Конец прогона со списка конкретного HSK. Это тестирование работы checkBox'ов (потом удалить)

def hieroglyphs():
    form.label_in_groupBox1.setText('我是')


# Проверка работы checkBox
def checkBox_show_hieroglyph_method(value):
    if value == False:
        print(f'НЕ показывать Иероглиф!')
        return value
    else:
        print('  Показать Иероглиф')
        return value


def checkBox_show_pinin_method(value):
    if value == False:
        print(f'НЕ показывать PININ!')
    else:
        print('  Показать PININ')


def checkBox_show_pfrase_method(value):
    if value == False:
        print(f'НЕ показывать ФРАЗУ!')
    else:
        print('  Показать ФРАЗУ')


def checkBox_show_translation_method(value):
    if value == False:
        print(f'НЕ показывать ПЕРЕВОД!')
    else:
        print('  Показать ПЕРЕВОД')


# Кнопка возврата к исходдным настройкам
form.pushButton_setBack.clicked.connect(on_click_setBack)

form.spinBox.valueChanged.connect(increase_character_size)
# form.dateEdit.dateTimeChanged.connect(dateEdit_use)

# Запуск показа статей
form.pushButton_start_all.clicked.connect(show_me_hieroglyphs)

# Слайдер управления размером иероглифа при показе
form.horizontalSlider_size.valueChanged.connect(horizontalSlider_size_Value)

# Слайдер управления скоростью показа статьи
form.horizontalSlider_speed.valueChanged.connect(increase_speed_show)

# Управление показом отдельных частей словарной статьи
form.checkBox_show_hieroglyph.stateChanged.connect(checkBox_show_hieroglyph_method)
form.checkBox_show_pinin.stateChanged.connect(checkBox_show_pinin_method)
form.checkBox_show_pfrase.stateChanged.connect(checkBox_show_pfrase_method)
form.checkBox_show_translation.stateChanged.connect(checkBox_show_translation_method)

# Управление запуском показа словарных статей с конкретной группы HSK
form.checkBox_show_hsk1.stateChanged.connect(checkBox_start_show_hsk1_method)
form.checkBox_show_hsk2.stateChanged.connect(checkBox_start_show_hsk2_method)
form.checkBox_show_hsk3.stateChanged.connect(checkBox_start_show_hsk3_method)
form.checkBox_show_hsk4.stateChanged.connect(checkBox_start_show_hsk4_method)

app.exec_()
