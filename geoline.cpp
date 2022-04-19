#include <cmath>
#include <iostream>
using namespace std;

class Coordinate{
    public:
    float x, y;
    Coordinate(float initX, float initY){
        x = initX;
        y = initY;
    }
    void get(){
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

float get_len(Coordinate point1, Coordinate point2){
    float ans = pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2);
    ans = pow(ans, 0.5);
    return ans;
}

// The Sensor1 && the sensor2 are on different cylindres
float HardCase(Coordinate sensor1, Coordinate sensor2, float step, int scy, int bcy){
    // Промежуток, в котором ищем
    float minx = min(sensor1.x, sensor2.x);
    float maxx = max(sensor1.x, sensor2.x);
    // Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    float minans = 9999999;

    for(float x1 = minx; x1 <= maxx; x1 += step){ 
        Coordinate scpoint(x1, scy); // Промежуточная координата на малой окр
        float len_sensor1_scpoint = get_len(sensor1, scpoint); // Расстояние до неё
        
        // Нужны для бин поиска
        float minxcopy = minx, maxxcopy = maxx;
        float minlen = 999999; // Минимальное расстояние внутри бин поиска
        
        do{
            float m = (maxxcopy + minxcopy)/2; // Середина
            Coordinate bcpoint(m, bcy); // Промежуточная кооридината на big circle
            float len_scpoint_sensor2 = get_len(scpoint, bcpoint) + get_len(bcpoint, sensor2); // Расстояние
            if (len_scpoint_sensor2 < minlen){ minlen = len_scpoint_sensor2; }
            // Определение направление бин поиска
            Coordinate helpbcpoint(m + step, bcy);
            float help_len_scpoint_sensor2 = get_len(scpoint, helpbcpoint) + get_len(helpbcpoint, sensor2);
            if(help_len_scpoint_sensor2 > len_scpoint_sensor2){ maxxcopy = m; }
            else { minxcopy = m; }

        } while(maxxcopy - minxcopy > step);

        // Итоговое расстояние внутри одной итерации
        float len_s1_s2 = len_sensor1_scpoint + minlen;
        if (minans > len_s1_s2) { minans = len_s1_s2; }
    }
    return minans;
}

// The Sensor1 is on the cylinder; The Sensor2 is on cone
float MiddleCase(Coordinate sensor1, Coordinate sensor2, float step, int cy){
    // Промежуток, в котором ищем
    float minx = min(sensor1.x, sensor2.x);
    float maxx = max(sensor1.x, sensor2.x);
    // Полное расстояние между сенсароми. Мы ищем мин значение этой штуки
    float minans = 9999999;
    do{
        float m = (maxx + minx)/2; // Середина
        Coordinate cpoint(m, cy); // Промежуточная кооридината на circle
        float len_sensor1_sensor2 = get_len(sensor1, cpoint) + get_len(cpoint, sensor2); // Расстояние
        
        if (len_sensor1_sensor2 < minans){ minans = len_sensor1_sensor2; }

        // Определение направление бин поиска
        Coordinate helpbcpoint(m + step, cy);
        float help_len_scpoint_sensor2 = get_len(sensor1, cpoint) + get_len(cpoint, sensor2);
        if(help_len_scpoint_sensor2 > len_sensor1_sensor2) {maxx = m; }
        else {minx = m; }   
    } while (maxx - minx > step);
    return minans;
}

int main(float x1, float y1, float x2, float y2){
    // Small circle
    float scy = 104; // Ордината малой окружности
    float lsc = 384; // Длина малой окружности

    // Big circle
    float bcy = 0; // Ордината бОльшей окружности  
    float lbc = 510; // Длина бОльшей окружности
    
    Coordinate sensor1(x1, y1);
    Coordinate sensor2(x2, y2);
    float step = 0.1;

    // Решение проблемы разверстки
    if (abs(sensor2.x - sensor1.x) > lsc / 2){
        if (sensor1.x < sensor2.x) { sensor2.x = sensor1.x + lsc + sensor1.x - sensor2.x; } // sensor1.x < 0; sensor2.x > 0
        else{ sensor1.x = sensor2.x + lsc + sensor2.x - sensor1.x; } // sensor1.x > 0; sensor2.x < 0
    }
    float answer;
    if ((sensor1.y > scy && sensor2.y > scy) || (sensor1.y < bcy && sensor2.y < bcy) || (sensor1.y < scy && sensor1.y > bcy && sensor2.y < scy && sensor2.y > bcy)){ answer = get_len(sensor1, sensor2); }
    if (sensor1.y > scy && sensor2.y < bcy){ answer = HardCase(sensor1, sensor2, step, scy, bcy); }
    if (sensor1.y < bcy && sensor2.y > scy){ answer = HardCase(sensor1, sensor2, step, bcy, scy); }
    if ((sensor1.y < scy && sensor1.y > bcy && sensor2.y < bcy)  || (sensor2.y < scy && sensor2.y > bcy && sensor1.y < bcy)){ answer = MiddleCase(sensor1, sensor2, step, bcy); }
    if ((sensor1.y < scy && sensor1.y > bcy && sensor2.y > scy)  || (sensor2.y < scy && sensor2.y > bcy && sensor1.y > scy)){ answer = MiddleCase(sensor1, sensor2, step, scy); }
    cout << answer;
}