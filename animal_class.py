#create Pet class
class Pet:
#initializing pet's name, age, and species
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        Pet.species = species
    #store species in dictionary
    species_years = {
        'dog': 5,
        'cat': 4,
        'parrot': 9,
        'rabbit': 10,
        'hamster': 26
    }
#calculate pet age in human years based on species
    def pet_human_age(self):
        if Pet.species == 'dog':
            return self.age * 5
        elif Pet.species == 'cat':
            return self.age * 4
        elif Pet.species == 'parrot':
            return self.age * 9
        elif Pet.species == 'rabbit':
            return self.age * 10
        elif Pet.species == 'hamster':
            return self.age * 26
        else:
            return print("not a valid species.")
#get lifespan of species
    def get_lifespan(self):
        return pet.species_years.get(self.species, "Unknown species")  
#creating pet instances
pet1 = Pet("Fluffy", 3, 'dog')
pet2 = Pet("Waffles", 2, 'cat')
pet3 = Pet("bugs", 5, 'rabbit')
#print pet instances
pet_group = [pet1,pet2,pet3]
for pet in pet_group:
    print(pet.name, "is", pet.pet_human_age(), "human years old.")
    print(" The average lifespan for a",pet.species,"is", pet.get_lifespan(),"years. \n")
