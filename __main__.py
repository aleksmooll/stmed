#!/bin/python

import sys

from PySide2.QtWidgets import QApplication
from core.StMain import StMainWindow

st_app = QApplication(sys.argv)
wm = StMainWindow()
wm.show()
sys.exit(st_app.exec_())