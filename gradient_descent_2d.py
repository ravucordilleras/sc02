# https://www.youtube.com/watch?v=gsfbWn4Gy5Q
import numpy as np
import matplotlib.pyplot as plt

scenario = 8        # 1 - 3

def y_function(x):
        if scenario == 1 or scenario == 2:
            return x ** 2
        elif scenario == 3 or scenario == 4 or scenario == 5 or scenario == 6:
            return np.sin(x)
        elif scenario == 7 or scenario == 8:
            return 1 / (x ** 3)
        elif scenario == 9 or scenario == 10:
            return np.cos(x)

def y_derivative(x):
    if scenario == 1 or scenario == 2:
        return 2 * x
    elif scenario == 3 or scenario == 4 or scenario == 5 or scenario == 6:
        return np.cos(x)
    elif scenario == 7 or scenario == 8:
        return -3 / (x ** 4)
    elif scenario == 9 or scenario == 10:
        return -(np.sin(x))

def range_fufu():
    if scenario == 1 or scenario == 2:
        return 100
    elif scenario == 3 or scenario == 4 or scenario == 5 or scenario == 6:
        return 5
    elif scenario == 7 or scenario == 8:
        return 0.5
    elif scenario == 9 or scenario == 10:
        return 6
    
def starting_pos():
    if scenario == 1 or scenario == 2:
        return 80
    elif scenario == 3 or scenario == 5:
        return 3
    elif scenario == 4 or scenario == 6:
        return 3
    elif scenario == 7 or scenario == 8:
        return 1.5
    elif scenario == 9 or scenario == 10:
        return 1.5
    
def learning_rate():
    if scenario == 1 or scenario == 7 or scenario == 9:
        return 0.01
    elif scenario == 2 or scenario == 8 or scenario == 10:
        return -0.01
    elif scenario == 3 or scenario == 5:
        return 0.1
    elif scenario == 4 or scenario == 6:
        return -0.1

step_size = 0.1
x = np.arange(-range_fufu(), range_fufu(), step_size)
y = y_function(x)

current_pos = (starting_pos(), y_function(starting_pos()))

for _ in range(1000):
    new_x = current_pos[0] - learning_rate() * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(0.001)
    plt.clf()
    print(_)