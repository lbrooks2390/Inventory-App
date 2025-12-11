# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Inventory(object):
    def setupUi(self, Inventory):
        if not Inventory.objectName():
            Inventory.setObjectName(u"Inventory")
        Inventory.resize(400, 300)

        self.pushButton = QPushButton(Inventory)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 210, 111, 32))

        self.pushButton_2 = QPushButton(Inventory)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 240, 111, 32))

        self.pushButton_3 = QPushButton(Inventory)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 100, 161, 32))

        self.lineEdit = QLineEdit(Inventory)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 60, 231, 21))

        self.lineEdit_2 = QLineEdit(Inventory)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 20, 231, 21))

        self.pushButton_4 = QPushButton(Inventory)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(200, 140, 161, 32))

        self.label = QLabel(Inventory)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 58, 16))

        self.label_2 = QLabel(Inventory)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(17, 60, 111, 20))

        self.textBrowser = QTextBrowser(Inventory)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 100, 161, 181))

        self.retranslateUi(Inventory)
        QMetaObject.connectSlotsByName(Inventory)

    def retranslateUi(self, Inventory):
        Inventory.setWindowTitle(QCoreApplication.translate("Inventory", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Inventory", u"View Inventory", None))
        self.pushButton_2.setText(QCoreApplication.translate("Inventory", u"Delete Inventory ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Inventory", u"Add Item", None))
        self.pushButton_4.setText(QCoreApplication.translate("Inventory", u"Remove Item", None))
        self.label.setText(QCoreApplication.translate("Inventory", u"        Item", None))
        self.label_2.setText(QCoreApplication.translate("Inventory", u"    Number of item", None))