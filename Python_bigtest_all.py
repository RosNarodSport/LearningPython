from functools import partial
from hieroglyphs import full_list_of_hieroglyphs
from PyQt5 import QtCore, Qt
from PyQt5 import uic
from PyQt5.QtCore import QTime, QDate, QTimer
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


# Весь новый код размещать здесь

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


def on_click():
    form.label_main_pushButton.setText("Ясно")


def on_click_replace():
    form.label_main_pushButton.setText("replace")


def horizontalSlider_size_Value():
    zzz = form.horizontalSlider_size.value()
    form.label_for_horizontalSlider_size.setText(f'Размер иероглифа: {str(zzz)}')

    if zzz > 6 and zzz < 50:
        form.label_main_pushButton.setFont(QFont('Arial', zzz))
        form.label_hieroglyph.setFont(QFont('Arial', zzz))


def increase_character_size():
    aaa = form.spinBox.value()
    form.label_hieroglyph.setFont(QFont('Arial', aaa))


def dateEdit_use():
    pass
    # form.dateEdit
    # www = str(form.dateEdit.value())
    # form.label_for_dateEdit.setText(www)


full_list_of_hieroglyphs1 = [
    [1, '爱', 'ài', 'любить', '妈妈，我爱你。', 'HSK1'],
    [2, '八', 'bā', 'восемь', '他儿子今年八岁了。', 'HSK1'],
    [3, '爸爸', 'bàba', 'отец', '我爸爸是医生。', 'HSK1'],
    [4, '杯子', 'bēizi', 'стакан, чашка', '杯子里有茶。', 'HSK1'],
    [5, '北京', 'Běijīng', 'Пекин', '我住在北京。', 'HSK1'],
    [6, '本', 'běn', 'применяется при счете книг', '桌子上有一本书。', 'HSK1'],
    [7, '不客气', 'bú kèqi', 'Не стоит.', '甲：谢谢你！乙：不客气。', 'HSK1'],
    [8, '不', 'bù', 'не, нет', '我不是学生。', 'HSK1'],
    [9, '菜', 'cài', 'овощи', '我去超市买点儿菜。', 'HSK1'],
    [10, '茶', 'chá', 'чай', '请喝杯茶吧。', 'HSK1'],
    [11, '吃', 'chī', 'кушать, есть', '请吃点儿米饭。', 'HSK1'],
    [12, '出租车', 'chūzūchē', 'такси', '我们坐出租车去火车站。', 'HSK1'],
    [13, '打电话', 'dǎdiànhuà', 'звонить или говорить по телефону', '他在打电话呢。', 'HSK1'],
    [14, '大', 'dà', 'большой, крупный', '这个苹果很大。', 'HSK1'],
    [15, '的', 'de', 'присоединяет определение', '这是我的书。', 'HSK1'],
    [16, '点', 'diǎn', '(который) час', '现在是下午 3点20。', 'HSK1'],
    [17, '电脑', 'diànnǎo', 'компьютер', '我买了个电脑。', 'HSK1'],
    [18, '电视', 'diànshì', 'телевизор', '妈妈在看电视。', 'HSK1'],
    [19, '电影', 'diànyǐng', 'кинофильм', '我喜欢看电影。', 'HSK1'],
    [20, '东西', 'dōngxi', 'вещь, предмет', '我在商店买了很多东西。', 'HSK1']
]


# Метод управляет изменением скорости показа иероглифа
def increase_speed_show():
    speed_value = form.horizontalSlider_speed.value()
    speed_value = int(speed_value)
    form.label_for_horizontalSlider_speed.setText(f'Задержка показа: {round(speed_value / 1000, 2)} сек.')
    return speed_value


# Отработка показа с управляемой задержкой speed
def show_me_hieroglyphs():
    set_time_at_start = datetime.datetime.now().time()  # Котроль выхода статьи (удалить)
    print(f'\n__________________Отсечка: {set_time_at_start}')  # Котроль выхода статьи (удалить)

    for i in range(0, len(full_list_of_hieroglyphs)):
        one_dictionary_entry = full_list_of_hieroglyphs[i]
        speed = increase_speed_show()
        QtCore.QTimer.singleShot(speed * i, partial(update, one_dictionary_entry, i))


# Отработка показа - не показа элемента соварной статьи по checkBox нажатию
def checkbox_hieroglyph(value):
    form.label_hieroglyph.setText(str(value))  # Поставить в зависмиость от checkBox_show_hieroglyph


def update(one_dictionary_entry, i):
    # form.label_hieroglyph.setAlignment(Qt.AlignCenter)
    print(f'\nЭто выход с позиции progress :{i}')
    #
    # set_time_at_start = datetime.datetime.now().time()  # Котроль выхода статьи (удалить)
    # print(f'\n__________________Отсечка: {set_time_at_start}')  # Котроль выхода статьи (удалить)
    y = 0
    while y < len(one_dictionary_entry):
        form.label_number.setText(str(one_dictionary_entry[0]))
        checkbox_hieroglyph(str(one_dictionary_entry[1]))
        # if checkBox_show_hieroglyph(form.value) == True:
        # form.label_hieroglyph.setText(str(one_dictionary_entry[1]))
        # else:
        #     form.label_hieroglyph.setText('Нет ничего')

        form.label_pinin.setText(str(one_dictionary_entry[2]))
        form.label_translation.setText(str(one_dictionary_entry[3]))
        form.label_phrase.setText(str(one_dictionary_entry[4]))
        form.label_HSK.setText(str(one_dictionary_entry[5]))
        y += 1

    form.progressBar.setMaximum(len(full_list_of_hieroglyphs))
    form.progressBar.setValue(i)

    set_time_end = datetime.datetime.now().time()  # Котроль выхода статьи (удалить)

    print(f'\n__________________Завершено: {set_time_end}')  # Котроль выхода статьи (удалить)


def hieroglyphs():
    form.label_in_groupBox1.setText('我是')


# Проверка работы checkBock
def checkBox_show_hieroglyph(value):
    if value == False:
        print(f'НЕ показывать Иероглиф!')
        return value
    else:
        print('  Показать Иероглиф')
        return value


def checkBox_show_pinin(value):
    if value == False:
        print(f'НЕ показывать PININ!')
    else:
        print('  Показать PININ')


def checkBox_show_pfrase(value):
    if value == False:
        print(f'НЕ показывать ФРАЗУ!')
    else:
        print('  Показать ФРАЗУ')


def checkBox_show_translation(value):
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
form.checkBox_show_hieroglyph.stateChanged.connect(checkBox_show_hieroglyph)
form.checkBox_show_pinin.stateChanged.connect(checkBox_show_pinin)
form.checkBox_show_pfrase.stateChanged.connect(checkBox_show_pfrase)
form.checkBox_show_translation.stateChanged.connect(checkBox_show_translation)

app.exec_()
