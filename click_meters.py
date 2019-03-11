"""
    This is a silly little game that I came up with when I was bored.
    I worked at Honeywell, I worked on writing test scripts for power
    meters so I thought it would be funny to make a simple clicker
    game for all of the other interns to use to pass the time while
    waiting for the test scripts to finish.
"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize
from random import randint
import sys

class ClickMeters(QMainWindow):
    """
        This class builds the GUI for the game
    """

	def __init__(self):
    """
        function:
            __init__ - Constructor that builds the GUI

        args:
            None

        returns:
            None

        raises:
            None
    """

        # Call init on the parent class and build the GUI
		QMainWindow.__init__(self)
		self.initUI()

	def initUI(self):
    """
        function:
            initUI - Builds the GUI

        args:
            None

        returns:
            None

        rasies:
            None
    """

        # Set the GUI to be 500x500px and keep the user from
        # resizing it. Also set the title and load the icon
		self.setFixedSize(500,500)
		self.setWindowTitle("Click the Meter!")
		self.setWindowIcon(QIcon('meter.jpg'))

        # Set the tiled meter image on the background of the
        # window
		self.image = QImage('meter.jpg')
		self.image = self.image.scaled(QSize(100,100))
		self.palette = QPalette()
		self.palette.setBrush(10, QBrush(self.image))

        # Declare a click button and put it in a random location.
        # Also bind the button click to the moveBtn function
		self.clickBtn = QPushButton('Click me!',self)
		self.clickBtn.resize(self.clickBtn.sizeHint())
		self.clickBtn.clicked.connect(self.moveBtn)
		self.clickBtn.move((randint(0,4)*100)+10,(randint(0,4)*100)+40)

        # Set the meter image and show the GUI
		self.setPalette(self.palette)
		self.show()

	def moveBtn(self):
        """
            function:
                moveBtn - this function just moves the button onto another
                          random location

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Move the button to a random location
		self.clickBtn.move((randint(0,4)*100)+10,(randint(0,4)*100)+40)

# Only do this if the file is run on its own
if __name__ == '__main__':

    # Declare a QApplication object and pass in the arg vector
	app = QApplication(sys.argv)

    # Create the GUI object and start the GUI main loop
	game = ClickMeters()
	sys.exit(app.exec_())

