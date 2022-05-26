# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addDeviceFrame.ui'
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


class Ui_AddDeviceDialog(object):
    def setupUi(self, AddDeviceDialog):
        if not AddDeviceDialog.objectName():
            AddDeviceDialog.setObjectName(u"AddDeviceDialog")
        AddDeviceDialog.resize(600, 340)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        AddDeviceDialog.setFont(font)
        self.gridLayout = QGridLayout(AddDeviceDialog)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(AddDeviceDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 2, 1)

        self.chooseFileButton = QPushButton(AddDeviceDialog)
        self.chooseFileButton.setObjectName(u"chooseFileButton")
        self.chooseFileButton.setMinimumSize(QSize(120, 0))
        self.chooseFileButton.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.chooseFileButton, 4, 0, 1, 1)

        self.label = QLabel(AddDeviceDialog)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(AddDeviceDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.ServerIPText = QLabel(AddDeviceDialog)
        self.ServerIPText.setObjectName(u"ServerIPText")

        self.gridLayout.addWidget(self.ServerIPText, 0, 1, 1, 3)

        self.appsComboBox = QComboBox(AddDeviceDialog)
        self.appsComboBox.setObjectName(u"appsComboBox")

        self.gridLayout.addWidget(self.appsComboBox, 1, 1, 1, 3)

        self.devprofileComboBox = QComboBox(AddDeviceDialog)
        self.devprofileComboBox.setObjectName(u"devprofileComboBox")

        self.gridLayout.addWidget(self.devprofileComboBox, 2, 1, 1, 3)

        self.infoText = QTextBrowser(AddDeviceDialog)
        self.infoText.setObjectName(u"infoText")

        self.gridLayout.addWidget(self.infoText, 7, 0, 1, 4)

        self.filePathText = QLabel(AddDeviceDialog)
        self.filePathText.setObjectName(u"filePathText")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathText.sizePolicy().hasHeightForWidth())
        self.filePathText.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.filePathText, 4, 1, 1, 2)

        self.startImportButton = QPushButton(AddDeviceDialog)
        self.startImportButton.setObjectName(u"startImportButton")

        self.gridLayout.addWidget(self.startImportButton, 4, 3, 1, 1)


        self.retranslateUi(AddDeviceDialog)

        QMetaObject.connectSlotsByName(AddDeviceDialog)
    # setupUi

    def retranslateUi(self, AddDeviceDialog):
        AddDeviceDialog.setWindowTitle(QCoreApplication.translate("AddDeviceDialog", u"\u8bbe\u5907\u6279\u91cf\u5bfc\u5165\u5de5\u5177", None))
        self.label_4.setText(QCoreApplication.translate("AddDeviceDialog", u" \u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.chooseFileButton.setText(QCoreApplication.translate("AddDeviceDialog", u"\u6d4f\u89c8", None))
        self.label.setText(QCoreApplication.translate("AddDeviceDialog", u" \u670d\u52a1\u5668IP\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("AddDeviceDialog", u" \u5173\u8054\u5e94\u7528\uff1a", None))
        self.ServerIPText.setText(QCoreApplication.translate("AddDeviceDialog", u"127.0.0.1", None))
        self.filePathText.setText(QCoreApplication.translate("AddDeviceDialog", u"\u6587\u4ef6\u8def\u5f84", None))
        self.startImportButton.setText(QCoreApplication.translate("AddDeviceDialog", u"\u5f00\u59cb\u5bfc\u5165", None))
    # retranslateUi

