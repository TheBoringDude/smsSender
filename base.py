# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '[design]smsSender.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 490)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"app.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(19, 23, 32);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tbPhoneNumber = QLineEdit(self.centralwidget)
        self.tbPhoneNumber.setObjectName(u"tbPhoneNumber")
        self.tbPhoneNumber.setGeometry(QRect(60, 90, 311, 41))
        self.tbPhoneNumber.setFont(font)
        self.tbMessage = QTextEdit(self.centralwidget)
        self.tbMessage.setObjectName(u"tbMessage")
        self.tbMessage.setGeometry(QRect(60, 160, 311, 241))
        self.tbMessage.setFont(font)
        self.btnSendSMS = QPushButton(self.centralwidget)
        self.btnSendSMS.setObjectName(u"btnSendSMS")
        self.btnSendSMS.setGeometry(QRect(120, 410, 201, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnSendSMS.setFont(font1)
        self.btnSendSMS.setStyleSheet(u"background-color: rgb(221, 79, 66);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 140, 191, 20))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 191, 20))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 15, 211, 41))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("SMS Sender", u"SMS Sender", None))
        self.tbPhoneNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+639... / 09...", None))
        self.tbMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hello World...", None))
        self.btnSendSMS.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SMS Sender", None))
    # retranslateUi

