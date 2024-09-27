# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_sign_in.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(677, 341)
        Frame.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sign_in_screen = QFrame(Frame)
        self.sign_in_screen.setObjectName(u"sign_in_screen")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_in_screen.sizePolicy().hasHeightForWidth())
        self.sign_in_screen.setSizePolicy(sizePolicy)
        self.sign_in_screen.setStyleSheet(u"background-color:rgb(0,0,34)")
        self.sign_in_screen.setFrameShape(QFrame.Shape.StyledPanel)
        self.sign_in_screen.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sign_in_screen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_login = QPushButton(self.sign_in_screen)
        self.button_login.setObjectName(u"button_login")

        self.verticalLayout_2.addWidget(self.button_login, 0, Qt.AlignmentFlag.AlignRight)

        self.label_username = QLabel(self.sign_in_screen)
        self.label_username.setObjectName(u"label_username")

        self.verticalLayout_2.addWidget(self.label_username, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_username = QLineEdit(self.sign_in_screen)
        self.line_username.setObjectName(u"line_username")
        self.line_username.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color:rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";\n"
"")

        self.verticalLayout_2.addWidget(self.line_username, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_password = QLabel(self.sign_in_screen)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout_2.addWidget(self.label_password, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_password = QLineEdit(self.sign_in_screen)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color:rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";\n"
"")

        self.verticalLayout_2.addWidget(self.line_password, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_password_again = QLabel(self.sign_in_screen)
        self.label_password_again.setObjectName(u"label_password_again")

        self.verticalLayout_2.addWidget(self.label_password_again, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_password_again = QLineEdit(self.sign_in_screen)
        self.line_password_again.setObjectName(u"line_password_again")
        self.line_password_again.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color:rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.line_password_again, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_sign_in = QPushButton(self.sign_in_screen)
        self.button_sign_in.setObjectName(u"button_sign_in")
        self.button_sign_in.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.button_sign_in, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.sign_in_screen, 0, Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.button_login.setText(QCoreApplication.translate("Frame", u"or Login", None))
        self.label_username.setText(QCoreApplication.translate("Frame", u"Username:", None))
        self.line_username.setText("")
        self.label_password.setText(QCoreApplication.translate("Frame", u"Password:", None))
        self.label_password_again.setText(QCoreApplication.translate("Frame", u"Password Again:", None))
        self.line_password_again.setText("")
        self.button_sign_in.setText(QCoreApplication.translate("Frame", u"Sign In", None))
    # retranslateUi

