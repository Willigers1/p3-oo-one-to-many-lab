class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # This will call the setter
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        print("GETTING _pet_type")
        return self._pet_type

    @pet_type.setter
    def pet_type(self, new_pet_type):
        print("SETTING _pet_type")
        if new_pet_type not in Pet.PET_TYPES:
            raise Exception(f"{new_pet_type} not in pet types")
        else:
            self._pet_type = new_pet_type


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return a list of pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Set the owner of the pet to this owner
        pet.owner = self

    def get_sorted_pets(self):
        # Call the pets method to get the list of owned pets
        my_pets = self.pets()  # Call the method to get the list of pets
        # Sort the pets by their name in lowercase
        sorted_pets = sorted(my_pets, key=lambda each_pet: each_pet.name.lower())
        return sorted_pets
