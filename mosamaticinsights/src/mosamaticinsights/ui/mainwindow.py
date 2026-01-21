import mosamaticinsights.ui.resources.mosamaticinsights_rc
from PySide6.QtCore import Qt, QByteArray
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QIcon,
)
from mosamaticinsights.ui.settings import Settings
from mosamaticinsights.ui.centraldockwidget import CentralDockWidget
from mosamaticinsights.ui.logdockwidget import LogDockWidget
from mosamaticinsights.ui.pages.page import Page


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = None
        self._central_dockwidget = None
        self._log_dockwidget = None
        self.init()

    def init(self):
        self.setWindowTitle('Mosamatic Insights 1.0')
        self.setWindowIcon(QIcon(self.settings().get('mainwindow/icon_path')))
        self.load_geometry_and_state()
        self.addDockWidget(
            Qt.DockWidgetArea.TopDockWidgetArea, self.central_dockwidget())
        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea, self.log_dockwidget())
        self.init_menus()
        self.init_pages_and_menus()
        
    def init_menus(self):
        self.init_app_menu()

    def init_pages_and_menus(self):
        page = Page(name='My Page', menu_path='Pages/My Page')
        page_manager = self.central_dockwidget().page_manager()
        page_manager.add_page(page)
        page_manager.switch_to(page.name())
        page_menu_action = QAction(page.menu_path().split('/')[1], self)
        page_menu = self.menuBar().addMenu(page.menu_path().split('/')[0])
        page_menu.addAction(page_menu_action)

    def init_app_menu(self):
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        app_menu = self.menuBar().addMenu('Application')
        app_menu.addAction(exit_action)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings('nl.rbeesoft', 'mosamaticinsights')
            self._settings.set('mainwindow/icon_path', ':/icons/mosamaticinsights')
        return self._settings
    
    def central_dockwidget(self):
        if not self._central_dockwidget:
            self._central_dockwidget = CentralDockWidget(self)
        return self._central_dockwidget
    
    def log_dockwidget(self):
        if not self._log_dockwidget:
            self._log_dockwidget = LogDockWidget(self)
        return self._log_dockwidget
    
    # EVENT HANDLERS

    def closeEvent(self, event):
        self.save_geometry_and_state()
    
    # HELPERS

    def load_geometry_and_state(self):
        geometry = self.settings().get('mainwindow/geometry')
        state = self.settings().get('mainwindow/state')
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        self.resize(1024, 1024)
        self.center_window()        
        return False

    def save_geometry_and_state(self):
        self.settings().set('mainwindow/geometry', self.saveGeometry())
        self.settings().set('mainwindow/state', self.saveState())

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

# class MainWindow(QMainWindow):
#     def __init__(self) -> None:
#         super(MainWindow, self).__init__()
#         self._settings = self.init_settings()

#         self.init_menus()

#         layout = QVBoxLayout()
#         central_widget = QWidget()
#         central_widget.setLayout(layout)

#         self.setCentralWidget(central_widget)
#         self.setWindowTitle('Mosamatic Insights')
#         self.setWindowIcon(QIcon(self._settings.get('mainwindow/icon_path')))
#         self._current_process = None

#     def init_settings(self):
#         settings = Settings('nl.rbeesoft', 'mosamaticinsights')
#         settings.set('mainwindow/width', 1024)
#         settings.set('mainwindow/height', 786)
#         settings.set('mainwindow/icon_path', ':/icons/mosamaticinsights')
#         return settings
    
#     def init_menus(self):

#         # Application menu
#         app_menu_action = QAction('Exit', self)
#         app_menu_action.triggered.connect(self.close)
#         app_menu = self.menuBar().addMenu('Application')
#         app_menu.addAction(app_menu_action)
        
#         # Data menu
#         data_menu_open_action = QAction('Open DICOM Folder', self)
#         data_menu_open_action.triggered.connect(self.open_dicom_folder)
#         data_menu = self.menuBar().addMenu('Data')
#         data_menu.addAction(data_menu_open_action)

#         # Render menu
#         render_menu_example_action = QAction('Show example', self)
#         render_menu_example_action.triggered.connect(self.show_example)
#         render_menu = self.menuBar().addMenu('Render')
#         render_menu.addAction(render_menu_example_action)

#     def init_render_canvas(self):
#         render_canvas = RenderCanvas(self, 6, 4, 100)
#         return render_canvas
    
#     def init_window_layout(self):
#         layout = QVBoxLayout()
#         layout.addWidget(self._render_canvas)
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#     def open_dicom_folder(self):
#         self._current_process = DicomAnalyzerProcess()
#         self._current_process.progress.connect(lambda progress: print(f'progress: {progress}'))
#         self._current_process.finished.connect(self.handle_process_finished)
#         self._current_process.failed.connect(self.handle_process_failed)
#         self._current_process.start()

#     def show_example(self):
#         pass

#     def handle_process_finished(self):
#         QMessageBox.information(self, 'Info', 'Process finished')

#     def handle_process_failed(self):
#         QMessageBox.warning(self, 'Error', 'Process failed')