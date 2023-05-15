from src.equipment import Equipment


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.equipment = Equipment()


    def attack(self, target):
        # Perform an attack action on the target
        pass

    def take_damage(self, damage):
        # Reduce the character's health by the damage amount
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.defeated()

    def defeated(self):
        return self.equipment
