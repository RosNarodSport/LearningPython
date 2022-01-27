import sys
from functools import partial
from PyQt5 import QtCore, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        fire_cord = [1, '爱', 'ài', 'любить', '妈妈，我爱你。', 'HSK1']
        for i in range(0, len(fire_cord)):
                QtCore.QTimer.singleShot(3000*i, partial(self.update, fire_cord, i))

    def update(self, fire_cord, i):
        print(f'{fire_cord[i]=}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())