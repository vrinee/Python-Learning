 # pylint: disable=C0103
 # pylint: disable=C0304
 # pylint: disable=C0111


class cordinates:
    __match_args__ = ('x', 'y') 
    def __init__ (self, x, y):
        self.x = x
        self.y = y
point = cordinates(0, 0)

match point:  
    case cordinates(0, 0):
        print("Origin")
    case cordinates(0, y):
        print("Y axis")
    case cordinates(x, 0):
        print("X axis")
    case cordinates(x, y):
        print("Arbitrary point")
        
    
    