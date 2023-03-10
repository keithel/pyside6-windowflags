# Copyright (C) 2023 Keith Kyzivat
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class PreviewWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.closeButton = QPushButton("&Close")
        self.closeButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

        self.hintFlags: list[Qt.WindowFlags] = [
            Qt.MSWindowsFixedSizeDialogHint,
            Qt.X11BypassWindowManagerHint,
            Qt.FramelessWindowHint,
            Qt.NoDropShadowWindowHint,
            Qt.WindowTitleHint,
            Qt.WindowSystemMenuHint,
            Qt.WindowMinimizeButtonHint,
            Qt.WindowMaximizeButtonHint,
            Qt.WindowCloseButtonHint,
            Qt.WindowContextHelpButtonHint,
            Qt.WindowShadeButtonHint,
            Qt.WindowStaysOnTopHint,
            Qt.WindowStaysOnBottomHint,
            Qt.CustomizeWindowHint
        ]

    def setAndDisplayWindowFlags(self, flags: Qt.WindowFlags) -> None:
        print(f"setAndDisplayWindowFlags flags: {flags}")
        self.setWindowFlags(flags)

        windowType = flags & Qt.WindowType_Mask
        text = windowType.name

        for hintFlag in self.hintFlags:
            if flags & hintFlag:
                text += f"\n| Qt.{hintFlag.name}"

        self.textEdit.setPlainText(text)
