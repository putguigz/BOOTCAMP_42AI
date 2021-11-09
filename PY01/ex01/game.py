class GotCharacter:
    def __init__(self, first_name="None", is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """LES GENTILS"""
    def __init__(self, first_name="None", is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming Jean-Neige"

        def print_house_words(self):
            print(self.house_words)

        def die(self):
            self.is_alive = False

class Lannister(GotCharacter):
    """LES MECHANTS"""
    def __init__(self, first_name="None", is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Lannister always pay their debts"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
