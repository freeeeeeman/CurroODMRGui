import sys

from PyQt5.QtWidgets import QToolButton, QLabel,  QLineEdit, QComboBox, QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

class MainGui(QMainWindow):
    """This is the main window."""
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        super(MainGui, self).__init__()
        self.font = QFont('Sans Serif', 12)
        app.setFont(self.font)
        self.title = 'ODMR Control'
        self.left = 200
        self.top = 50
        self.width = 300
        self.height = 300
        self.initUI()
        sys.exit(app.exec_())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        buttons = PulseInputButtons()
        self.setCentralWidget(buttons)

        self.show()

class PulseInputButtons(QWidget):
    def __init__(self):
        super(PulseInputButtons, self).__init__()

        self.initpulsebuttons()

    def initpulsebuttons(self):
        grid = QGridLayout()
        MW = self.MWbuttons()
        Laser = self.Laserbuttons()
        DAQ = self.DAQbuttons()
        Save = self.SaveLoadButtons()

        grid.addWidget(MW,0,0)
        grid.addWidget(Laser, 1,0)
        grid.addWidget(DAQ, 2,0)
        grid.addWidget(Save, 2, 1, 4, 1)
        self.setLayout(grid)

    def MWbuttons(self):
        MWgroupbox = QGroupBox()
        MWlayout = QGridLayout()
        MWgroupbox.setTitle('MW')
        MWgroupbox.setLayout(MWlayout)

        MWPWlabel = QLabel('PW')
        MWPWbutton = QLineEdit()

        Triggerlabel = QLabel('Trigger Mode')
        Triggermode = QComboBox()
        Triggermode.addItem('Setting a')
        Triggermode.addItem('Setting b')
        Triggermode.addItem('Setting c')
        Triggermode.activated[str].connect(lambda x: self.setmode(x))

        Samplinglabel = QLabel('Sampling Mode')
        Samplingmode = QComboBox()
        Samplingmode.addItem('Setting a')
        Samplingmode.addItem('Setting b')
        Samplingmode.addItem('Setting c')
        Samplingmode.activated[str].connect(lambda x: self.setmode(x))

        Routelabel = QLabel('Sampling Route')
        Samplingroute = QLineEdit()

        MWlayout.addWidget(MWPWlabel,0,0)
        MWlayout.addWidget(MWPWbutton,0,1)

        MWlayout.addWidget(Triggerlabel,1,0)
        MWlayout.addWidget(Triggermode,1,1)

        MWlayout.addWidget(Samplinglabel,2,0)
        MWlayout.addWidget(Samplingmode,2,1)

        MWlayout.addWidget(Routelabel,3,0)
        MWlayout.addWidget(Samplingroute,3,1)

        return MWgroupbox

    def Laserbuttons(self):
        Laserbox = QGroupBox()
        Laserlayout = QGridLayout()
        Laserbox.setTitle('Laser')
        Laserbox.setLayout(Laserlayout)

        Laserlabel = QLabel('Laser')
        Laserbutton = QLineEdit()

        Laserlayout.addWidget(Laserlabel, 0,0)
        Laserlayout.addWidget(Laserbutton,0,1)
        return Laserbox

    def DAQbuttons(self):
        DAQbox = QGroupBox()
        DAQlayout = QGridLayout()
        DAQbox.setTitle('DAQ')
        DAQbox.setLayout(DAQlayout)

        Samplelabel = QLabel('N Sample')
        Samplebutton = QLineEdit()

        Timeoutlabel = QLabel('Timeout')
        Timeoutbutton = QLineEdit()

        DAQlayout.addWidget(Samplelabel,0,0)
        DAQlayout.addWidget(Samplebutton,0,1)
        DAQlayout.addWidget(Timeoutlabel,1,0)
        DAQlayout.addWidget(Timeoutbutton,1,1)

        return DAQbox

    def SaveLoadButtons(self):
        SaveLoadbox = QGroupBox()
        SaveLoadlayout = QHBoxLayout()
        SaveLoadbox.setLayout(SaveLoadlayout)

        Savebutton = QPushButton('Save')
        Loadbutton = QPushButton('Load')

        SaveLoadlayout.addWidget(Savebutton)
        SaveLoadlayout.addWidget(Loadbutton)
        return SaveLoadbox

    def setmode(self, text):
        if text == 'a':
            self.colormap = self.heat
        if text == 'b':
            self.colormap = self.gray
        if text == 'c':
            self.colormap = self.rainbow
MainGui()

#TODO: add functionality to all buttons
#TODO: make sure we have the layout correct (ask Zeppelin what buttons are missing or are formatted wrong, etc.)
#TODO: figure out the layout for the central pulse sequence design (table of drop downs? how many columns/rows, etc.)