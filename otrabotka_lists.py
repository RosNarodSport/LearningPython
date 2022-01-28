# Это будущий модуль показа элементов из списка? Как его сделать? ООП

my_list1 = ['1 Кролбаса', '1 Сыр', '1 Мясо', '1 Печень', '1 Молоко']
my_list2 = ['2 Кефир', '2 Сметана', '2 Огурцы', '2 Картофель', '2 Хлеб']
# i = 0
# while i < len(my_list2):
#     my_list1.append(my_list2[i])
#     i += 1

tt = len(my_list1)
for www in range(tt):
    print (my_list1[www])

print('\nВ одну строку через пробел или с сепаратором:')
print(*my_list1, sep = ', ')

print(*my_list1, sep = '\n')

print('\nС помощью карты map() в функции def print_my_list():')

def print_my_list(some_list_here):
    print('\n'.join(map(str, some_list_here)))

print('\nЗдесь вывожу с запуском функции + map() с передачей списка в функциюЖ\n')
print_my_list(my_list1)

class Get_this():
    def __init__(self, some_list, len_some_list):
        self.some_list = some_list
        self.len_some_list = len_some_list

    def get_my_list(self, my_list1):
        i = 0
        rez_list = []
        while i < self.len_some_list:
            rez_list.append(self.some_list[i])
            i += 1
        return rez_list

print('\nОтработка ООП (класс и функции):')
eee = Get_this(my_list1, len(my_list1))
eee.get_my_list(my_list1)

print('Что тут?\n Вывод в столбик')
print_my_list(eee.get_my_list(my_list1))
# print(','.join(map(str, eee)))

# Задача 2. Выбрать из двух списков первые элементы

print(my_list1)
print(my_list2)
lll = 0
mmm = 0
while lll < len(my_list1):
    print(my_list1[lll])
    print(my_list2[lll])
    sum = my_list1[lll] + ' + ' + my_list2[lll]
    print(sum)
    print('\n------------')
    lll += 1

full_list_of_hieroglyphs = [
    [1, '爱', 'ài', 'любить', '妈妈，我爱你。', 'HSK1'],
    [2, '八', 'bā', 'восемь', '他儿子今年八岁了。', 'HSK1'],
    [3, '爸爸', 'bàba', 'отец', '我爸爸是医生。', 'HSK1'],
    [4, '杯子', 'bēizi', 'стакан, чашка', '杯子里有茶。', 'HSK1']
]


def print_this(what_print):
    sss = 0
    while sss < len(what_print):
        print(what_print[sss])
        sss += 1


# print_this(full_list_of_hieroglyphs)
print('Старт')

# Метод позволит взять список (одна словарная статья) и показать.
# При этом я могу отключать отдельные жлементы списка (для управления показом)
def show_lists_in_my_lists(what_list):
    x = 0
    while x < len(what_list):
        newlist = what_list[x]
        y = 0
        while y < len(newlist):
            rez_list = newlist[y]
            a = 0
            # Метки временно установлены как переменные (вводиться будут через окно)
            # Задача меток - поймать элемент списка (показать или скрыть)
            rezult1 = True
            rezult2 = True
            rezult3 = False # Означает, что я поймал метку
            rezult4 = True
            rezult5 = True

            if newlist[y] == newlist[0] and rezult1 == False:
                print(f'\n----------------\nПоймал! {newlist[y]}')
            elif newlist[y] == newlist[1] and rezult1 == False:
                print(f'Поймал! {newlist[y]}') # Здесь и ниже ставлю функции, обрабатывающие это положение
            elif newlist[y] == newlist[2] and rezult2 == False:
                print(f'Поймал! {newlist[y]}')
            elif newlist[y] == newlist[3] and rezult3 == False:
                print(f'Поймал! {newlist[y]}')
            elif newlist[y] == newlist[4] and rezult4 == False:
                print(f'Поймал! {newlist[y]}')
            elif newlist[y] == newlist[5] and rezult5 == False:
                print(f'Поймал! {newlist[y]}')
            else:
                print(rez_list)
            y += 1
        x += 1



show_lists_in_my_lists(full_list_of_hieroglyphs)

big = full_list_of_hieroglyphs[3]
small = big[4]
print('Смотрим, что получилось')
print(small)
print(full_list_of_hieroglyphs[0][3])