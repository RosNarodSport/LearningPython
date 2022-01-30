from functools import partial
from hieroglyphs import *
from PyQt5 import QtCore, Qt
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

# Блок для работы со списками иероглифов из файла hieroglyphs.py


# Поставить if и в зависимости от vaqlue checkBoxHSK помещать int в переменную number,
# вызывать метод get_my_number_for_start_hsk(number). Или делать это прямо в методе!

def get_my_number_for_start_hsk():
    global start_hsk_show
    if form.checkBox_show_hsk1.isChecked() == True:
        start_hsk_show = hsk1
        print(f'Что if :{form.checkBox_show_hsk1.isChecked()}')
    else:
        print(f'Что else  :{form.checkBox_show_hsk1.isChecked()}')
        print('Сняли метку - False')
    return start_hsk_show

get_my_number_for_start_hsk()

# Отработка показа с управляемой задержкой speed
def show_me_hieroglyphs():
    set_time_at_start_metod_show_me_hieroglyphs = datetime.datetime.now().time()
    print(f'\n__________________Старт метода show_me_hieroglyphs: {0}')

    for i in range(0, 150):
        one_dictionary_entry = hsk1[i]
        speed = increase_speed_show()
        QtCore.QTimer.singleShot(speed * i, partial(update, one_dictionary_entry, i))


# Отработка показа - не показа элемента словарной статьи по checkBox нажатию
def checkbox_hieroglyph(value):
    form.label_hieroglyph.setText(str(value))  # Поставить в зависмиость от checkBox_show_hieroglyph


def update(one_dictionary_entry, i):
    set_time_at_start = datetime.datetime.now().time()  # Котроль выхода статьи (удалить)
    print(f'\n__________________Старт работы метода update: {set_time_at_start}')  # Котроль выхода статьи (удалить)
    print(f'\nЭто выход с позиции progress :{i}')
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

    set_time_end = datetime.datetime.now().time()  # Котроль выхода статьи (удалить)
    print(f'\n__________________Завершено: {set_time_end}')  # Котроль выхода статьи (удалить)


# form.checkBox_show_hsk1.stateChanged.connect(checkBox_start_show_hsk1_method)
# form.checkBox_show_hsk2.stateChanged.connect(checkBox_start_show_hsk2_method)
# form.checkBox_show_hsk3.stateChanged.connect(checkBox_start_show_hsk3_method)
# form.checkBox_show_hsk4.stateChanged.connect(checkBox_start_show_hsk4_method)

# Откат к начальным настройкам
def on_click_setBack():
    form.label_main_pushButton.setText("Текст")
    form.label_for_horizontalSlider_size.setText('1')
    form.horizontalSlider_size.setProperty("value", 12)

    form.label_main_pushButton.setFont(QFont('Arial', 12))
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


def dateEdit_use():  # Проверка. Удалить
    pass
    # form.dateEdit
    # www = str(form.dateEdit.value())
    # form.label_for_dateEdit.setText(www)


# Метод управляет изменением скорости показа иероглифа
def increase_speed_show():
    speed_value = form.horizontalSlider_speed.value()
    speed_value = int(speed_value)
    form.label_for_horizontalSlider_speed.setText(f'{round(speed_value / 1000, 1)} сек')
    return speed_value


# Запуск прогона со списка конкретного HSK

def checkBox_start_show_hsk1_method(value):
    if value == False:
        print('Стяли метку HSK1')
    else:
        print('Поставили метку HSK1')


def checkBox_start_show_hsk2_method(value):
    if value == False:
        print('Стяли метку HSK2')
    else:
        print('Поставили метку HSK2')


def checkBox_start_show_hsk3_method(value):
    if value == False:
        print('Стяли метку HSK3')
    else:
        print('Поставили метку HSK3')


def checkBox_start_show_hsk4_method(value):
    if value == False:
        print('Стяли метку HSK4')
    else:
        print('Поставили метку HSK4')

# get_my_number_for_start_hsk должен передать список!!! первый элемент!!! int
print(f'Это отсечка для показа HSK с определенного места :{get_my_number_for_start_hsk}')





def hieroglyphs():
    form.label_in_groupBox1.setText('我是')


# Проверка работы checkBock
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


form.main_pushButton.clicked.connect(on_click)
form.pushButton_setBack.clicked.connect(on_click_setBack)

form.spinBox.valueChanged.connect(increase_character_size)
form.dateEdit.dateTimeChanged.connect(dateEdit_use)

# Запуск показа статей
form.pushButton_replace.clicked.connect(show_me_hieroglyphs)

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
