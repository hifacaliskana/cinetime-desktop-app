from Importer.QtImporter import *
from Views.Dashboard.After_Login.after_login import Ui_Frame

class DashboardAfterLoginPage(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        