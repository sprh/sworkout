import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer


class Entry(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('')

        self.name = QLabel(self)
        self.name.move(65, 30)
        self.name.setText('          Привет!               ')
        self.btn = QPushButton('', self)
        self.btn.resize(150, 70)
        self.btn.move(55, 65)

        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(10, self)

    / Users / sofya / Desktop / Kyrsu / project
    def timerEvent(self, e):

        if self.step >= 50:
            print(self.step)
            self.but()
            self.timer.stop()

        self.step = self.step + 1

    def but(self):
        print('a')
        self.clearFocus()
        self.name.setText('Расскажи нам о себе')
        self.btn.setText('Рассказать')
        self.btn.clicked.connect(self.check)

    def check(self):
        self.ok = Main()
        self.ok.show()
        self.close()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Введите информацию')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entry()
    ex.show()
    sys.exit(app.exec_())