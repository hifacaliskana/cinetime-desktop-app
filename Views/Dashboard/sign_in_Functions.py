from Importer.QtImporter import*
from Views.Dashboard.Sign_In.dashboard_sign_in import Ui_Frame
from Models.User.user_model import UserModel

class DashboardSignInPage(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)  
        self.user = UserModel()
        self.ui.button_sign_in.clicked.connect(self.register)
       
    def register(self):
        username = self.ui.line_username.text()
        password = self.ui.line_password.text()
        password_again = self.ui.line_password_again.text()

        self.user.validate_password(username, password, password_again) 


# View-Model class       

  
