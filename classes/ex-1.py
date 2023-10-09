 # pylint: disable=C0103
 # pylint: disable=C0304
 # pylint: disable=C0111


class var:
    def __init__(self, name, typeOf):
        self.name = name
        self.type = typeOf
        

cats = var("cats", "int")
dogs = var("dogs", "int")

print(cats.name)
print(cats.type)
print(dogs.name)
print(dogs.type)
 