import BaseLib as bl
import Cases as c
from trans import trans
hp = ['x: ', 'y: ']
scz = int(input("Введите ординату малой окружности: ")) # Small circle
bcz = int(input("Введите ординату бОльшей окружности: ")) # Big circle
print("Введите координаты первой точки: ")
p, fi, z = trans(*[float(input(hp[i])) for i in range(2)])
sensor1 = bl.Coordinate(p, fi, z)
print("Введите координаты второй точки: ")
p, fi, z = trans(*[float(input(hp[i])) for i in range(2)])
sensor2 = bl.Coordinate(p, fi, z)
step = float(input("Введите скорость поиска (<=1): "))

# Ориентироваться можно и на z, и на p
if (sensor1.z > scz and sensor2.z > scz) or (sensor1.z < bcz and sensor2.z < bcz):
    answer = c.SimpleCase(sensor1, sensor2, 0)
if (sensor1.z < scz and sensor1.z > bcz and sensor2.z < scz and sensor2.z > bcz):
    answer = c.SimpleCase(sensor1, sensor2, 1)
if (sensor1.z > scz and sensor2.z < bcz):
    answer = c.HardCase(sensor1, sensor2, step, scz, bcz)
if (sensor1.z < bcz and sensor2.z > scz):
    answer = c.HardCase(sensor2, sensor1, step, bcz, scz)
if (sensor1.z < scz and sensor1.z > bcz and sensor2.z < bcz)  or (sensor1.z < scz and sensor1.z > bcz and sensor2.z > scz):
    answer = c.MiddleCase(sensor2, sensor1, step, bcz)
if (sensor2.z < scz and sensor2.z > bcz and sensor1.z < bcz) or (sensor2.z < scz and sensor2.z > bcz and sensor1.z > scz):
    answer = c.MiddleCase(sensor1, sensor2, step, scz)
print(answer)