from typing import List

from src.item import Item


class Equipment:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item):
        # Add an item to the equipment
        self.items.append(item)

    def remove_item(self, item):
        # Remove an item from the equipment
        self.items.remove(item)