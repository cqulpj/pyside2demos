# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cusDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CusDialog(object):
    def setupUi(self, CusDialog):
        if CusDialog.objectName():
            CusDialog.setObjectName(u"CusDialog")
        CusDialog.resize(477, 347)
        self.verticalLayout = QVBoxLayout(CusDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CusDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(CusDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(CusDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(CusDialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(CusDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox = QSpinBox(CusDialog)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(CusDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.dateTimeEdit = QDateTimeEdit(CusDialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.pushButton = QPushButton(CusDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(CusDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(CusDialog)

        QMetaObject.connectSlotsByName(CusDialog)
    # setupUi

    def retranslateUi(self, CusDialog):
        CusDialog.setWindowTitle(QCoreApplication.translate("CusDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CusDialog", u"\u53c2\u65701\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("CusDialog", u"\u53c2\u65702\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CusDialog", u"\u9009\u62e91", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CusDialog", u"\u9009\u62e92", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("CusDialog", u"\u9009\u62e93", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("CusDialog", u"\u9009\u62e94", None))

        self.label_3.setText(QCoreApplication.translate("CusDialog", u"\u53c2\u65703\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("CusDialog", u"\u53c2\u65704\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("CusDialog", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("CusDialog", u"\u53d6\u6d88", None))
    # retranslateUi

