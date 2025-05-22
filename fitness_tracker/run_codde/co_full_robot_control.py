import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from fitness_tracker.ui_enhanced_robot_control import Ui_RobotControlWindow
from fitness_tracker.classes.sous_classes import Drone
from fitness_tracker.classes.robot import Robot
from fitness_tracker.type_enum.enum_mode import Mode
from fitness_tracker.classes.sous_classes import Groundrobot
class Track_robot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RobotControlWindow()
        self.ui.setupUi(self)
        self.robot = None

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
        self.ui.btn_startMission.clicked.connect(self.commencer_mission)
        self.ui.btn_emergencyStop.clicked.connect(self.stop_mision)
        self.ui.btn_applySettings.clicked.connect(self.changer_settings)

    def cacher_altitude(self):
        if self.ui.comboBox_robotType.currentText() == "GroundBot":
            self.ui.spinBox_2.hide()
            self.ui.label_3.hide()
            self.ui.spinBox_altitude.hide()
            self.ui.label_altitude.hide()
        else:
            self.ui.spinBox_2.show()
            self.ui.label_3.show()
            self.ui.spinBox_altitude.show()
            self.ui.label_altitude.show()

    def entrer_information_robot(self):
        nom = self.ui.lineEdit_robotName.text().capitalize()
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
        elif mode_robot == "Return":
            robot_mode = Mode.RETURN

        true_or_false = None
        if mission_active == "True":
            true_or_false = True
        elif mission_active == "False":
            true_or_false = False

        verification_robot = None
        if self.ui.comboBox_robotType.currentText() == "DroneBot":
            verification_robot = Drone(nom, speed, robot_mode, true_or_false, altitude)
        elif self.ui.comboBox_robotType.currentText() == "GroundBot":
            verification_robot = Groundrobot(nom, speed, robot_mode, true_or_false)

        erreur_str = ""
        if len(Robot._liste_erreur) >=1:
            for chiffre,erreur in  enumerate(Robot._liste_erreur,start=1):
                erreur_str += f"{chiffre}. {erreur}\n"
            QMessageBox.warning(self,"Erreur",erreur_str)
            Robot._liste_erreur.clear()
            return
        else:
            QMessageBox.information(self, "Completer", f"{verification_robot.name} a été crée")
            self.robot = verification_robot
            print(self.robot)


    def refresh_status(self):
        if self.robot.mision_active:
            self.ui.label_status.setText("Mission: Active")
        elif not self.robot.mision_active:
            self.ui.label_status.setText("Mision: Idle")

    def stop_mision(self):
        existance_robot = self.verification_creation_robot()
        if existance_robot:
            self.robot.emergency_stop()
            self.ui.label_status.setText("Mission: Stopped")

    def commencer_mission(self):
        existance_robot = self.verification_creation_robot()
        if existance_robot:
            self.robot.start_mission()
            if len(Robot._liste_erreur) == 1:
                QMessageBox.warning(self, "Erreur", f"{Robot._liste_erreur[0]}")
                Robot._liste_erreur.clear()
                return
            else:
                self.refresh_status()

    def stacked_widget_page1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def stacked_widget_page2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        existance_robot = self.verification_creation_robot()

        if existance_robot:
            self.ui.label_robotNameDashboard.setText(f"Robot: {self.robot.name}")
            self.refresh_status()



    def stacked_widget_page3(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.afficher_settings()

    def afficher_settings(self):
        existance_robot = self.verification_creation_robot()
        if existance_robot:
            self.ui.spinBox_speed.setValue(self.robot.speed)
            self.ui.comboBox_mode.setCurrentText(self.robot.mode.value)
            if isinstance(self.robot,Drone):
                self.ui.spinBox_altitude.setValue(self.robot.altitude)


    def changer_settings(self):
        existance_robot = self.verification_creation_robot()
        if existance_robot:
            speed = self.ui.spinBox_speed.value()
            mode = self.ui.comboBox_mode.currentText()
            altitude = self.ui.spinBox_altitude.value()

            robot_mode = None
            if mode == "Patrol":
                robot_mode = Mode.PATROL
            elif mode == "Search":
                robot_mode = Mode.SEARCH
            elif mode == "Return":
                robot_mode = Mode.RETURN
            # changement dans les attributs du robot

            self.robot.speed = speed
            self.robot.mode = robot_mode
            if isinstance(self.robot,Drone):
                self.robot.altitude = altitude
        print(self.robot)
    def verification_creation_robot(self):
        if self.robot is None:
            QMessageBox.information(self, "Erreur", f"Veuillez crée le robot pour utiliser l'application")
            return False
        else:
            return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Track_robot()
    window.show()
    sys.exit(app.exec())