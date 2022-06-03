# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainDialog.ui'
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


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(764, 421)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        dialog.setFont(font)
        dialog.setSizeGripEnabled(True)
        self.horizontalLayout_2 = QHBoxLayout(dialog)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hisDataCheckBox = QCheckBox(self.frame)
        self.hisDataCheckBox.setObjectName(u"hisDataCheckBox")

        self.verticalLayout_2.addWidget(self.hisDataCheckBox)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.endTimeLabel_3 = QLabel(self.groupBox)
        self.endTimeLabel_3.setObjectName(u"endTimeLabel_3")

        self.gridLayout_3.addWidget(self.endTimeLabel_3, 1, 0, 1, 1)

        self.endTimeEdit = QDateTimeEdit(self.groupBox)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        self.endTimeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.endTimeEdit, 1, 1, 1, 2)

        self.startTimeLabel_3 = QLabel(self.groupBox)
        self.startTimeLabel_3.setObjectName(u"startTimeLabel_3")

        self.gridLayout_3.addWidget(self.startTimeLabel_3, 0, 0, 1, 1)

        self.startTimeEdit = QDateTimeEdit(self.groupBox)
        self.startTimeEdit.setObjectName(u"startTimeEdit")
        self.startTimeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.startTimeEdit, 0, 1, 1, 2)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 3)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.captureGapLabel = QLabel(self.frame)
        self.captureGapLabel.setObjectName(u"captureGapLabel")

        self.horizontalLayout_3.addWidget(self.captureGapLabel)

        self.capGapTimeSpin = QSpinBox(self.frame)
        self.capGapTimeSpin.setObjectName(u"capGapTimeSpin")
        self.capGapTimeSpin.setMaximum(99999)

        self.horizontalLayout_3.addWidget(self.capGapTimeSpin)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.testConnectButton = QPushButton(self.groupBox_2)
        self.testConnectButton.setObjectName(u"testConnectButton")

        self.verticalLayout_3.addWidget(self.testConnectButton)

        self.startCaptureButton = QPushButton(self.groupBox_2)
        self.startCaptureButton.setObjectName(u"startCaptureButton")

        self.verticalLayout_3.addWidget(self.startCaptureButton)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.consoleLogText = QPlainTextEdit(self.frame_2)
        self.consoleLogText.setObjectName(u"consoleLogText")

        self.gridLayout_4.addWidget(self.consoleLogText, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u91d1\u521a\u7891\u8ba2\u7968\u4fe1\u606f\u91c7\u96c6", None))
        self.hisDataCheckBox.setText(QCoreApplication.translate("dialog", u"\u5386\u53f2\u6570\u636e\u4e0a\u4f20", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialog", u"\u5386\u53f2\u6570\u636e\u65e5\u671f\u8303\u56f4", None))
        self.endTimeLabel_3.setText(QCoreApplication.translate("dialog", u"\u7ed3\u675f\uff1a", None))
        self.endTimeEdit.setDisplayFormat(QCoreApplication.translate("dialog", u"yyyy/MM/dd HH:mm", None))
        self.startTimeLabel_3.setText(QCoreApplication.translate("dialog", u"\u8d77\u59cb\uff1a", None))
        self.startTimeEdit.setDisplayFormat(QCoreApplication.translate("dialog", u"yyyy/MM/dd HH:mm", None))
        self.captureGapLabel.setText(QCoreApplication.translate("dialog", u"\u91c7\u96c6\u95f4\u9694(\u79d2)\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dialog", u"\u64cd\u4f5c", None))
        self.testConnectButton.setText(QCoreApplication.translate("dialog", u"\u6d4b\u8bd5\u8fde\u63a5", None))
        self.startCaptureButton.setText(QCoreApplication.translate("dialog", u"\u5f00\u59cb\u91c7\u96c6", None))
    # retranslateUi

