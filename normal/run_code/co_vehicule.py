import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from normal.ui_vehicule import Ui_MainWindow
from normal.classes.vehicule_manager import gerer_vechile
from normal.classes.vehicule import Vehicule
from normal.vehicule_type.type_vehicule import Type_vehicule

class Vehicule_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface = Ui_MainWindow()
        self.interface.setupUi(self)

        # connection boutton
        self.interface.pushButton_add.clicked.connect(self.ajouter_personne)

        # adding the type of cas into the combobox

    def ajouter_personne(self):
        nom = self.interface.lineEdit_name.text()
        type_voiture = self.interface.comboBox_type.currentText()
        if type_voiture == 'Car':
            type_voiture = Type_vehicule.CAR
        elif type_voiture == 'Truck':
            type_voiture = Type_vehicule.TRUCK
        elif type_voiture == 'Bike':
            type_voiture = Type_vehicule.BIKE


        la_voiture = Vehicule(nom, type_voiture)
        print(f"la voiture {la_voiture.name} a été crée")
        self.sauvegarder_personne(la_voiture)

    def sauvegarder_personne(self,la_voiture):
        gerer_vechile.lst_vehicule.append(la_voiture) # ajouter la voiture dans la liste

        gerer_vechile.save_to_file() #sauvegarder la nouvelle voiture
        print(la_voiture,"a été sauvegardée")
        self.afficher_voiture()

    def afficher_voiture(self):
        texte_voiture  = ""

        for voiture in gerer_vechile.lst_vehicule:
            texte_voiture += f"{voiture}\n"
        self.interface.textBrowser.setText(texte_voiture)
        self.interface.stackedWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vehicule_main()
    window.show()
    sys.exit(app.exec())
