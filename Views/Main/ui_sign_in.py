# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_inxeuqss.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(465, 433)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_topBar = QFrame(self.centralwidget)
        self.frame_topBar.setObjectName(u"frame_topBar")
        self.frame_topBar.setMinimumSize(QSize(0, 60))
        self.frame_topBar.setMaximumSize(QSize(16777215, 60))
        self.frame_topBar.setStyleSheet(u"background-color:rgb(0, 0, 34);")
        self.frame_topBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_topBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_topBar)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_minimize = QPushButton(self.frame_topBar)
        self.button_minimize.setObjectName(u"button_minimize")
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/Icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.button_minimize)

        self.button_maximize = QPushButton(self.frame_topBar)
        self.button_maximize.setObjectName(u"button_maximize")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/Icons/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.button_maximize)

        self.button_close = QPushButton(self.frame_topBar)
        self.button_close.setObjectName(u"button_close")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Assets/Icons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_close.setIcon(icon2)
        self.button_close.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.button_close)

        self.button_close.raise_()
        self.button_maximize.raise_()
        self.button_minimize.raise_()
        self.label.raise_()

        self.verticalLayout.addWidget(self.frame_topBar)

        self.frame_base = QFrame(self.centralwidget)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_base)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_base)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(0,0,0);\n"
"background-position:center;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.sign_in_page = QWidget()
        self.sign_in_page.setObjectName(u"sign_in_page")
        self.sign_in_page.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.gridLayout = QGridLayout(self.sign_in_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget.addWidget(self.sign_in_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:rgb(0,0,0)")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_base)

        self.frame_bottomBar = QFrame(self.centralwidget)
        self.frame_bottomBar.setObjectName(u"frame_bottomBar")
        self.frame_bottomBar.setMinimumSize(QSize(0, 60))
        self.frame_bottomBar.setMaximumSize(QSize(16777215, 60))
        self.frame_bottomBar.setStyleSheet(u"background-color:rgb(0, 0, 34);")
        self.frame_bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_bottomBar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_time = QLabel(self.frame_bottomBar)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(416, 42))
        self.label_time.setMaximumSize(QSize(416, 16777215))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_time.setFont(font1)
        self.label_time.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_4.addWidget(self.label_time, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_2 = QLabel(self.frame_bottomBar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setPixmap(QPixmap(u":/Images/Assets/Icons/copyright.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_bottomBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"    CINETIME    ", None))
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_close.setText("")
        self.label_time.setText("")
        self.label_2.setText("")
    # retranslateUi

