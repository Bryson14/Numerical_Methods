import numpy as np
import matplotlib.pyplot as plt
'''
y_x+1 = y_x + h * f(t_x, y_x)
'''
def euler(inital_v, initial_y, step):

    curr_y = initial_y
    positions = [curr_y]
    times = [0]
    velocities = [inital_v]
    index = 0
    while curr_y > 0:  # hasn't hit the ground yet
        if index % (1/step) == 0:
            print(index)

        velocities.append(velocities[index] + falling_acc(velocities[index]) * step)
        positions.append(positions[index] + falling_vel(velocities[index]) * step)
        times.append(index * step)
        curr_y = positions[index + 1]
        index += 1

    print(f"Object hit the ground at approximately {times[-1]} seconds")
    make_plot(times, positions, velocities, "Position/ Velocity Approximation using Euler's Method")

'''
ODE representing the downward acceleration of a falling object.
Positive return value means the object is accelerating downward.
This is representing the air drag that is proportional to the velocity squared
This means that at +-62.64 m/s, the air drag and gravity equal, reaching terminal velocity
dv/dt = 9.81-0.0025v^2
'''
def falling_acc(v):
    return 9.81 - 0.0025 * np.power(v, 2)


'''
ODE representing the downward velocity of a falling object
dy/dt = -v
'''
def falling_vel(v):
    return -v

'''
Produces the plot with two y axis. Convenient for plotting without duplicating data
'''
def make_plot(time, position, velocity, title):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Position (m)', color=color)
    ax1.plot(time, position, label="Position", color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Velocity (m/s)', color=color)  # we already handled the x-label with ax1
    ax2.plot(time, velocity, label="Velocity", color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.set_title(title)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

euler(0, 2000, .0001)