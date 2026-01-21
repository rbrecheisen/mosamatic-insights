from PySide6.QtWidgets import (
    QLabel,
    QDockWidget,
    QStackedWidget,
)
from mosamaticinsights.ui.pages.pagemanager import PageManager


class CentralDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super(CentralDockWidget, self).__init__(parent)
        self._title_label = None
        self._page_manager = None
        self.init()

    def init(self):
        self.setObjectName('centraldockwidget')
        self.setWindowTitle(self.title_label().text())
        self.setWidget(self.page_manager())

    # GETTERS

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel('')
            self._title_label.setStyleSheet('color: black; font-weight: bold; font-size: 14pt;')
        return self._title_label

    def page_manager(self):
        if not self._page_manager:
            self._page_manager = PageManager(self)
        return self._page_manager