import jsonpickle

class Stockage:
    def __init__(self):
        self.lst_tout = []

    def sauvegardder(self):
        with open("Stocker.json","w",encoding="utf-8") as file:
            file.write(jsonpickle.encode(self,indent=4))

    @staticmethod
    def load():
        try:
            with open("Stocker.json","r",encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            return Stockage()


stocker = Stockage.load()