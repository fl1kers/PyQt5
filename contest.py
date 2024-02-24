from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox , QLabel,QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()
win.setWindowTitle("Конкурс")
win.resize(600,300)

question = QLabel("В якому році Гітлер застрелився?")
op1 = QRadioButton("20 червня 1943")
op2 = QRadioButton("16 лютого 1941")
op3 = QRadioButton("9 травня 1945")
op4 = QRadioButton("30 квітня 1945")

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment= Qt.AlignCenter)

layout_H1 = QHBoxLayout()
layout_H1.addWidget(op1, alignment= Qt.AlignCenter)
layout_H1.addWidget(op2, alignment= Qt.AlignCenter)

layout_H2 = QHBoxLayout()
layout_H2.addWidget(op3, alignment= Qt.AlignCenter)
layout_H2.addWidget(op4, alignment= Qt.AlignCenter)

layout_main.addLayout(layout_H1)
layout_main.addLayout(layout_H2)
win.setLayout(layout_main)

def show_win():
    win_win = QMessageBox()
    win_win.setText("Правильно!\nВи виграв Німецьку Імперію!")
    win_win.exec_()
def show_lose():
    lose_win = QMessageBox()
    lose_win.setText("Близько, 30 квітня 1945!\nТому Ви виграв Німецький Бомбардувальник Stuka B-1/Ju-87!")
    lose_win.exec_()
def show_none():
    lose_win = QMessageBox()
    lose_win.setText("Нічого!")
    lose_win.exec_()   
op1.clicked.connect(show_none)
op2.clicked.connect(show_none)
op3.clicked.connect(show_lose)
op4.clicked.connect(show_win)
win.show()
app.exec_()