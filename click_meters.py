from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize
from random import randint
import sys

class ClickMeters(QMainWindow):

	def __init__(self):

		QMainWindow.__init__(self)
		self.initUI()

	def initUI(self):

		self.setFixedSize(500,500)
		self.setWindowTitle("Click the Meter!")
		self.setWindowIcon(QIcon('meter.jpg'))

		self.image = QImage('meter.jpg')
		self.image = self.image.scaled(QSize(100,100))
		self.palette = QPalette()
		self.palette.setBrush(10, QBrush(self.image))

		self.clickBtn = QPushButton('Click me!',self)
		self.clickBtn.resize(self.clickBtn.sizeHint())
		self.clickBtn.clicked.connect(self.moveBtn)
		self.clickBtn.move((randint(0,4)*100)+10,(randint(0,4)*100)+40)

		self.setPalette(self.palette)
		self.show()

	def moveBtn(self):

		self.clickBtn.move((randint(0,4)*100)+10,(randint(0,4)*100)+40)

if __name__ == '__main__':

	app = QApplication(sys.argv)
	game = ClickMeters()
	sys.exit(app.exec_())
