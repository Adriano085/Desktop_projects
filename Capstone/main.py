from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QDateEdit,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout
)

class ExpenseApp(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(550,500)
    self.setWindowTitle("Expense Tracker 2.0")

    self.date_box = QDateEdit()
    self.dropdown = QComboBox()
    self.description = QLineEdit()
    self.amount = QLineEdit()

    self.add_btn = QPushButton("Add Expense")
    self.delete_btn = QPushButton("Delete")

    self.table = QTableWidget()
    self.table.setColumnCount(5)
    self.table.setHorizontalHeaderLabels(['Id', 'Date', 'Category', 'Amount', 'Description'])

    self.master_layout = QVBoxLayout()
    self.row1 = QHBoxLayout()
    self.row2 = QHBoxLayout()
    self.row3 = QHBoxLayout()

    self.row1.addWidget(QLabel("Date:"))
    self.row1.addWidget(self.date_box)
    self.row1.addWidget(QLabel("Category:"))
    self.row1.addWidget(self.dropdown)

    self.row2.addWidget(QLabel("Amount:"))
    self.row2.addWidget(self.amount)
    self.row2.addWidget(QLabel("Description:"))
    self.row2.addWidget(self.description)

    self.row3.addWidget(self.add_btn)
    self.row3.addWidget(self.delete_btn)

    self.master_layout.addLayout(self.row1)
    self.master_layout.addLayout(self.row2)
    self.master_layout.addLayout(self.row3)

    self.master_layout.addWidget(self.table)

    self.setLayout(self.master_layout)


if __name__ == "__main__":
  app = QApplication([])
  window = ExpenseApp()
  window.show()
  app.exec_()