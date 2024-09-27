from Importer.QtImporter import *
from Models.Database.database import Database


class ThreadLoginModel(QThread):
    login_result = Signal(bool)

    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        login_result = True
        self.login_result.emit(login_result)    


class ThreadModel(QThread):
    result = Signal(str) 

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        self.db = Database() 
        result = self.db.add_user(self.username, self.password)
        self.result.emit(result) 
        self.db.close() 

class UserModel:
    def __init__(self, parent_widget=None):  
        self.db = Database()
        self.parent_widget = parent_widget  

    def validate_password(self, username, password, password_again):
        validation = self.validate_reg(username, password, password_again)

        if validation is not True:
            QMessageBox.warning(self.parent_widget, "Warning", validation)
            return

        else:
            self.thread = ThreadModel(username, password)
            self.thread.result.connect(self.handle_result) 
            self.thread.start()

    def validate_reg(self, username, password, password_again):
        
        if not username or not password or not password_again:
            return "Username, password, or password again cannot be empty!"
        if password != password_again:
            return "Passwords do not match!"
        if len(password) < 6:
            return "The password must be at least 6 characters!"
        if self.get_user(username) is not None:  
            return "Username already exists!"
        return True

    def handle_result(self, result):
        QMessageBox.information(self.parent_widget, "Accepted", result)

    def get_user(self, username):
        return self.db.get_username(username)
    
    def validation_login(self, username, password):
        result = self.db.get_username_password(username)
        if not result[1] == username or not result[2] == password:
            return QMessageBox.warning(self.parent_widget, "Warning", "Username and password do not matched") 
        else:
            self.thread=ThreadLoginModel(username, password)
            self.thread.login_result.connect(self.handle_login_result)
            self.thread.start()
            
    
    def handle_login_result(self, login_result):
        QMessageBox.information(self.parent_widget, "Accepted", str(login_result))
    
    