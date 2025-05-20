import sys

from PySide6.QtCore import QMessageLogContext
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from Home_management.type_enum.type_device import Device_type
from Home_management.ui_smart_home_manager import Ui_MainWindow
from classes_sous import Light,Camera,Thermostat
from stockage import stocker

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.refresh_tout()

        self.ui.comboBox_deviceType.currentTextChanged.connect(self.device_type_changed)
        self.ui.pushButton_register.clicked.connect(self.gerer_class)
        self.ui.btn_goToRegister.clicked.connect(self.set_page_register)
        self.ui.btn_goToManage.clicked.connect(self.set_page_manage)
        self.ui.btn_goToOverview.clicked.connect(self.set_page_overview)
        self.ui.comboBox_selectDevice.currentIndexChanged.connect(self.changing_stuff)
        self.ui.pushButton_toggleRecording.clicked.connect(self.changer_toggle)
        self.ui.slider_light.valueChanged.connect(self.changer_bright_thermo)

    def obtenir_value_slidder_bar(self):
        valeur_slide_bar = self.ui.slider_light.value()
        print(valeur_slide_bar)
        return valeur_slide_bar

    def changer_bright_thermo(self):
        nom_combo_box = self.ui.comboBox_selectDevice.currentText()
        print(nom_combo_box)
        valeur_slide_bar = self.obtenir_value_slidder_bar()
        for personne in stocker.lst_tout:
            if personne.name == nom_combo_box:
                if isinstance(personne, Light) and hasattr(personne,"set_brightness"):
                        personne.set_brightness(valeur_slide_bar)
                        stocker.sauvegardder()
                        break
                elif isinstance(personne, Thermostat) and hasattr(personne,"set_temperature"):
                        personne.set_temperature(valeur_slide_bar)
                        stocker.sauvegardder()
                        break
        self.afficher_device()


    def verification_personne_creer(self,verification):
        if len(stocker.lst_tout) == 0:
            return True
        for personne in stocker.lst_tout:
            if personne.name == verification.name:
                QMessageBox.warning(self,"Nom déjà crée",f"{verification.name} a déjà été crée")
                return False
        return True

    def changer_toggle(self):
        device_camera,index = self.changing_stuff()
        recording = None
        if device_camera.is_recording:
            recording = True
        else:
            recording = False

        if hasattr(device_camera, 'toggle_recording'):
            device_camera.toggle_recording(recording)
            stocker.lst_tout[index] = device_camera
            stocker.sauvegardder()
            self.afficher_device()

    def changing_stuff(self):
        nom_persone = self.ui.comboBox_selectDevice.currentText()
        device_camera = None
        idx = None

        for i, device in enumerate(stocker.lst_tout):
            if nom_persone == device.name and isinstance(device, Light):
                self.ui.manageDeviceStack.setCurrentIndex(1)
                break
            elif nom_persone == device.name and isinstance(device, Camera):
                device_camera = device
                idx = i
                self.ui.manageDeviceStack.setCurrentIndex(2)
            elif nom_persone == device.name and isinstance(device, Thermostat):
                self.ui.manageDeviceStack.setCurrentIndex(0)
                break

        return device_camera, idx

    def refresh_tout(self):
        self.afficher_device()
        self.afficher_device_manage()

    def afficher_device_manage(self):
        self.ui.comboBox_selectDevice.clear()
        for nom in stocker.lst_tout:
            self.ui.comboBox_selectDevice.addItem(f"{nom.name}")
    def afficher_device(self):
        string_device = ""
        for device in stocker.lst_tout:
            string_device += f"{device}\n"
        self.ui.textBrowser_overview.setText(string_device)

    def set_page_register(self):
        self.ui.mainStack.setCurrentIndex(0)
    def set_page_manage(self):
        self.ui.mainStack.setCurrentIndex(1)

    def set_page_overview(self):
        self.ui.mainStack.setCurrentIndex(2)

    def gerer_class(self):
        if self.ui.deviceInputStack.currentIndex() == 0:
            self.light_device()
        elif self.ui.deviceInputStack.currentIndex() == 1:
            self.thermostat_device()
        elif self.ui.deviceInputStack.currentIndex() == 2:
            self.camera_device()

    def device_type_changed(self):
        device_type = self.ui.comboBox_deviceType.currentText()
        if device_type == "Light":
            self.ui.deviceInputStack.setCurrentIndex(0)
        elif device_type == "Camera":
            self.ui.deviceInputStack.setCurrentIndex(2)
        elif device_type == "Thermostat":
            self.ui.deviceInputStack.setCurrentIndex(1)

    def light_device(self):
        nom = self.ui.lineEdit_deviceName.text()
        brightness_level = int(self.ui.spinBox_brightness.value())
        valeur = Device_type.LIGHT.value
        try:
            verification = Light(nom, valeur, True, brightness_level)
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"{e}")
            return
        else:
            if verification:
                if  self.verification_personne_creer(verification):
                    QMessageBox.information(self,"Sauvegarder",f"{verification.name} a été enregistré")
                    stocker.lst_tout.append(verification)
                    stocker.sauvegardder()
                    self.refresh_tout()


    def thermostat_device(self):
        nom = self.ui.lineEdit_deviceName.text()
        print(nom)
        temperature = int(self.ui.spinBox_temperature.value())
        valeur = Device_type.THERMOSTAT.value
        try:
            verification = Thermostat(nom, valeur, True, temperature)
        except Exception as e:
            QMessageBox.warning(self,"Erreur",f"{e}")
            return
        else:
            if verification:
                if  self.verification_personne_creer(verification):
                    QMessageBox.information(self,"Sauvegarder",f"{verification.name} a été enregistré")
                    stocker.lst_tout.append(verification)
                    stocker.sauvegardder()
                    self.refresh_tout()

    def camera_device(self):
        nom = self.ui.lineEdit_deviceName.text()
        recording = self.ui.checkBox_recording.checkState()
        print(recording)
        valeur = Device_type.THERMOSTAT.value
        try:
            if recording.value == 2:
                verification = Camera(nom, valeur, True, True)
            else:
                verification = Camera(nom, valeur, True, False)
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"{e}")
            return
        else:
            if verification:
                if  self.verification_personne_creer(verification):
                    QMessageBox.information(self,"Sauvegarder",f"{verification.name} a été enregistré")
                    stocker.lst_tout.append(verification)
                    stocker.sauvegardder()
                    self.refresh_tout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())