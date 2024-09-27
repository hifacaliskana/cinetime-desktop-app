from Importer.QtImporter import *
from Views.Dashboard.Login.dashboard_login import Ui_Frame
from Models.User.user_model import UserModel

class DashboardLoginPage(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.user = UserModel()
        self.ui.button_sign_in.clicked.connect(self.login)

    def login(self):
        username = self.ui.line_username.text()
        password = self.ui.line_password.text()
        self.user.validation_login(username, password)

# View-Model class