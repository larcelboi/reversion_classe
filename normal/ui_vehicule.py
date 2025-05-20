# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout.addWidget(self.pushButton_add)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_input = QWidget()
        self.page_input.setObjectName(u"page_input")
        self.verticalLayout_2 = QVBoxLayout(self.page_input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_name = QLineEdit(self.page_input)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_2.addWidget(self.lineEdit_name)

        self.comboBox_type = QComboBox(self.page_input)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.verticalLayout_2.addWidget(self.comboBox_type)

        self.stackedWidget.addWidget(self.page_input)
        self.page_output = QWidget()
        self.page_output.setObjectName(u"page_output")
        self.verticalLayout_3 = QVBoxLayout(self.page_output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.page_output)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.page_output)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vehicle Registry", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add Vehicle", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter vehicle name", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Car", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Truck", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Bike", None))

    # retranslateUi

