from PyQt5.QtGui import QPixmap


class Editor:
  def __init__(self, label):
    self.label = label
    self.image = None
  
  def load_image(self, image_path):
    self.image = QPixmap(image_path)
    self.update_display()

  def update_display(self):
    if self.image:
      self.label.setPixmap(self.image)
  
  def filter_type(self, filter):
    if self.image:
      self.image = self.image.convertToFormat(filter)
      self.update_display()