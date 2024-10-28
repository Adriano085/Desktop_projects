from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice

# Main App Object and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(300,200)

# Create all app Objects
txt_title = QLabel('Password Generation')
txt_password = QLabel('?')

btn_generate = QPushButton('Generate')
btn_copy = QPushButton('Copy')
btn_clear = QPushButton('Clear')

# All Design
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(txt_title, alignment=Qt.AlignCenter)
row2.addWidget(txt_password, alignment=Qt.AlignCenter)
row3.addWidget(btn_generate, alignment=Qt.AlignCenter)
row3.addWidget(btn_clear, alignment=Qt.AlignCenter)
row3.addWidget(btn_copy, alignment=Qt.AlignCenter)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Functions
def generate():
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
  password = ''.join(choice(chars) for _ in range(12))
  txt_password.setText(password)
  change_text_btn_copy("Copy")


def clear():
  txt_password.setText('?')
  change_text_btn_copy("Copy")

def copy_text():
  text = txt_password.text()
  if text != "?":
    app.clipboard().setText(text)
    change_text_btn_copy("Copied")

def change_text_btn_copy(text):
  btn_copy.setText(text)


# Events
btn_generate.clicked.connect(generate)
btn_clear.clicked.connect(clear)
btn_copy.clicked.connect(copy_text)

# Show/run our app
main_window.show()
app.exec_()