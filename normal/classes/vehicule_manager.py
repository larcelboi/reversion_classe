from normal.classes.vehicule import Vehicule
import jsonpickle

class Vehicule_manager:
    def __init__(self):
        self.lst_vehicule : list[Vehicule] = []


    def add_vehicule(self, vehicule: Vehicule):
        self.lst_vehicule.append(vehicule)

    def save_to_file(self):
        with open("car_management.json", "w",encoding="utf-8") as file:
            file.write(jsonpickle.encode(self,indent=4))

    @staticmethod
    def load_from_file():
        try:
            with open("car_management.json",encoding="utf-8") as file:
                return  jsonpickle.decode(file.read())
        except FileNotFoundError:
            return Vehicule_manager()

gerer_vechile = Vehicule_manager.load_from_file()
