import BaseLib as bl
import Cases as c

hp = ['x: ', 'y: ']
scy = 104 # int(input("Введите ординату малой окружности: ")) # Small circle
lsc = 384 # int(input("Введите длину малой окружности: "))
bcy = 0   # int(input("Введите ординату бОльшей окружности: ")) # Big circle
lbc = 510 # int(input("Введите длину бОльшей окружности: "))
print("Введите координаты первой точки: ")
sensor1 = bl.Coordinate(*[int(input(hp[i])) for i in range(2)])
print("Введите координаты второй точки: ")
sensor2 = bl.Coordinate(*[int(input(hp[i])) for i in range(2)])
step = 1  # int(input("Введите скорость поиска (<=1): "))

# Решение проблемы разверстки
if abs(sensor2.x - sensor1.x) > lsc / 2: #FIXME
    if sensor1.x < sensor2.x:
        # sensor1.x < 0; sensor2.x > 0
        sensor2.x = sensor1.x + lsc + sensor1.x - sensor2.x
    else:
        # sensor1.x > 0; sensor2.x < 0
        sensor1.x = sensor2.x + lsc + sensor2.x - sensor1.x

if (sensor1.y > scy and sensor2.y > scy) or (sensor1.y < bcy and sensor2.y < bcy) or (sensor1.y < scy and sensor1.y > bcy and sensor2.y < scy and sensor2.y > bcy):
    answer = c.SimpleCase(sensor1, sensor2)
if (sensor1.y > scy and sensor2.y < bcy):
    answer = c.HardCase(sensor1, sensor2, step, scy, bcy)
if (sensor1.y < bcy and sensor2.y > scy):
    answer = c.HardCase(sensor1, sensor2, step, bcy, scy)
if (sensor1.y < scy and sensor1.y > bcy and sensor2.y < bcy)  or (sensor2.y < scy and sensor2.y > bcy and sensor1.y < bcy):
    answer = c.MiddleCase(sensor1, sensor2, step, bcy)
if (sensor1.y < scy and sensor1.y > bcy and sensor2.y > scy)  or (sensor2.y < scy and sensor2.y > bcy and sensor1.y > scy):
    answer = c.MiddleCase(sensor1, sensor2, step, scy)
print(answer)
