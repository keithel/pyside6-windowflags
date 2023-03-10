# Copyright (C) 2023 Keith Kyzivat
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the widgets/widgets/windowflags example from Qt 5.x"""

import sys
from PySide6.QtWidgets import QApplication
from controllerwindow import ControllerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = ControllerWindow()
    controller.show()
    sys.exit(app.exec())
