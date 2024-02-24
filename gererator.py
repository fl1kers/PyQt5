from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle("CS2 Injector")
win.resize(500,300)

text = QLabel("Click on Button to Inject!")
winner = QLabel("?")
button = QPushButton("inject!")
ruls = QLabel("YT channel: https://www.youtube.com/watch?reload=9&v=dQw4w9WgXcQ")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(ruls, alignment=Qt.AlignCenter)
win.setLayout(line)

def show_winner():
    text.setText("Your Compter will exploit for:")
    winner.setText(str(randint(1,100)))

button.clicked.connect(show_winner)

win.show()
app.exec_()