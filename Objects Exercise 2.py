class Animal:
    def __init__ (self, animals, territory, sound, legs = 4, ears = 2, is_a_cat = True):
        self.animals = animals
        self.sound = sound,
        self.territory = territory,
        self.ears = ears,
        self.legs = legs
        self.is_a_cat = is_a_cat
    def get_animal(self, n):
        print("Animal object was created")
        if type(n) == str:
            print(n)
        else:
            print("gone")
    def count_legs(self):
        print("The number of legs is")
    def return_legs(self):
        return self.legs
    def number_of_legs(self):
        print(f'{self.legs}')

cats = Animal(["lion", "cheetah", "Leopard", "jaguar" ],
                    ["savanna", "grassland", "rainforest"],
                    ["roar", "snarl", "growl"]
                   )
cats.get_animal("Running started")
cats.count_legs()
print(cats.return_legs())

