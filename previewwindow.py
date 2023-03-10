# Copyright (C) 2023 Keith Kyzivat
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class PreviewWindow(QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.closeButton = QPushButton("&Close")
        self.closeButton.clicked.connect(self.close) # type: ignore[attr-defined]

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

        self.hintFlags: list[Qt.WindowType] = [
            Qt.WindowType.MSWindowsFixedSizeDialogHint,
            Qt.WindowType.X11BypassWindowManagerHint,
            Qt.WindowType.FramelessWindowHint,
            Qt.WindowType.NoDropShadowWindowHint,
            Qt.WindowType.WindowTitleHint,
            Qt.WindowType.WindowSystemMenuHint,
            Qt.WindowType.WindowMinimizeButtonHint,
            Qt.WindowType.WindowMaximizeButtonHint,
            Qt.WindowType.WindowCloseButtonHint,
            Qt.WindowType.WindowContextHelpButtonHint,
            Qt.WindowType.WindowShadeButtonHint,
            Qt.WindowType.WindowStaysOnTopHint,
            Qt.WindowType.WindowStaysOnBottomHint,
            Qt.WindowType.CustomizeWindowHint
        ]

    def setAndDisplayWindowFlags(self, flags: Qt.WindowType) -> None:
        print(f"setAndDisplayWindowFlags flags: {flags}")
        self.setWindowFlags(flags)

        windowType = flags & Qt.WindowType.WindowType_Mask
        text = windowType.name

        for hintFlag in self.hintFlags:
            if flags & hintFlag:
                text += f"\n| Qt.{hintFlag.name}"

        self.textEdit.setPlainText(text)
