from numpy import arange
import BaseLib as bl

# The Sensor1 is on small cylindre and the sensor2 is on big cylindre
def HardCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate, step: float, scz: int, bcz: int):
    # Промежуток, в котором ищем
    minfi = min(sensor1.fi, sensor2.fi)
    maxfi = max(sensor1.fi, sensor2.fi)
    # Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    minans = 9999999 

    for fi1 in arange(minfi, maxfi, step):        
        scpoint = bl.Coordinate(sensor1.p, fi1, scz) # Промежуточная координата на малой окр
        len_sensor1_scpoint = bl.get_cylinder_len(sensor1, scpoint) # Расстояние до неё
        
        # Нужны для бин поиска
        minficopy, maxficopy = minfi, maxfi
        minlen = 999999 # Минимальное расстояние внутри бин поиска
        while(maxficopy - minficopy > step):
            m = (maxficopy + minficopy)/2 # Середина
            bcpoint = bl.Coordinate(sensor2.p, m, bcz) # Промежуточная кооридината на big circle
            len_scpoint_sensor2 = bl.get_cone_len(scpoint, bcpoint) + bl.get_cylinder_len(bcpoint, sensor2) # Расстояние
        
            if (len_scpoint_sensor2 < minlen):
                minlen = len_scpoint_sensor2
        
            # Определение направление бин поиска
            helpbcpoint = bl.Coordinate(sensor2.p, m + step, bcz)
            help_len_scpoint_sensor2 = bl.get_cone_len(scpoint, helpbcpoint) + bl.get_cylinder_len(helpbcpoint, sensor2)
            if(help_len_scpoint_sensor2 > len_scpoint_sensor2):
                maxficopy = m
            else:
                minficopy = m
        
        # Итоговое расстояние внутри одной итерации
        len_s1_s2 = len_sensor1_scpoint + minlen
        if minans > len_s1_s2:
            minans = len_s1_s2
    return minans

# The Sensor1 is on the cylinder; The Sensor2 is on cone
def MiddleCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate, step: int, cz: int):
    # Промежуток, в котором ищем
    minfi = min(sensor1.fi, sensor2.fi)
    maxfi = max(sensor1.fi, sensor2.fi)
    # Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    minans = 9999999 

    while(maxfi - minfi > step):
            m = (maxfi + minfi)/2 # Середина
            cpoint = bl.Coordinate(sensor1.p, m, cz) # Промежуточная кооридината на circle
            len_sensor1_sensor2 = bl.get_cylinder_len(sensor1, cpoint) + bl.get_cone_len(cpoint, sensor2) # Расстояние
        
            if (len_sensor1_sensor2 < minans):
                minans = len_sensor1_sensor2
        
            # Определение направление бин поиска
            helpbcpoint = bl.Coordinate(sensor1.p, m + step, cz)
            help_len_scpoint_sensor2 = bl.get_cylinder_len(sensor1, cpoint) + bl.get_cone_len(cpoint, sensor2)
            if(help_len_scpoint_sensor2 > len_sensor1_sensor2):
                maxfi = m
            else:
                minfi = m
    return minans

# flag = 0: cylinder, flag = 1: cone
def SimpleCase(sensor1: bl.Coordinate, sensor2: bl.Coordinate, flag: bool):
    if flag == 0: 
        minans = bl.get_cylinder_len(sensor1, sensor2)
    else:
        minans = bl.get_cone_len(sensor1, sensor2)
    return minans