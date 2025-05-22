# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enhanced_robot_control.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_RobotControlWindow(object):
    def setupUi(self, RobotControlWindow):
        if not RobotControlWindow.objectName():
            RobotControlWindow.setObjectName(u"RobotControlWindow")
        RobotControlWindow.resize(261, 238)
        self.centralwidget = QWidget(RobotControlWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_robotInfo = QWidget()
        self.page_robotInfo.setObjectName(u"page_robotInfo")
        self.formLayout_robotInfo = QFormLayout(self.page_robotInfo)
        self.formLayout_robotInfo.setObjectName(u"formLayout_robotInfo")
        self.label_name = QLabel(self.page_robotInfo)
        self.label_name.setObjectName(u"label_name")

        self.formLayout_robotInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.lineEdit_robotName = QLineEdit(self.page_robotInfo)
        self.lineEdit_robotName.setObjectName(u"lineEdit_robotName")

        self.formLayout_robotInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_robotName)

        self.label_type = QLabel(self.page_robotInfo)
        self.label_type.setObjectName(u"label_type")

        self.formLayout_robotInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_type)

        self.comboBox_robotType = QComboBox(self.page_robotInfo)
        self.comboBox_robotType.addItem("")
        self.comboBox_robotType.addItem("")
        self.comboBox_robotType.setObjectName(u"comboBox_robotType")

        self.formLayout_robotInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_robotType)

        self.btn_createRobot = QPushButton(self.page_robotInfo)
        self.btn_createRobot.setObjectName(u"btn_createRobot")

        self.formLayout_robotInfo.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.btn_createRobot)

        self.label = QLabel(self.page_robotInfo)
        self.label.setObjectName(u"label")

        self.formLayout_robotInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label)

        self.spinBox = QSpinBox(self.page_robotInfo)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout_robotInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.label_2 = QLabel(self.page_robotInfo)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_robotInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.page_robotInfo)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_robotInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.page_robotInfo)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_robotInfo.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.spinBox_2 = QSpinBox(self.page_robotInfo)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.formLayout_robotInfo.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spinBox_2)

        self.label_4 = QLabel(self.page_robotInfo)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_robotInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.comboBox = QComboBox(self.page_robotInfo)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_robotInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.stackedWidget.addWidget(self.page_robotInfo)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.layout_dashboard = QVBoxLayout(self.page_dashboard)
        self.layout_dashboard.setObjectName(u"layout_dashboard")
        self.label_robotNameDashboard = QLabel(self.page_dashboard)
        self.label_robotNameDashboard.setObjectName(u"label_robotNameDashboard")

        self.layout_dashboard.addWidget(self.label_robotNameDashboard)

        self.label_status = QLabel(self.page_dashboard)
        self.label_status.setObjectName(u"label_status")

        self.layout_dashboard.addWidget(self.label_status)

        self.btn_startMission = QPushButton(self.page_dashboard)
        self.btn_startMission.setObjectName(u"btn_startMission")

        self.layout_dashboard.addWidget(self.btn_startMission)

        self.btn_emergencyStop = QPushButton(self.page_dashboard)
        self.btn_emergencyStop.setObjectName(u"btn_emergencyStop")

        self.layout_dashboard.addWidget(self.btn_emergencyStop)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.layout_settings = QFormLayout(self.page_settings)
        self.layout_settings.setObjectName(u"layout_settings")
        self.label_speed = QLabel(self.page_settings)
        self.label_speed.setObjectName(u"label_speed")

        self.layout_settings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_speed)

        self.spinBox_speed = QSpinBox(self.page_settings)
        self.spinBox_speed.setObjectName(u"spinBox_speed")
        self.spinBox_speed.setMaximum(100)

        self.layout_settings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_speed)

        self.label_mode = QLabel(self.page_settings)
        self.label_mode.setObjectName(u"label_mode")

        self.layout_settings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_mode)

        self.comboBox_mode = QComboBox(self.page_settings)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")

        self.layout_settings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_mode)

        self.label_altitude = QLabel(self.page_settings)
        self.label_altitude.setObjectName(u"label_altitude")

        self.layout_settings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_altitude)

        self.spinBox_altitude = QSpinBox(self.page_settings)
        self.spinBox_altitude.setObjectName(u"spinBox_altitude")
        self.spinBox_altitude.setMaximum(500)

        self.layout_settings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_altitude)

        self.btn_applySettings = QPushButton(self.page_settings)
        self.btn_applySettings.setObjectName(u"btn_applySettings")

        self.layout_settings.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.btn_applySettings)

        self.stackedWidget.addWidget(self.page_settings)

        self.mainLayout.addWidget(self.stackedWidget)

        self.navButtons = QHBoxLayout()
        self.navButtons.setObjectName(u"navButtons")
        self.btn_goToInfo = QPushButton(self.centralwidget)
        self.btn_goToInfo.setObjectName(u"btn_goToInfo")

        self.navButtons.addWidget(self.btn_goToInfo)

        self.btn_goToDashboard = QPushButton(self.centralwidget)
        self.btn_goToDashboard.setObjectName(u"btn_goToDashboard")

        self.navButtons.addWidget(self.btn_goToDashboard)

        self.btn_goToSettings = QPushButton(self.centralwidget)
        self.btn_goToSettings.setObjectName(u"btn_goToSettings")

        self.navButtons.addWidget(self.btn_goToSettings)


        self.mainLayout.addLayout(self.navButtons)

        RobotControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RobotControlWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RobotControlWindow)
    # setupUi

    def retranslateUi(self, RobotControlWindow):
        RobotControlWindow.setWindowTitle(QCoreApplication.translate("RobotControlWindow", u"Robot Control Panel", None))
        self.label_name.setText(QCoreApplication.translate("RobotControlWindow", u"Robot Name", None))
        self.label_type.setText(QCoreApplication.translate("RobotControlWindow", u"Robot Type", None))
        self.comboBox_robotType.setItemText(0, QCoreApplication.translate("RobotControlWindow", u"GroundBot", None))
        self.comboBox_robotType.setItemText(1, QCoreApplication.translate("RobotControlWindow", u"DroneBot", None))

        self.btn_createRobot.setText(QCoreApplication.translate("RobotControlWindow", u"Create Robot", None))
        self.label.setText(QCoreApplication.translate("RobotControlWindow", u"Speed", None))
        self.label_2.setText(QCoreApplication.translate("RobotControlWindow", u"Miission active", None))
        self.label_3.setText(QCoreApplication.translate("RobotControlWindow", u"Altitude", None))
        self.label_4.setText(QCoreApplication.translate("RobotControlWindow", u"Mode robot", None))
        self.label_robotNameDashboard.setText(QCoreApplication.translate("RobotControlWindow", u"Robot: --", None))
        self.label_status.setText(QCoreApplication.translate("RobotControlWindow", u"Status: Idle", None))
        self.btn_startMission.setText(QCoreApplication.translate("RobotControlWindow", u"Start Mission", None))
        self.btn_emergencyStop.setText(QCoreApplication.translate("RobotControlWindow", u"Emergency Stop", None))
        self.label_speed.setText(QCoreApplication.translate("RobotControlWindow", u"Speed (0\u2013100)", None))
        self.label_mode.setText(QCoreApplication.translate("RobotControlWindow", u"Mode", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("RobotControlWindow", u"Patrol", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("RobotControlWindow", u"Search", None))
        self.comboBox_mode.setItemText(2, QCoreApplication.translate("RobotControlWindow", u"Return", None))

        self.label_altitude.setText(QCoreApplication.translate("RobotControlWindow", u"Altitude", None))
        self.btn_applySettings.setText(QCoreApplication.translate("RobotControlWindow", u"Apply Settings", None))
        self.btn_goToInfo.setText(QCoreApplication.translate("RobotControlWindow", u"Robot Info", None))
        self.btn_goToDashboard.setText(QCoreApplication.translate("RobotControlWindow", u"Dashboard", None))
        self.btn_goToSettings.setText(QCoreApplication.translate("RobotControlWindow", u"Settings", None))
    # retranslateUi

