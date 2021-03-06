import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer, QRect
from PyQt5.QtGui import QPixmap, QFont
import urllib.request

imt = 0


class Entry(QWidget):  # первая страница, слоган, название
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tr = False
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('')
        url = 'http://www.krunchtoday.com/images/august2018/columnist/swetha-bhatia.jpg'
        img = urllib.request.urlopen(url).read()
        out = open("img.jpg", "wb")
        out.write(img)
        out.close()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("img.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.name = QLabel(self)
        self.name.setGeometry(QRect(65, 40, 150, 30))
        self.name.setText('')
        self.name1 = QLabel(self)
        self.name1.setGeometry(QRect(65, 40, 250, 200))
        self.name.setFont(QFont("Helvetica", 25, QFont.Bold))
        self.bnt = QPushButton('Начать', self)  # перебрасывает на следующую
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.setGeometry(QRect(65, 220, 90, 40))
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(10, self)
        self.bnt.clicked.connect(self.check)

    def timerEvent(self, e):  # название приложения 'печатается', после через некоторое время
        # выводится слоган
        if self.step / 10 < 9 and self.step / 10 == int(self.step / 10):
            st = 'SWORKტUT'[:int(self.step / 10)]
            self.name.setText(st)
        if self.step >= 120:
            self.name1.setText('Вам не будет никаких\nоправданий, если вы\nне будете делать\n'
                               'физические упражнения!')
            self.name1.setFont(QFont("Times", 20, QFont.Bold))
            self.name1.setStyleSheet('color: black')
            self.but()
            self.timer.stop()
        self.step = self.step + 1

    def but(self):
        self.clearFocus()

    def check(self):
        self.ok = Info()
        self.ok.show()
        self.close()


class Info(QWidget):  # ифнормация о возрасте и поле пользователя
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Введите информацию')
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(QRect(140, 20, 40, 24))
        self.spinBox.setMaximum(70)  # ограничения по возрасту -- от 14 до 70 лет
        self.spinBox.setMinimum(14)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 20, 150, 20))
        self.label.setText("Сколько вам лет?")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(20, 70, 85, 20))
        self.label_2.setText("Ваш пол")
        self.radioButton = QRadioButton('Женский', self)  # только 2 варианта
        self.radioButton.setGeometry(QRect(140, 80, 85, 20))
        self.radioButton_2 = QRadioButton('Мужской', self)
        self.radioButton_2.setGeometry(QRect(140, 60, 85, 20))
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(120, 115, 85, 20))
        self.pushButton.setText("Далее")
        self.pushButton.setStyleSheet("background-color: grey")
        self.pushButton.clicked.connect(self.click)

    def click(self):
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.no()  # не все ввели -- диалоговое окно
        else:
            self.ok = Info_Main()
            self.ok.show()
            self.close()

    def no(self):
        QMessageBox.about(self, "Ошибка!", 'Вы не все ввели!')  # уведомление об ошибке


class Info_Main(QWidget):  # основная информация -- рост, вес
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('И еще немного...')
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(160, 115, 80, 20))
        self.pushButton.setText("Далее") # переход к рассчету ИМТ
        self.pushButton.clicked.connect(self.next)
        self.pushButton1 = QPushButton(self)
        self.pushButton1.setGeometry(QRect(70, 115, 80, 20))
        self.pushButton1.setText("Назад")  # переход обратно
        self.pushButton1.clicked.connect(self.back)
        self.pushButton1.setStyleSheet("background-color: grey")
        self.pushButton.setStyleSheet("background-color: grey")
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(QRect(140, 20, 70, 24))
        self.spinBox.setMaximum(220.0)
        self.spinBox.setMinimum(130.0)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 20, 150, 20))
        self.label.setText("Какой у вас рост?")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(20, 70, 85, 24))
        self.label_2.setText("А вес?")
        self.spinBox1 = QDoubleSpinBox(self)
        self.spinBox1.setGeometry(QRect(140, 70, 70, 24))
        self.spinBox1.setMaximum(250.0)
        self.spinBox1.setMinimum(40.0)

    def back(self):  # переход к вводу пола и возраста
        self.ok = Info()
        self.ok.show()
        self.close()

    def next(self):  # рассчет ИМТ, переход далее
        global imt
        imt = round(float(self.spinBox1.value()) / ((int(self.spinBox.value())/100)**2), 1)
        self.okno = Down()
        self.okno.show()
        self.close()


class Down(QWidget):  # загрузка
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 100, 200, 25)
        self.timer = QBasicTimer()
        self.timer.start(20, self)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 20, 240, 65))
        self.label.setText("Рассчитываем индекс массы тела...")
        self.step = 0
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Загрузка...')

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.ok = IMT()
            self.ok.show()
            self.close()

        self.step = self.step + 1
        self.pbar.setValue(self.step)


class IMT(QWidget):  # рассчет ИМТ, совет
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global imt
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Ваш ИМТ!')
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(200, 20, 40, 40))
        self.pushButton.setText("?")
        self.pushButton.clicked.connect(self.what)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(100, 20, 150, 20))
        self.label.setText(('ИМТ ' + str(imt)))
        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(20, 60, 200, 40))
        self.bnt = QPushButton(self)
        self.bnt.setGeometry(QRect(30, 110, 200, 30))
        self.bnt.setText("Рассчитать программу")  # переход к программе
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.clicked.connect(self.click)
        if imt < 18.5:  # вывод значения, совета
            self.label1.setText('Ваш ИМТ ниже среднего!\nСоветуем набрать вес!')
        elif 25.0 >= imt >= 18.5:
            self.label1.setText('Ваш показатель ИМТ в норме,\nпоздравляем!')
        elif 25.0 < imt <= 28.0:
            self.lebel1.setText('Ваш ИМТ выше среднего! Стоит задуматься.')
        elif 28.0 < imt <= 32.0:
            self.label1.setText('ИМТ высокий! Задумайтесь\nо похудении!')
        else:
            self.label1.setText('Очень высокий ИМТ! Вам явно\nстоит сбросить вес!')

    def what(self):  # что такое имт?
        QMessageBox.about(self, "Title", 'ИМТ: вес / рост в квадрате.\n'
                                         'Руководствуясь только показателем ИМТ, вы не можете '
                                         'определить имеющееся "скрытое ожирение". Даже при '
                                         'нормальном показателе ИМТ люди могут иметь много'
                                         'жира и мало мышечной массы, что является признаком '
                                         '"скрытого ожирения".')

    def click(self):
        self.ok = Programm()
        self.ok.show()
        self.close()


class Programm(QWidget):  # выбор тренировки
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 175)
        self.setWindowTitle('Ваша программа!')
        self.hand = QPushButton('Тренировка рук', self)  # выбор тренировки на соответствующую
        # часть тела
        self.hand.setGeometry(QRect(0, 0, 250, 30))
        self.hand.setStyleSheet("background-color: #899")
        self.foot = QPushButton('Тренировка ног', self)
        self.foot.setGeometry(QRect(0, 30, 250, 35))
        self.foot.setStyleSheet("background-color: #886")
        self.press = QPushButton('Тренировка пресса', self)
        self.press.setGeometry(QRect(0, 65, 250, 35))
        self.press.setStyleSheet("background-color: #899")
        self.body = QPushButton('Тренировка всего тела', self)
        self.body.setGeometry(QRect(0, 95, 250, 35))
        self.body.setStyleSheet("background-color: #886")
        self.bnt = QPushButton('Выход', self)  # выход из приложения
        self.bnt.setGeometry(QRect(130, 135, 100, 30))
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.clicked.connect(self.exit)
        self.hand.clicked.connect(self.Hand)
        self.foot.clicked.connect(self.Foot)
        self.press.clicked.connect(self.Press)
        self.body.clicked.connect(self.Body)

    # при нажатии на тренироку --> переход к соответствующему окну
    def Hand(self):
        self.ok = Tr_Hand()
        self.ok.show()
        self.close()

    def Foot(self):
        self.ok = Tr_Foot()
        self.ok.show()
        self.close()

    def Press(self):
        self.ok = Tr_Press()
        self.ok.show()
        self.close()

    def Body(self):
        self.ok = Tr_Body()
        self.ok.show()
        self.close()

    def exit(self):  # диалоговое окно -- выхо при положительном ответе
        buttonReply = QMessageBox.question(self, 'Точно?', "Вы точно хотите выйти?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()


class Tr_Hand(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 180)
        self.setWindowTitle('Тренировка рук.')
        self.bnt = QPushButton('Назад', self)  # переход к выбору тренировки
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.setGeometry(QRect(170, 130, 100, 30))
        self.bnt.clicked.connect(self.exit)
        self.first = QLabel(self)
        self.first.setGeometry(QRect(75, 20, 150, 30))
        self.first.setText('Попеременный подъем\nгантелей стоя')
        self.kol_1 = QPushButton(self)
        self.kol_1.setGeometry(QRect(260, 25, 100, 30))
        self.kol_1.setText('1 минута')
        self.kol_1.clicked.connect(self.time)
        self.what_1 = QPushButton('?', self)
        self.what_1.setGeometry(QRect(10, 20, 30, 30))
        self.second = QLabel(self)
        self.second.setGeometry(QRect(75, 80, 200, 30))
        self.second.setText('Концентрированное\nсгибание рук сидя')
        self.kol_2 = QLabel(self)
        self.kol_2.setGeometry(QRect(260, 80, 100, 30))
        self.kol_2.setText('20 раз')
        self.what_2 = QPushButton('?', self)
        self.what_1.setStyleSheet("background-color: grey")
        self.what_2.setStyleSheet("background-color: grey")
        self.what_2.setGeometry(QRect(10, 80, 30, 30))
        self.what_1.clicked.connect(self.What_1)
        self.what_2.clicked.connect(self.What_2)

    def What_2(self):  # описание 2 упражнения
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'сидя на скамье, рука перпендикулярно полу, локоть чуть '
                                         'согнут, ладонь развернута к себе. При выдохе сгибаем '
                                         'руку и одновременно разворачиваем так, чтобы в верхней '
                                         'точке ладонь была развернута вверх, при выдохе разгибаем '
                                         'руку.')

    def What_1(self):  # описание первого упражнения
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'стоя, спина прогнута. На выдохе равномерно поднимаем '
                                         'гантель одной руки, на выдохе равномерно опускаем. Затем '
                                         'аналогично - другой рукой.')

    def time(self):  # переход к таймеру
        self.ok = Timer()
        self.ok.show()

    def exit(self):
        buttonReply = QMessageBox.question(self, 'Точно?', "Вы точно хотите закончить "
                                                           "тренировку рук?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.ok = Programm()
            self.ok.show()
            self.close()


class Timer(QWidget):  # таймер, если упражнение на время
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 80, 200, 25)
        self.name = QLabel(self)
        self.name.setGeometry(QRect(120, 40, 250, 200))
        self.name.setFont(QFont("Helvetica", 25, QFont.Bold))
        self.name.setText('60')
        self.timer = QBasicTimer()
        self.timer.start(600, self)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(50, 20, 240, 65))
        self.label.setText("Выполняйте упражнение!")
        self.step = 0
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Таймер')

    def timerEvent(self, e):
        if self.step == 100:
            self.timer.stop()
            self.no()
        self.name.setText(str(60 - round(self.step / 16.4 * 10)))  # обратный отсчет
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def no(self):
        QMessageBox.about(self, "", 'Время вышло!')
        self.close()


class Tr_Foot(QWidget):  # для каждой тренировки похожие функции
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 180)
        self.setWindowTitle('Тренировка ног.')
        self.bnt = QPushButton('Назад', self)
        self.bnt.setGeometry(QRect(170, 130, 100, 30))
        self.bnt.clicked.connect(self.exit)
        self.bnt.setStyleSheet("background-color: grey")
        self.first = QLabel(self)
        self.first.setGeometry(QRect(75, 20, 150, 30))
        self.first.setText('Выпады вперед\nс гантелями')
        self.kol_1 = QPushButton(self)
        self.kol_1.setGeometry(QRect(260, 25, 100, 30))
        self.kol_1.setText('1 минута')
        self.kol_1.clicked.connect(self.time)
        self.what_1 = QPushButton('?', self)
        self.what_1.setGeometry(QRect(10, 20, 30, 30))
        self.second = QLabel(self)
        self.second.setGeometry(QRect(75, 80, 200, 30))
        self.second.setText('Махи ног назад\nстоя в блоке')
        self.kol_2 = QLabel(self)
        self.kol_2.setGeometry(QRect(260, 80, 100, 30))
        self.kol_2.setText('35 раз')
        self.what_2 = QPushButton('?', self)
        self.what_2.setGeometry(QRect(10, 80, 30, 30))
        self.what_1.setStyleSheet("background-color: grey")
        self.what_2.setStyleSheet("background-color: grey")
        self.what_1.clicked.connect(self.What_1)
        self.what_2.clicked.connect(self.What_2)

    def What_2(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'стоя на одной ноге, спина прогнута, корпус немного '
                                         'наклонен вперед, руки зафиксированы на тренажере для '
                                         'устойчивости. На выдохе равномерно отводим руку назад, '
                                         'слегка выпрямляем ее в колене, задерживаем на секунду, '
                                         'на вдохе равномерно приводим ногу в исходное положение')

    def What_1(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'стоя, ноги вместе. При вдохе делаем шаг вперед и приседаем '
                                         'до положения, когда обе ноги в коленях образуют угол 90 '
                                         'градусов. В нижнем положении задняя нога стоит на носке. '
                                         'При выдохе встаем в исходное положение. Далее поочередно '
                                         'меняем ногу.')

    def time(self):
        self.ok = Timer()
        self.ok.show()

    def exit(self):
        buttonReply = QMessageBox.question(self, 'Точно?', "Вы точно хотите закончить "
                                                           "тренировку ног?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.ok = Programm()
            self.ok.show()
            self.close()


class Tr_Press(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 180)
        self.setWindowTitle('Тренировка пресса.')
        self.bnt = QPushButton('Назад', self)
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.setGeometry(QRect(170, 130, 100, 30))
        self.bnt.clicked.connect(self.exit)
        self.first = QLabel(self)
        self.first.setGeometry(QRect(75, 20, 150, 30))
        self.first.setText('Скручивани лежа')
        self.kol_1 = QPushButton(self)
        self.kol_1.setGeometry(QRect(260, 25, 100, 30))
        self.kol_1.setText('1 минута')
        self.kol_1.clicked.connect(self.time)
        self.what_1 = QPushButton('?', self)
        self.what_1.setGeometry(QRect(10, 20, 30, 30))
        self.second = QLabel(self)
        self.second.setGeometry(QRect(75, 80, 200, 30))
        self.second.setText('Скуручивания на\nскамье')
        self.kol_2 = QPushButton(self)
        self.kol_2.setGeometry(QRect(260, 80, 100, 30))
        self.kol_2.setText('1 минута')
        self.kol_2.clicked.connect(self.time)
        self.what_2 = QPushButton('?', self)
        self.what_1.setStyleSheet("background-color: grey")
        self.what_2.setStyleSheet("background-color: grey")
        self.what_2.setGeometry(QRect(10, 80, 30, 30))
        self.what_1.clicked.connect(self.What_1)
        self.what_2.clicked.connect(self.What_2)

    def What_1(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'лежа на спине, колени согнуты, руки прямые, перед '
                                         'собой. На выдохе скручивайте живот, приводя грудь '
                                         'ближе к ногам, поясница не должна отрываться о пола. '
                                         'Задержитесь на секунду, на вдохе равномерно разогнитесь.')

    def What_2(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'сидя/лежа на скамье, руки скрещиваем на груди, на выдохе '
                                         'делаем скучивания и доводим до точки максимального '
                                         'сокращения мышц живота, выдыхая весь воздух. Затем на '
                                         'выдохе - опускаемся.')

    def time(self):
        self.ok = Timer()
        self.ok.show()

    def exit(self):
        buttonReply = QMessageBox.question(self, 'Точно?', "Вы точно хотите закончить тренировку "
                                                           "пресса?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.ok = Programm()
            self.ok.show()
            self.close()


class Tr_Body(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 180)
        self.setWindowTitle('Тренировка всего тела.')
        self.bnt = QPushButton('Назад', self)
        self.bnt.setStyleSheet("background-color: grey")
        self.bnt.setGeometry(QRect(170, 130, 100, 30))
        self.bnt.clicked.connect(self.exit)
        self.first = QLabel(self)
        self.first.setGeometry(QRect(75, 20, 150, 30))
        self.first.setText('Прыгающий Джек')
        self.kol_1 = QLabel(self)
        self.kol_1.setGeometry(QRect(260, 25, 100, 30))
        self.kol_1.setText('50 раз')
        self.what_1 = QPushButton('?', self)
        self.what_1.setGeometry(QRect(10, 20, 30, 30))
        self.second = QLabel(self)
        self.second.setGeometry(QRect(75, 80, 200, 30))
        self.second.setText('Берпи')
        self.kol_2 = QLabel(self)
        self.kol_2.setGeometry(QRect(260, 80, 100, 30))
        self.kol_2.setText('40 раз')
        self.what_2 = QPushButton('?', self)
        self.what_1.setStyleSheet("background-color: grey")
        self.what_2.setStyleSheet("background-color: grey")
        self.what_2.setGeometry(QRect(10, 80, 30, 30))
        self.what_1.clicked.connect(self.What_1)
        self.what_2.clicked.connect(self.What_2)

    def What_1(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'стойте прямо, ноги шире плеч, руки по швам. '
                                         'Сделайте глубокий присед, дотроньтесь до пола кончиками '
                                         'пальцев. Резко выпрямитесь, в прижке сведите ноги вместе '
                                         'и сделайте хлопок над головой.')

    def What_2(self):
        QMessageBox.about(self, "Title", 'Исходное положение: '
                                         'Встаньте прямо, ноги на ширине плеч. Приседайте, пока не '
                                         'сможете поставить ладони на пол. Перенесите вес тела на '
                                         'руки, выполните прыжок ногами назад. Сделайте отжимание, '
                                         'затем в прыжке подтяните ноги к рукам. Выпрямитесь и '
                                         'подпрыгните, сделав хлопок над головой')

    def time(self):
        self.ok = Timer()
        self.ok.show()

    def exit(self):
        buttonReply = QMessageBox.question(self, 'Точно?', "Вы точно хотите закончить тренировку "
                                                           "всего тела?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.ok = Programm()
            self.ok.show()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entry()
    ex.show()
    sys.exit(app.exec_())
