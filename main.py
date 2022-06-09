import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import imageio.v2 as imageio


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Loading ui file
        uic.loadUi("untitled.ui", self)
        # Setting Widgets from untitled.ui file
        self.label = self.findChild(QtWidgets.QLabel, "label")
        self.browse_button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.export_button = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        # Assigning action to browse_button which will activate after clicking button
        self.browse_button.clicked.connect(self.browseFiles)
        # Assigning action to export_button which will activate after clicking button
        self.export_button.clicked.connect(self.export)
        # Creating Object Of GIF Class
        self.converting_handler = GIF()
        # Creating empty variables for later
        self.files = None
        self.movie = None
        # Show The App
        self.show()

    def browseFiles(self):
        # Creating dialog window which allows us to select files that will turn into our gif
        fnames = QtWidgets.QFileDialog.getOpenFileNames(self, "Open file", r"C:\Users\Jakub\Dokumenty")
        # Selecting first item (list) from fnames and assigning it to self.files
        self.files = fnames[0]

    def export(self):
        # Using GIF class object and its method convert to create GIF
        self.converting_handler.convert(self.files)
        # Starting play_gif method of UI class
        self.play_gif()

    def play_gif(self):
        # Creating Object QMovie and passing our created GIF into it
        self.movie = QtGui.QMovie('gif.gif')
        # Setting max size of self.movie
        self.movie.setScaledSize(QtCore.QSize().scaled(386, 300, Qt.KeepAspectRatio))
        self.label.setMovie(self.movie)
        self.movie.scaledSize()
        # Starting our GIF in application
        self.movie.start()


class GIF:
    def __init__(self):
        # Creating empty list images in which we will store our images for converting
        self.images = []

    # Creating convert method which takes files as an argument
    def convert(self, files):
        # Iterating through files
        for file in files:
            # Appending self.images with imageio objects
            self.images.append(imageio.imread(file))
        # Creating GIF through imageio module
        imageio.mimsave("gif.gif", self.images, duration=0.5)
        # Clearing self.images
        self.images.clear()


if __name__ == "__main__":
    # Creating QApplication object with sys.argv argument passed into it
    app = QApplication(sys.argv)
    # Creating object of UI Class which will be our application window
    UIWindow = UI()
    # Executing our application
    app.exec_()
