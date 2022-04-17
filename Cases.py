import BaseLib as bl

# The Sensor1 and the sensor2 are on different cylindres
def HardCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate, step: int, scy: int, bcy: int):
    # Промежуток, в котором ищем
    minx = min(sensor1.x, sensor2.x)
    maxx = max(sensor1.x, sensor2.x) + 1
    # Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    minans = 9999999
    for x1 in range(minx, maxx, step):
        
        scpoint = bl.Coordinate(x1, scy) # Промежуточная координата на малой окр
        len_sensor1_scpoint = bl.get_len(sensor1, scpoint) # Расстояние до неё
        
        # Нужны для бин поиска
        minxcopy, maxxcopy = minx, maxx
        minlen = 999999 # Минимальное расстояние внутри бин поиска
        
        if True: #FIXME
            m = (maxxcopy + minxcopy)/2 # Середина

            bcpoint = bl.Coordinate(m, bcy) # Промежуточная кооридината на big circle
            len_scpoint_sensor2 = bl.get_len(scpoint, bcpoint) + bl.get_len(bcpoint, sensor2) # Расстояние

            if (len_scpoint_sensor2 < minlen):
                minlen = len_scpoint_sensor2

        while(maxxcopy - minxcopy > step):
            m = (maxxcopy + minxcopy)/2 # Середина

            bcpoint = bl.Coordinate(m, bcy) # Промежуточная кооридината на big circle
            len_scpoint_sensor2 = bl.get_len(scpoint, bcpoint) + bl.get_len(bcpoint, sensor2) # Расстояние
            print(len_scpoint_sensor2)

            if (len_scpoint_sensor2 < minlen):
                minlen = len_scpoint_sensor2
                print(minlen)
        
            # Определение направление бин поиска
            helpbcpoint = bl.Coordinate(m + step, bcy)
            help_len_scpoint_sensor2 = bl.get_len(scpoint, helpbcpoint) + bl.get_len(helpbcpoint, sensor2)
            if(help_len_scpoint_sensor2 > len_scpoint_sensor2):
                maxxcopy = m
            else:
                minxcopy = m

        # Итоговое расстояние внутри одной итерации
        len_s1_s2 = len_sensor1_scpoint + minlen
        if minans > len_s1_s2:
            minans = len_s1_s2
    return minans

# The Sensor1 is on the cylinder; The Sensor2 is on cone
def MiddleCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate, step: int, cy: int):
    # Промежуток, в котором ищем
    minx = min(sensor1.x, sensor2.x)
    maxx = max(sensor1.x, sensor2.x)
    # Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    minans = 9999999 

    while(maxx - minx > step):
            m = (maxx + minx)/2 # Середина
            cpoint = bl.Coordinate(m, cy) # Промежуточная кооридината на circle
            len_sensor1_sensor2 = bl.get_len(sensor1, cpoint) + bl.get_len(cpoint, sensor2) # Расстояние
        
            if (len_sensor1_sensor2 < minans):
                minans = len_sensor1_sensor2
        
            # Определение направление бин поиска
            helpbcpoint = bl.Coordinate(m + step, cy)
            help_len_scpoint_sensor2 = bl.get_len(sensor1, cpoint) + bl.get_len(cpoint, sensor2)
            if(help_len_scpoint_sensor2 > len_sensor1_sensor2):
                maxx = m
            else:
                minx = m
    return minans

def SimpleCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate):
    minans = bl.get_len(sensor1, sensor2)
    return minans