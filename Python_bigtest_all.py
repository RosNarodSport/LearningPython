from functools import *

import media_sound
from hieroglyphs import *
from hsk_selection_options import *

from PyQt5 import QtCore, Qt, QtGui, QtMultimedia
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

    if form.checkBox_show_hsk1.isChecked() == True:
        if form.checkBox_show_hsk2.isChecked() == True:
            if form.checkBox_show_hsk3.isChecked() == True:
                if form.checkBox_show_hsk4.isChecked() == True:
                    start_hsk_show = []
                    start_hsk_show_temporary.extend(hsk1)
                    start_hsk_show_temporary.extend(hsk2)
                    start_hsk_show_temporary.extend(hsk3)
                    start_hsk_show_temporary.extend(hsk4)

                    start_hsk_show = start_hsk_show_temporary  # Получили и отдали список hsk 1-2-3-4
                    label_status_text_show_group()
                else:
                    start_hsk_show = []
                    label_status_text_no_group()
            else:
                start_hsk_show = []
                label_status_text_no_group()
        else:
            start_hsk_show = []
            label_status_text_no_group()
    else:
        start_hsk_show = []
        label_status_text_no_group()

    # if form.checkBox_show_hsk1.isChecked() == True:
    #     if form.checkBox_show_hsk2.isChecked() == True:
    #         if form.checkBox_show_hsk3.isChecked() == True:
    #             if form.checkBox_show_hsk4.isChecked() == False:
    #                 start_hsk_show = []
    #                 start_hsk_show_temporary.extend(hsk1)
    #                 start_hsk_show_temporary.extend(hsk2)
    #                 start_hsk_show_temporary.extend(hsk3)
    #
    #                 start_hsk_show = start_hsk_show_temporary  # Получили и отдали список hsk 1-2-3
    #                 label_status_text_show_group()
    #             else:
    #                 start_hsk_show = []
    #                 label_status_text_no_group()
    #         else:
    #             start_hsk_show = []
    #             label_status_text_no_group()
    #     else:
    #         start_hsk_show = []
    #         label_status_text_no_group()
    # else:
    #     start_hsk_show = []
    #     label_status_text_no_group()
    #
    # if form.checkBox_show_hsk1.isChecked() == True:
    #     if form.checkBox_show_hsk2.isChecked() == True:
    #         if form.checkBox_show_hsk4.isChecked() == True:
    #             if form.checkBox_show_hsk3.isChecked() == False:
    #                 start_hsk_show = []
    #                 start_hsk_show_temporary.extend(hsk1)
    #                 start_hsk_show_temporary.extend(hsk2)
    #                 start_hsk_show_temporary.extend(hsk4)
    #
    #                 start_hsk_show = start_hsk_show_temporary  # Получили и отдали список hsk 1-2-4
    #                 label_status_text_show_group()
    #             else:
    #                 start_hsk_show = []
    #                 label_status_text_no_group()
    #         else:
    #             start_hsk_show = []
    #             label_status_text_no_group()
    #     else:
    #         start_hsk_show = []
    #         label_status_text_no_group()
    # else:
    #     start_hsk_show = []
    #     label_status_text_no_group()
    #
    # if form.checkBox_show_hsk1.isChecked() == True:
    #     if form.checkBox_show_hsk3.isChecked() == True:
    #         if form.checkBox_show_hsk4.isChecked() == True:
    #             if form.checkBox_show_hsk2.isChecked() == False:
    #                 start_hsk_show = []
    #                 start_hsk_show_temporary.extend(hsk1)
    #                 start_hsk_show_temporary.extend(hsk3)
    #                 start_hsk_show_temporary.extend(hsk4)
    #
    #                 start_hsk_show = start_hsk_show_temporary  # Получили и отдали список hsk 1-3-4
    #                 label_status_text_show_group()
    #             else:
    #                 start_hsk_show = []
    #                 label_status_text_no_group()
    #         else:
    #             start_hsk_show = []
    #             label_status_text_no_group()
    #     else:
    #         start_hsk_show = []
    #         label_status_text_no_group()
    # else:
    #     start_hsk_show = []
    #     label_status_text_no_group()
    #
    # if form.checkBox_show_hsk2.isChecked() == True:
    #     if form.checkBox_show_hsk3.isChecked() == True:
    #         if form.checkBox_show_hsk4.isChecked() == True:
    #             if form.checkBox_show_hsk1.isChecked() == False:
    #                 start_hsk_show = []
    #                 start_hsk_show_temporary.extend(hsk2)
    #                 start_hsk_show_temporary.extend(hsk3)
    #                 start_hsk_show_temporary.extend(hsk4)
    #
    #                 start_hsk_show = start_hsk_show_temporary  # Получили и отдали список hsk 2-3-4
    #                 label_status_text_show_group()
    #             else:
    #                 start_hsk_show = []
    #                 label_status_text_no_group()
    #         else:
    #             start_hsk_show = []
    #             label_status_text_no_group()
    #     else:
    #         start_hsk_show = []
    #         label_status_text_no_group()
    # else:
    #     start_hsk_show = []
    #     label_status_text_no_group()


def stop_showing():
    if form.radioButton_stop_showing.isChecked():
        print('СТОП показ! radioButton_stop_showing')
    else:
        print('Не сработала метка radioButton_stop_showing')


def start_showing():
    if form.radioButton_start_showing.isChecked():
        print('НАЧНИ показ! radioButton_start_showing')
    else:
        print('Нес работала метка radioButton_start_showing')


def show_me_hieroglyphs():
    # Тут проверка нужна, иначе повторное нажатие на кнопку СТАРТ
    # приводит к смешению показов словарных статей

    get_my_number_for_start_hsk()  # Поступил правильный лист для демонстрации
    print(len(start_hsk_show), start_hsk_show)
    # Временная заглушка 11. Не понимаю, почему она необходимо (где-то сбой)
    # Связь м.б. в формировании списков HSK в методе get_my_number_for_start_hsk()
    # 12 - при списке в 1200 статей - это связь
    new_point_for_show = int((len(start_hsk_show) * (show_new_start_point() / 100) + 12))

    for i in range(new_point_for_show, len(start_hsk_show)):
        one_dictionary_entry = start_hsk_show[i]
        speed = increase_speed_show()
        QtCore.QTimer.singleShot(speed * (i - new_point_for_show), partial(update, one_dictionary_entry, i))


def sound():
    filename = 'sound.mp3'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    url = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(url)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()


# Смена цвета словарной статьи
def new_color():
    if form.radioButton_black.isChecked():
        set_new_color = '#000;'
    if form.radioButton_green.isChecked():
        set_new_color = '#008000;'
    if form.radioButton_blue.isChecked():
        set_new_color = '#0000ff;'
    if form.radioButton_red.isChecked():
        set_new_color = '#f00;'
    return set_new_color


def update(one_dictionary_entry, i):
    if i >= len(start_hsk_show) - 1:
        label_status_text_show_is_done()
    else:
        pass
    y = 0
    set_new_color = 1
    while y < len(one_dictionary_entry):
        form.label_number.setText(str(one_dictionary_entry[0]))
        form.label_hieroglyph.setText(f"<span style='color: {new_color()}'>{str(one_dictionary_entry[1])}</span>")
        form.label_pinin.setText(f"<span style='color: {new_color()}'>{str(one_dictionary_entry[2])}</span>")
        form.label_translation.setText(f"<span style='color: {new_color()}'>{str(one_dictionary_entry[3])}</span>")
        form.label_phrase.setText(f"<span style='color: {new_color()}'>{str(one_dictionary_entry[4])}</span>")
        form.label_HSK.setText(f"<span style='color: {new_color()}'>{str(one_dictionary_entry[5])}</span>")
        y += 1

    form.progressBar.setMaximum(len(start_hsk_show))
    form.progressBar.setValue(i)

    set_time_end = datetime.datetime.now()  # Котроль выхода статьи (удалить тест)
    print('Итерация: ', i + 1, ' - ', one_dictionary_entry[0], ' - ', (i + 1) - (one_dictionary_entry[0]),
          ' - ', one_dictionary_entry[1], ' - ', set_time_end, ' - ',
          int(datetime.datetime.now().timestamp()))  # Котроль выхода статьи (удалить)


# Отработка "показа - не показа" элемента словарной статьи по checkBox нажатию
def checkbox_hieroglyph(value):
    form.label_hieroglyph.setText(str(value))  # Поставить в зависмиость от checkBox_show_hieroglyph


def on_click():  # Проверка. Удалить
    form.label_main_pushButton.setText("Ясно")


def on_click_replace():  # Проверка. Удалить
    form.label_main_pushButton.setText("replace")


def horizontalSlider_size_Value():
    zzz = form.horizontalSlider_size.value()

    if zzz > 6 and zzz < 50:
        form.label_hieroglyph.setFont(QFont('Arial', zzz))


def increase_character_size():
    aaa = form.spinBox.value()
    form.label_hieroglyph.setFont(QFont('Arial', aaa))


# def dateEdit_use():  # Проверка. Удалить
#     pass


# Метод управляет изменением скорости показа иероглифа. Где-то здесь ошибка, искажающая вывод словарных статей
def increase_speed_show():
    speed_value = form.horizontalSlider_speed.value()
    # speed_value = int(speed_value)
    form.label_for_horizontalSlider_speed.setText(f'{round(speed_value / 1000, 2)} сек')
    return speed_value


# Метод управляет выбором места начала показа словарной статьи.
# Связь с label СТАТУС
def show_new_start_point():
    new_point_for_show = form.horizontalSlider_show_new_start_point.value()
    new_point_for_show = int(new_point_for_show)
    form.label_check_new_start_point.setText(f'-> {new_point_for_show + 1}')
    return new_point_for_show


# Запуск прогона со списка конкретного HSK. Это тестирование работы checkBox'ов (потом удалить)

def checkBox_start_show_hsk1_method(value):
    if value == 2:
        print('Поставил метку HSK1')
    else:
        print('______Снял метку HSK1')


def checkBox_start_show_hsk2_method(value):
    if value == 2:
        print('Поставил метку HSK2')
    else:
        print('______Снял метку HSK2')


def checkBox_start_show_hsk3_method(value):
    if value == 2:
        print('Поставил метку HSK3')
    else:
        print('______Снял метку HSK3')


def checkBox_start_show_hsk4_method(value):
    if value == 2:
        print('Поставил метку HSK4')
    else:
        print('______Снял метку HSK4')


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

# Управление точкой запуска просмотра
form.horizontalSlider_show_new_start_point.valueChanged.connect(show_new_start_point)

# Управление паузой и снятием с паузы
form.radioButton_start_showing.clicked.connect(start_showing)
form.radioButton_stop_showing.clicked.connect(stop_showing)

# Управление цветом показа словарных статей. Задача: Вставить в показ
form.radioButton_black.clicked.connect(new_color)
form.radioButton_green.clicked.connect(new_color)
form.radioButton_blue.clicked.connect(new_color)
form.radioButton_red.clicked.connect(new_color)

# Проверка работы кнопки с выводом звука
# form.pushButton_sound.clicked.connect(media_sound)

app.exec_()
