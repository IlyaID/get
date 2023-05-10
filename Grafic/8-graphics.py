from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker



file = open('data.txt', 'r')
file = open('settings.txt', 'r')

with open('settings.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

#считываем показания компаратора и переводим через шаг квантования в вольиты
data=numpy.loadtxt('data.txt', dtype=int) * settings[1]
#data=numpy.loadtxt('data.txt', dtype=int)

#массив времен, создаваемый черед количество измерений и известный шаг по времени
data_time=numpy.array([i*settings[0] for i in range(data.size)])

#устанавливаем размеры окна графика и разрешение
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#устанавливае минимальные и максимальные значения для осей
ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

#  Устанавливаем шаг основных делений на оси "х":
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

#  Устанавливаем шаг промежуточных делений на оси "х":
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Устанавливаем шаг основных делений на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

#  Устанавливаем шаг промежуточных делений на оси"y":
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#задаём название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепи', 60)), loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')



#подпись осей
ax.set_ylabel("Напряжение U, В")
ax.set_xlabel("Время t, с")

#линия с легендой

ax.plot(data_time, data, color='black', linewidth=2, label = '$U_C(t)$', marker='o', markerfacecolor='green', linestyle='-',
    markersize=5, markevery = 10)

textstr = '\n'.join((
    r'Время зарядки t_{зарядки} = 5.21 c',
    r'Время разрядки t_{разрядки} = 6.79 c' ))


ax.text(0.55, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')


ax.legend(shadow = False, loc = 'right', fontsize = 20)

#сохранение
fig.savefig('graph.png')
fig.savefig('graph.svg')
