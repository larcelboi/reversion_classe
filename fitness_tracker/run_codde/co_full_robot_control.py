import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from fitness_tracker.ui_enhanced_robot_control import Ui_RobotControlWindow
from fitness_tracker.classes.sous_classes import Drone
from fitness_tracker.classes.robot import Robot
from fitness_tracker.type_enum.enum_mode import Mode

class Track_robot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RobotControlWindow()
        self.ui.setupUi(self)

        for mode_robot in list(Mode):
            self.ui.comboBox.addItem(mode_robot.value)
        self.cacher_altitude()
        self.ui.comboBox_robotType.currentTextChanged.connect(self.cacher_altitude)
        self.ui.lineEdit_robotName.setPlaceholderText("Nom du robot")
        self.ui.lineEdit.setPlaceholderText("True or False")
        self.setWindowTitle("Welcome to robot control")
        self.ui.btn_goToInfo.clicked.connect(self.stacked_widget_page1)
        self.ui.btn_goToDashboard.clicked.connect(self.stacked_widget_page2)
        self.ui.btn_goToSettings.clicked.connect(self.stacked_widget_page3)
        self.ui.btn_createRobot.clicked.connect(self.entrer_information_robot)

    def cacher_altitude(self):
        if self.ui.comboBox_robotType.currentText() == "GroundBot":
            self.ui.spinBox_2.hide()
            self.ui.label_3.hide()
        else:
            self.ui.spinBox_2.show()
            self.ui.label_3.show()
    def entrer_information_robot(self):

        nom = self.ui.lineEdit_robotName.text().capitalize()
        type_robot = self.ui.comboBox_robotType.currentText()
        speed = self.ui.spinBox.value()
        mission_active = self.ui.lineEdit.text().capitalize()
        altitude = self.ui.spinBox_2.value()
        mode_robot = self.ui.comboBox.currentText()



        try:
            if  mission_active.strip() == "":
                raise ValueError("Vous devez remplir la casse Mission active")
            elif mission_active.strip() not in ["True", "False"]:
                raise ValueError("La case Mission active doit être True ou False")
        except Exception as e:
            Robot._liste_erreur.append(e)

        robot_mode = None
        if mode_robot == "Patrol":
            robot_mode = Mode.PATROL
        elif mode_robot == "Search":
            robot_mode = Mode.SEARCH
        elif mode_robot == "RETURN":
            robot_mode = Mode.RETURN

        true_or_false = None
        if mission_active == "True":
            true_or_false = True
        elif mission_active == "False":
            true_or_false = False

        verification_robot = Drone(nom, speed, robot_mode, true_or_false, altitude)

        erreur_str = ""
        if len(Robot._liste_erreur) >=1:
            for chiffre,erreur in  enumerate(Robot._liste_erreur,start=1):
                erreur_str += f"{chiffre}. {erreur}\n"
            QMessageBox.warning(self,"Erreur",erreur_str)
            Robot._liste_erreur = []

    def stacked_widget_page1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def stacked_widget_page2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def stacked_widget_page3(self):
        self.ui.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Track_robot()
    window.show()
    sys.exit(app.exec())