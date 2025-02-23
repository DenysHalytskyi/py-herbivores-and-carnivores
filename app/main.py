class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])

    def dies(self) -> None:
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, pray: Herbivore) -> None:
        if isinstance(pray, Herbivore):
            if not pray.hidden:
                pray.health -= 50
                pray.dies()
