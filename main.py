# Copyright (C) 2023 Keith Kyzivat
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the widgets/widgets/windowflags example from Qt 5.x"""

import sys
import argparse
from PySide6.QtWidgets import QApplication
from controllerwindow import ControllerWindow

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pythonic", action='store_true',
        help="Create and register widgets pythonically.")
    args = parser.parse_args()
    app = QApplication(sys.argv)
    controller = ControllerWindow(None, args.pythonic)
    controller.show()
    sys.exit(app.exec())
