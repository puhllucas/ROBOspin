import random
import time
import datetime

# random values
temperature_limit = (100, 300)  
speed_limit = (1000, 2000)
pressure_limit = (50, 150)
vibration_limit = (0, 10)

sample = 10
cnt = 0

while cnt < sample:
    cnt += 1

    temperature = random.uniform(temperature_limit[0], temperature_limit[1])
    speed = random.uniform(speed_limit[0], speed_limit[1])
    pressure = random.uniform(pressure_limit[0], pressure_limit[1])
    vibration = random.uniform(vibration_limit[0], vibration_limit[1])

    data = datetime.datetime.today()
    data_str = data.strftime("%d/%m/%y %H:%M:%S")
    
    data = "({} - Temperature: {:.2f}C - Speed: {:.2f} RPM - Pressure {:.2f} psi - Vibration: {:.2f} ms/s2)".format(data_str ,temperature, speed, pressure, vibration)
    
    with open('data/test.txt', 'a', encoding="utf-8") as f:
        f.write(data+'\n')
    
    time.sleep(1)
