# This is a sample Python script.
from src.enemy import Enemy
from src.equipment import Equipment
from src.item import Item
from src.user import User


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class GameMaster:
    def __init__(self):
        self.enemies = []
        self.users = []

    def create_enemy(self, name, health, damage, item_names):
        enemy = Enemy(name, health, damage)
        equipment = Equipment()
        for item_name in item_names:
            item = Item(item_name)
            equipment.add_item(item)
        enemy.equipment = equipment
        self.enemies.append(enemy)

    def create_user(self, name, health):
        user = User(name, health)
        self.users.append(user)




def example():
    # Example usage
    game_master = GameMaster()

    # Create enemies with equipment and items
    game_master.create_enemy("Goblin", 100, 10, ["Dagger", "Potion"])
    game_master.create_enemy("Orc", 150, 15, ["Axe", "Shield"])

    # Create users
    game_master.create_user("Player 1", 200)
    game_master.create_user("Player 2", 250)

    # Accessing the created enemies and users
    enemies = game_master.enemies
    users = game_master.users

    # Print enemy information
    for enemy in enemies:
        print(f"Enemy: {enemy.name}, Health: {enemy.health}, Damage: {enemy.damage}")
        print("Equipment:")
        for item in enemy.equipment.items:
            print(f"- {item.name}")
        print()

    # Print user information
    for user in users:
        print(f"User: {user.name}, Health: {user.health}")
        print()

    pass
if __name__ == '__main__':
    example()