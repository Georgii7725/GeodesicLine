from math import pi

# fi считается по X`
def trans(x, y):
    if y >= 104:
        p = 192 / pi
        fi = x * pi / 192
    elif y < 0:
        p = 255 / pi
        fi = x * pi / 255
    else:
        p = (80832 - 192 * y) / (371 * pi)
        fi = x * pi / 255
    z = y
    return p, fi, z