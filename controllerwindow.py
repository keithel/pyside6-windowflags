# Copyright (C) 2023 Keith Kyzivat
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QRadioButton
from PySide6.QtWidgets import QCheckBox, QGroupBox, QGridLayout
from typing import Optional
from previewwindow import PreviewWindow
from enum import Enum

class ControllerWindow(QWidget):
    def __init__(self, parent = None, pythonic_window_registration: bool = False):
        super().__init__(parent)

        self.pythonic_reg = pythonic_window_registration
        self.previewWindow = PreviewWindow()

        self.createTypeGroupBox()
        self.createHintsGroupBox()

        quitButton = QPushButton("&Quit")
        quitButton.clicked.connect(qApp.quit)

        bottomLayout = QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(quitButton)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.typeGroupBox)
        mainLayout.addWidget(self.hintsGroupBox)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Window Flags")
        self.updatePreview()

        self.typeFlagWidgets: Optional[list[tuple[QRadioButton, Qt.WindowFlags]]] = []
        self.hintFlagWidgets: Optional[list[tuple[QCheckBox, Qt.WindowFlags]]] = []
        self.typeGroupBox = None
        self.hintsGroupBox = None

    @Slot()
    def updatePreview(self) -> None:
        flags = Qt.WindowFlags()
        if self.pythonic_reg:
            for radioButton, flag in self.typeFlagWidgets:
                print(f"updatePreview radioButton {radioButton.text()} {flag}")
                if radioButton.isChecked():
                    print(f"rb {radioButton.text()} is checked. {flag.value}")
                    flags = flag

            for checkBox, flag in self.hintFlagWidgets:
                if checkBox.isChecked():
                    flags = flags | flag
        else:
            if self.windowRadioButton.isChecked():
                print(f"windowRadioButton is checked. {Qt.Window}")
                flags = Qt.Window
            if self.dialogRadioButton.isChecked():
                print(f"dialogRadioButton is checked. {Qt.Dialog}")
                flags = Qt.Dialog
            if self.sheetRadioButton.isChecked():
                print(f"sheetRadioButton is checked. {Qt.Dialog}")
                flags = Qt.Sheet
            if self.drawerRadioButton.isChecked():
                print(f"drawerRadioButton is checked. {Qt.Dialog}")
                flags = Qt.Drawer
            if self.popupRadioButton.isChecked():
                print(f"popupRadioButton is checked. {Qt.Dialog}")
                flags = Qt.Popup
            if self.toolRadioButton.isChecked():
                print(f"toolRadioButton is checked. {Qt.Dialog}")
                flags = Qt.Tool
            if self.toolTipRadioButton.isChecked():
                print(f"toolTipRadioButton is checked. {Qt.Dialog}")
                flags = Qt.ToolTip
            if self.splashScreenRadioButton.isChecked():
                print(f"splashScreenRadioButton is checked. {Qt.Dialog}")
                flags = Qt.SplashScreen

            if self.msWindowsFixedSizeDialogCheckBox.isChecked():
                flags = flags | Qt.MSWindowsFixedSizeDialogHint
            if self.x11BypassWindowManagerCheckBox.isChecked():
                flags = flags | Qt.X11BypassWindowManagerHint
            if self.framelessWindowCheckBox.isChecked():
                flags = flags | Qt.FramelessWindowHint
            if self.windowNoShadowCheckBox.isChecked():
                flags = flags | Qt.NoDropShadowWindowHint
            if self.windowTitleCheckBox.isChecked():
                flags = flags | Qt.WindowTitleHint
            if self.windowSystemMenuCheckBox.isChecked():
                flags = flags | Qt.WindowSystemMenuHint
            if self.windowMinimizeButtonCheckBox.isChecked():
                flags = flags | Qt.WindowMinimizeButtonHint
            if self.windowMaximizeButtonCheckBox.isChecked():
                flags = flags | Qt.WindowMaximizeButtonHint
            if self.windowCloseButtonCheckBox.isChecked():
                flags = flags | Qt.WindowCloseButtonHint
            if self.windowContextHelpButtonCheckBox.isChecked():
                flags = flags | Qt.WindowContextHelpButtonHint
            if self.windowShadeButtonCheckBox.isChecked():
                flags = flags | Qt.WindowShadeButtonHint
            if self.windowStaysOnTopCheckBox.isChecked():
                flags = flags | Qt.WindowStaysOnTopHint
            if self.windowStaysOnBottomCheckBox.isChecked():
                flags = flags | Qt.WindowStaysOnBottomHint
            if self.customizeWindowHintCheckBox.isChecked():
                flags = flags | Qt.CustomizeWindowHint

        self.previewWindow.setAndDisplayWindowFlags(flags)

        pos = self.previewWindow.pos()
        if pos.x() < 0:
            pos.setX(0)
        if pos.y() < 0:
            pos.setY(0)
        self.previewWindow.move(pos)
        self.previewWindow.show()

    def createTypeGroupBox(self) -> None:
        self.typeGroupBox = QGroupBox("Type")
        layout = QGridLayout()

        if self.pythonic_reg:
            typeFlags: list[Qt.WindowFlags] = [
                Qt.Window, Qt.Dialog, Qt.Sheet, Qt.Drawer, Qt.Popup, Qt.Tool,
                Qt.ToolTip, Qt.SplashScreen
            ]
            self.typeFlagWidgets: list[tuple[QRadioButton, Qt.WindowFlags]] = [
                (self.createRadioButton(flag.name), flag) for flag in typeFlags
            ]
            self.typeFlagWidgets[0][0].setChecked(True)

            for i, (radioButton, _) in enumerate(self.typeFlagWidgets):
                layout.addWidget(radioButton, i%3, int(i/3))
        else:
            self.windowRadioButton = self.createRadioButton("Window");
            self.dialogRadioButton = self.createRadioButton("Dialog");
            self.sheetRadioButton = self.createRadioButton("Sheet");
            self.drawerRadioButton = self.createRadioButton("Drawer");
            self.popupRadioButton = self.createRadioButton("Popup");
            self.toolRadioButton = self.createRadioButton("Tool");
            self.toolTipRadioButton = self.createRadioButton("Tooltip");
            self.splashScreenRadioButton = self.createRadioButton("Splash screen")
            self.windowRadioButton.setChecked(True)

            layout.addWidget(self.windowRadioButton, 0, 0)
            layout.addWidget(self.dialogRadioButton, 1, 0)
            layout.addWidget(self.sheetRadioButton, 2, 0)
            layout.addWidget(self.drawerRadioButton, 3, 0)
            layout.addWidget(self.popupRadioButton, 0, 1)
            layout.addWidget(self.toolRadioButton, 1, 1)
            layout.addWidget(self.toolTipRadioButton, 2, 1)
            layout.addWidget(self.splashScreenRadioButton, 3, 1)

        self.typeGroupBox.setLayout(layout)

    def createHintsGroupBox(self) -> None:
        self.hintsGroupBox = QGroupBox("Hints")
        layout = QGridLayout()

        if self.pythonic_reg:
            self.hintFlagWidgets: list[tuple[QCheckBox, Qt.WindowFlags]] = [
                (self.createCheckBox(flag.name), flag) for flag in
                self.previewWindow.hintFlags
            ]

            for i, (checkBox, _) in enumerate(self.hintFlagWidgets):
                layout.addWidget(checkBox, i%6, int(i/6))
        else:
            self.msWindowsFixedSizeDialogCheckBox = self.createCheckBox("MS Windows fixed size dialog")
            self.x11BypassWindowManagerCheckBox = self.createCheckBox("X11 bypass window manager")
            self.framelessWindowCheckBox = self.createCheckBox("Frameless window")
            self.windowNoShadowCheckBox = self.createCheckBox("No drop shadow")
            self.windowTitleCheckBox = self.createCheckBox("Window title")
            self.windowSystemMenuCheckBox = self.createCheckBox("Window system menu")
            self.windowMinimizeButtonCheckBox = self.createCheckBox("Window minimize button")
            self.windowMaximizeButtonCheckBox = self.createCheckBox("Window maximize button")
            self.windowCloseButtonCheckBox = self.createCheckBox("Window close button")
            self.windowContextHelpButtonCheckBox = self.createCheckBox("Window context help button")
            self.windowShadeButtonCheckBox = self.createCheckBox("Window shade button")
            self.windowStaysOnTopCheckBox = self.createCheckBox("Window stays on top")
            self.windowStaysOnBottomCheckBox = self.createCheckBox("Window stays on bottom")
            self.customizeWindowHintCheckBox = self.createCheckBox("Customize window")

            layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
            layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
            layout.addWidget(self.x11BypassWindowManagerCheckBox, 1, 0)
            layout.addWidget(self.framelessWindowCheckBox, 2, 0)
            layout.addWidget(self.windowNoShadowCheckBox, 3, 0)
            layout.addWidget(self.windowTitleCheckBox, 4, 0)
            layout.addWidget(self.windowSystemMenuCheckBox, 5, 0)
            layout.addWidget(self.windowMinimizeButtonCheckBox, 6, 0)
            layout.addWidget(self.windowMaximizeButtonCheckBox, 0, 1)
            layout.addWidget(self.windowCloseButtonCheckBox, 1, 1)
            layout.addWidget(self.windowContextHelpButtonCheckBox, 2, 1)
            layout.addWidget(self.windowShadeButtonCheckBox, 3, 1)
            layout.addWidget(self.windowStaysOnTopCheckBox, 4, 1)
            layout.addWidget(self.windowStaysOnBottomCheckBox, 5, 1)
            layout.addWidget(self.customizeWindowHintCheckBox, 6, 1)
        self.hintsGroupBox.setLayout(layout)

    def createCheckBox(self, text: str) -> QCheckBox:
        checkBox = QCheckBox(text)
        checkBox.clicked.connect(self.updatePreview)
        return checkBox

    def logRadioButtonChecked(self, checked):
        print(f"Radio button {'checked' if checked else 'not checked'}")
    def createRadioButton(self, text: str) -> QRadioButton:
        radioButton = QRadioButton(text)
        radioButton.clicked.connect(self.updatePreview)
        radioButton.clicked.connect(self.logRadioButtonChecked)
        return radioButton

