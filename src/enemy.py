from src.character import Character


class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self, target: Character):
        # Attack the target
        target.take_damage(self.damage)