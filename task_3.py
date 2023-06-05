# Винтовая Дария 44-22-122 задание 3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import math

def main(*args):
    try:
        x = float(args[0])
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x) ** 2)
        else:
            return math.exp(x ** 3 * (math.sin(3*x)))
    except:
        return "Произошла ошибка"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task 3")

        vbox = QVBoxLayout(self)
        self.lbl = QLabel()
        self.lbl.resize(100, 100)
        vbox.addWidget(self.lbl)

        img = QPixmap("formula.jpg")
        self.lbl.setPixmap(img)

        self.lineEdit = QLineEdit()
        self.btn = QPushButton("Получить y")
        self.lbl2 = QLabel()

        fbox = QFormLayout()
        fbox.addRow("Введите x: ", self.lineEdit)
        fbox.addRow(self.btn)
        fbox.addRow("Ответ: ", self.lbl2)
        vbox.addLayout(fbox)

        self.btn.clicked.connect(self.calculate)

    def calculate(self):
        res = main(float(self.lineEdit.text()))
        self.lbl2.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
