class Animal:
    isDog = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

    def in_dog_years(self):
        if not self.isDog:
            return self.age * 7
        else:
            return self.age


snuffy = Animal('Aloysius Snuffleupagus', 25)
garfield = Animal('Garfield', 32)
george = Animal('Curious George', 70)
snoopy = Animal('Snoopy', 60)
