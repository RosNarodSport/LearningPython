# import sys
#
# from PyQt5 import QtCore, QtWidgets, QtMultimedia
#
# app = QtWidgets.QApplication(sys.argv)
# filename = 'sound.mp3'
# fullpath = QtCore.QDir.current().absoluteFilePath(filename)
# url = QtCore.QUrl.fromLocalFile(fullpath)
# content = QtMultimedia.QMediaContent(url)
# player = QtMultimedia.QMediaPlayer()
# player.setMedia(content)
# player.play()