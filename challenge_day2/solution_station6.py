import matplotlib.pyplot as plt
import math

z = [ 0.4, 
     0.8,
    1.6,
    1.7,
    2.4,
    2.8,
    2.9,
    0,
    2]

y = [0.3894,
    0.7174,
    0.9996,
    0.9917,
    0.6755,
    0.335, 
    0.2392,
    0,
    0.9093]

plt.plot(z, y, '.')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('plotting x on y')
plt.show()


def solution_station_6(x):
    return math.sin(x)
