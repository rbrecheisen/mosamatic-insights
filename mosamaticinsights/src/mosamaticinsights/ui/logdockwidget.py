from PySide6.QtWidgets import (
    QWidget,
    QDockWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)

from mosamaticinsights.core.logmanagerlistener import LogManagerListener


class LogDockWidget(QDockWidget, LogManagerListener):
    def __init__(self, parent=None):
        super(LogDockWidget, self).__init__(parent)
        self._title_label = None
        self._text_edit = None
        self.init()

    def init(self):
        clear_logs_button = QPushButton('Clear log')
        clear_logs_button.clicked.connect(self.handle_clear_logs_button)
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit())
        layout.addWidget(clear_logs_button)
        container = QWidget()
        container.setLayout(layout)
        self.setObjectName('logdockwidget')
        self.setWindowTitle(self.title_label().text())
        self.setWidget(container)

    # GETTERS

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel('Log output')
        return self._title_label

    def text_edit(self):
        if not self._text_edit:
            self._text_edit = QTextEdit()
        return self._text_edit
    
    # HELPERS

    def add_line(self, line):
        self.text_edit().insertPlainText(line + '\n')
        self.move_to_end()

    def move_to_end(self):
        cursor = self.text_edit().textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.text_edit().setTextCursor(cursor)
        self.text_edit().ensureCursorVisible()

    # EVENT HANDLERS

    def handle_clear_logs_button(self):
        self.text_edit().clear()

    # LogManagerListener
    def new_message(self, message):
        self.add_line(message)