import sys

from PyQt5.QtCore import (Qt, QSettings, QCoreApplication)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMdiArea)

def readSetting(orgName, appName, keyName, value):

    set = QSettings()

class QSTMainWindow(QMainWindow):
    def __init__(self):
        super(QSTMainWindow, self).__init__()

        set = QSettings("file.ini", QSettings.IniFormat )
        set.setValue("main/key", "value")
        set.sync()

        
        self.initUI()
        self.createAction()
        self.createMenus()
        self.createToolBars()

    def initUI(self):
        pass

    def createAction(self):
        pass

    def createMenus(self):
        pass

    def createToolBars(self):
        pass


if __name__ == "__main__":

    QCoreApplication.setOrganizationName("Org Name")
    QCoreApplication.setOrganizationDomain("Org Domain")
    QCoreApplication.setApplicationName("App Name")

    app = QApplication(sys.argv)
    mw = QSTMainWindow()
    mw.show()

    sys.exit(app.exec())
