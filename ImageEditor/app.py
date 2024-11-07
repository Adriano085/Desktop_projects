from PyQt5.QtWidgets import QApplication, QWidget
from image_editor import ImageEditor

class Application(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Image Editor")
    self.resize(900, 700)

    self.image_editor = ImageEditor()
    self.setLayout(self.image_editor.master_layout)

if __name__ == "__main__":
  app = QApplication([])
  window = Application()
  window.show()
  app.exec_()