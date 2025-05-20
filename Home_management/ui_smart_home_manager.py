# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smart_home_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainStack = QStackedWidget(self.centralwidget)
        self.mainStack.setObjectName(u"mainStack")
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.layout_register = QVBoxLayout(self.page_register)
        self.layout_register.setObjectName(u"layout_register")
        self.comboBox_deviceType = QComboBox(self.page_register)
        self.comboBox_deviceType.addItem("")
        self.comboBox_deviceType.addItem("")
        self.comboBox_deviceType.addItem("")
        self.comboBox_deviceType.setObjectName(u"comboBox_deviceType")

        self.layout_register.addWidget(self.comboBox_deviceType)

        self.lineEdit_deviceName = QLineEdit(self.page_register)
        self.lineEdit_deviceName.setObjectName(u"lineEdit_deviceName")

        self.layout_register.addWidget(self.lineEdit_deviceName)

        self.deviceInputStack = QStackedWidget(self.page_register)
        self.deviceInputStack.setObjectName(u"deviceInputStack")
        self.input_light = QWidget()
        self.input_light.setObjectName(u"input_light")
        self.layout_light = QVBoxLayout(self.input_light)
        self.layout_light.setObjectName(u"layout_light")
        self.spinBox_brightness = QSpinBox(self.input_light)
        self.spinBox_brightness.setObjectName(u"spinBox_brightness")
        self.spinBox_brightness.setMaximum(100)
        self.spinBox_brightness.setMinimum(0)

        self.layout_light.addWidget(self.spinBox_brightness)

        self.deviceInputStack.addWidget(self.input_light)
        self.input_thermostat = QWidget()
        self.input_thermostat.setObjectName(u"input_thermostat")
        self.layout_thermostat = QVBoxLayout(self.input_thermostat)
        self.layout_thermostat.setObjectName(u"layout_thermostat")
        self.spinBox_temperature = QSpinBox(self.input_thermostat)
        self.spinBox_temperature.setObjectName(u"spinBox_temperature")
        self.spinBox_temperature.setMinimum(10)
        self.spinBox_temperature.setMaximum(30)

        self.layout_thermostat.addWidget(self.spinBox_temperature)

        self.deviceInputStack.addWidget(self.input_thermostat)
        self.input_camera = QWidget()
        self.input_camera.setObjectName(u"input_camera")
        self.layout_camera = QVBoxLayout(self.input_camera)
        self.layout_camera.setObjectName(u"layout_camera")
        self.checkBox_recording = QCheckBox(self.input_camera)
        self.checkBox_recording.setObjectName(u"checkBox_recording")

        self.layout_camera.addWidget(self.checkBox_recording)

        self.deviceInputStack.addWidget(self.input_camera)

        self.layout_register.addWidget(self.deviceInputStack)

        self.pushButton_register = QPushButton(self.page_register)
        self.pushButton_register.setObjectName(u"pushButton_register")

        self.layout_register.addWidget(self.pushButton_register)

        self.mainStack.addWidget(self.page_register)
        self.page_manage = QWidget()
        self.page_manage.setObjectName(u"page_manage")
        self.layout_manage = QVBoxLayout(self.page_manage)
        self.layout_manage.setObjectName(u"layout_manage")
        self.comboBox_selectDevice = QComboBox(self.page_manage)
        self.comboBox_selectDevice.setObjectName(u"comboBox_selectDevice")

        self.layout_manage.addWidget(self.comboBox_selectDevice)

        self.manageDeviceStack = QStackedWidget(self.page_manage)
        self.manageDeviceStack.setObjectName(u"manageDeviceStack")
        self.manage_light = QWidget()
        self.manage_light.setObjectName(u"manage_light")
        self.layout_manage_light = QVBoxLayout(self.manage_light)
        self.layout_manage_light.setObjectName(u"layout_manage_light")
        self.slider_light = QSlider(self.manage_light)
        self.slider_light.setObjectName(u"slider_light")
        self.slider_light.setMaximum(100)
        self.slider_light.setOrientation(Qt.Horizontal)

        self.layout_manage_light.addWidget(self.slider_light)

        self.manageDeviceStack.addWidget(self.manage_light)
        self.manage_thermostat = QWidget()
        self.manage_thermostat.setObjectName(u"manage_thermostat")
        self.layout_manage_thermostat = QVBoxLayout(self.manage_thermostat)
        self.layout_manage_thermostat.setObjectName(u"layout_manage_thermostat")
        self.slider_thermo = QSlider(self.manage_thermostat)
        self.slider_thermo.setObjectName(u"slider_thermo")
        self.slider_thermo.setMinimum(10)
        self.slider_thermo.setMaximum(30)
        self.slider_thermo.setOrientation(Qt.Horizontal)

        self.layout_manage_thermostat.addWidget(self.slider_thermo)

        self.manageDeviceStack.addWidget(self.manage_thermostat)
        self.manage_camera = QWidget()
        self.manage_camera.setObjectName(u"manage_camera")
        self.layout_manage_camera = QVBoxLayout(self.manage_camera)
        self.layout_manage_camera.setObjectName(u"layout_manage_camera")
        self.pushButton_toggleRecording = QPushButton(self.manage_camera)
        self.pushButton_toggleRecording.setObjectName(u"pushButton_toggleRecording")

        self.layout_manage_camera.addWidget(self.pushButton_toggleRecording)

        self.manageDeviceStack.addWidget(self.manage_camera)

        self.layout_manage.addWidget(self.manageDeviceStack)

        self.mainStack.addWidget(self.page_manage)
        self.page_overview = QWidget()
        self.page_overview.setObjectName(u"page_overview")
        self.layout_overview = QVBoxLayout(self.page_overview)
        self.layout_overview.setObjectName(u"layout_overview")
        self.textBrowser_overview = QTextBrowser(self.page_overview)
        self.textBrowser_overview.setObjectName(u"textBrowser_overview")

        self.layout_overview.addWidget(self.textBrowser_overview)

        self.mainStack.addWidget(self.page_overview)

        self.mainLayout.addWidget(self.mainStack)

        self.nav_buttons_layout = QHBoxLayout()
        self.nav_buttons_layout.setObjectName(u"nav_buttons_layout")
        self.btn_goToRegister = QPushButton(self.centralwidget)
        self.btn_goToRegister.setObjectName(u"btn_goToRegister")

        self.nav_buttons_layout.addWidget(self.btn_goToRegister)

        self.btn_goToManage = QPushButton(self.centralwidget)
        self.btn_goToManage.setObjectName(u"btn_goToManage")

        self.nav_buttons_layout.addWidget(self.btn_goToManage)

        self.btn_goToOverview = QPushButton(self.centralwidget)
        self.btn_goToOverview.setObjectName(u"btn_goToOverview")

        self.nav_buttons_layout.addWidget(self.btn_goToOverview)


        self.mainLayout.addLayout(self.nav_buttons_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Smart Home Device Manager", None))
        self.comboBox_deviceType.setItemText(0, QCoreApplication.translate("MainWindow", u"Light", None))
        self.comboBox_deviceType.setItemText(1, QCoreApplication.translate("MainWindow", u"Thermostat", None))
        self.comboBox_deviceType.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera", None))

        self.lineEdit_deviceName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Device Name", None))
        self.spinBox_brightness.setPrefix(QCoreApplication.translate("MainWindow", u"Brightness: ", None))
        self.spinBox_temperature.setPrefix(QCoreApplication.translate("MainWindow", u"Temp \u00b0C: ", None))
        self.checkBox_recording.setText(QCoreApplication.translate("MainWindow", u"Start Recording", None))
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"Register Device", None))
        self.pushButton_toggleRecording.setText(QCoreApplication.translate("MainWindow", u"Toggle Recording", None))
        self.btn_goToRegister.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.btn_goToManage.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.btn_goToOverview.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
    # retranslateUi

