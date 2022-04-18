from math import pi

class Coordinate(object):
    def __init__(self, p, fi, z):
        self.p = p
        self.fi = fi # В радианах
        self.z = z

    def get(self):
        return [self.p, self.fi, self.z]

# Цилиндрическое расстояние 
def get_cylinder_len(point1: Coordinate, point2: Coordinate): 
    if point1.p != point2.p:
        return None
    a = (point1.z - point2.z)**2
        # Расстояние по прямой
        # b = point1.p**2 + point2.p**2 - 2 * cos(abs(point1.fi - point2.fi)) * point1.p * point2.p
    b = min((2 * pi - abs(point1.fi - point2.fi)), abs(point1.fi - point2.fi))**2 * point1.p**2 
    ans = (a + b) ** 0.5
    return ans

# Коническое расстояние (ГРУБО!!! - как диагональ равнобокой трапеции)
def get_cone_len(point1: Coordinate, point2: Coordinate):
    if point1.p == point2.p:
        return None
    a = point1.p * (point1.fi - point2.fi)
    b = point2.p * (point1.fi - point2.fi)
    c = (point1.p - point2.p)**2 + (point1.z - point2.z)**2
    answer = (c + a * b)**0.5
    return answer