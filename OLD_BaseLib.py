class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return [self.x, self.y]

# Евклидово расстояние
def get_len(point1: Coordinate, point2: Coordinate): 
    ans = (point1.x - point2.x)**2 + (point1.y - point2.y)**2
    ans = ans**0.5
    return ans
