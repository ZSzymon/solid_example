from src.character import Character


class User(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, target):
        # Attack the target
        target.take_damage(self.calculate_damage())

    def calculate_damage(self):
        return 55