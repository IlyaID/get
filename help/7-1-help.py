import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)

LEDS=[21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(LEDS, GPIO.OUT)

DAC=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(DAC, GPIO.OUT, initial=GPIO.HIGH)

comparator=4
troyka=17 
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

#снятие показаний с тройки
def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(DAC, perev(k))
        time.sleep(0.005)
        if GPIO.input(comparator)==0:
            k-=2**i
    return k

#перевод в двоичную
def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    voltage=0
    result_of_experement=[]
    time_start=time.time()
    counter=0

    #зарядка конденсатора, запис показаний в процессе
    print('начало зарядки конденсатора')
    while voltage<256*0.25:
        voltage=adc()
        result_of_experement.append(voltage)
        time.sleep(0)
        counter+=1
        GPIO.output(LEDS, perev(voltage))

    GPIO.setup(troyka,GPIO.OUT, initial=GPIO.LOW)

    #разрядка конденсатора, запис показаний в процессе
    print('начало разрядки конденсатора')
    while voltage>256*0.02:
        voltage=adc()
        result_of_experement.append(voltage)
        time.sleep(0)
        counter+=1
        GPIO.output(LEDS, perev(voltage))

    time_experiment=time.time()-time_start

    #запись данных в файлы
    print('запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in result_of_experement:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/counter) + '\n')
        f.write('0.01289')
    
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/counter, 1/time_experiment/counter, 0.013))

    #графики
    print('построение графиков')
    y=[i/256*3.3 for i in result_of_experement]
    x=[i*time_experiment/counter for i in range(len(result_of_experement))]
    pyplot.plot(x, y)
    pyplot.xlabel('время')
    pyplot.ylabel('вольтаж')
    pyplot.show()

finally:
    GPIO.output(LEDS, 0)
    GPIO.output(DAC, 0)
    GPIO.cleanup()