from PySide6.QtWidgets import QStackedWidget
from mosamaticinsights.ui.exceptions import PageNotFoundException


class PageManager(QStackedWidget):
    def __init__(self, parent=None):
        super(PageManager, self).__init__(parent)
        self._pages = None

    # GETTERS

    def pages(self):
        if not self._pages:
            self._pages = {}
        return self._pages
    
    def page(self, name):
        if name in self.pages().keys():
            return self.pages()[name]
        return None
    
    # HELPERS

    def add_page(self, page):
        if page.name() not in self.pages().keys():
            self.pages()[page.name()] = page
            self.addWidget(page)

    def switch_to(self, name):
        page = self.page(name)
        if page:
            self.setCurrentWidget(page)
        else:
            raise PageNotFoundException(name)

    def current_page(self):
        return self.currentWidget()