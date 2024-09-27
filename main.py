import sys
from Importer.QtImporter import*
from PySide6.QtWidgets import QApplication, QMainWindow
from Views.Main.ui_sign_in import Ui_MainWindow
from Views.Dashboard.sign_in_Functions import DashboardSignInPage 
from Views.Dashboard.login_Functions import DashboardLoginPage
from Views.Dashboard.after_login_Functions import DashboardAfterLoginPage

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint) # minimize, maximize, close devre dışı bırakıldı
        self.initial_ui()

        self.screenMin = 0

        self.ui.button_minimize.clicked.connect(self.set_minimize)
        self.ui.button_maximize.clicked.connect(self.set_maximize)
        self.ui.button_close.clicked.connect(self.set_close)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_something) 
        self.timer.start(1000) 


    def show_login_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.dashboard_login_page) 

    def show_after_login_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.dashboard_after_login_page) 
    
    def initial_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dashboard_page = DashboardSignInPage()
        self.dashboard_login_page = DashboardLoginPage()  
        self.dashboard_after_login_page = DashboardAfterLoginPage()

        self.ui.stackedWidget.addWidget(self.dashboard_page)
        self.ui.stackedWidget.addWidget(self.dashboard_login_page)  
        self.ui.stackedWidget.addWidget(self.dashboard_after_login_page)
        self.ui.stackedWidget.setCurrentWidget(self.dashboard_page)

        self.dashboard_page.ui.button_login.clicked.connect(self.show_login_page) 
        self.dashboard_login_page.ui.button_sign_in.clicked.connect(self.show_after_login_page) 

    def set_minimize(self):
        self.showMinimized()

    def set_maximize(self):
        if self.screenMin == 0:
            self.showMaximized()
            self.screenMin = 1
        else:
            self.showNormal()
            self.screenMin = 0
        

    def set_close(self):
        self.close()


    def update_something(self):
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.ui.label_time.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())