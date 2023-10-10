 # pylint: disable=C0103
 # pylint: disable=C0304
 # pylint: disable=C0111

class Animal:
    description = "A living thing made of cells that can move around in a macro scale"
    
class bird(Animal):
    description2 = "A warm-blooded egg-laying vertebrate distinguished by the possession of feathers, wings, and a beak and (typically) by being able to fly."
    

OpiumBird = bird()

print(OpiumBird.description)