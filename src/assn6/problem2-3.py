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
    return times, positions, velocities

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
    # fig.savefig("RK4 Method Falling Object.png")
    plt.show()

'''
Runge-Kutta Method is a better version basically of Euler's Method.
 t takes four different approximations at each step, then makes the next step an average of the four approximations.

'''
def runge_kutta(inital_v, initial_y, step):
    curr_y = initial_y
    positions = [curr_y]
    times = [0]
    velocities = [inital_v]
    index = 0
    '''
    Naming Scheme: 
    vel_1 -> velocity approximation 1
    pos_1 -> position approximation 1
    '''
    while curr_y > 0:  # hasn't hit the ground yet

        pos_1 = falling_vel(velocities[index])
        vel_1 = falling_acc(velocities[index])

        pos_2 = falling_vel(velocities[index] + 0.5 * step * vel_1)
        vel_2 = falling_acc(velocities[index] + 0.5 * step * vel_1)

        pos_3 = falling_vel(velocities[index] + 0.5 * step * vel_2)
        vel_3 = falling_acc(velocities[index] + 0.5 * step * vel_2)

        pos_4 = falling_vel(velocities[index] + step * vel_3)
        vel_4 = falling_acc(velocities[index] + step * vel_3)

        velocities.append(velocities[index] + (vel_1 + 2*vel_2 + 2*vel_3 + vel_4) * step / 6)
        positions.append(positions[index] + (pos_1 + 2*pos_2 + 2*pos_3 + pos_4) * step / 6)
        times.append(index * step)
        curr_y = positions[index + 1]
        index += 1

    print(f"Object hit the ground at approximately {times[-1]} seconds")
    make_plot(times, positions, velocities, "Position/ Velocity Approximation using Runge-Kutta 4 Approximation")
    return times, positions, velocities


runge_kutta(0, 2000, .001)
# euler(0, 2000, 0.001)