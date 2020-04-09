import numpy as np
import matplotlib.pyplot as plt
'''
y_x+1 = y_x + h * f(t_x, y_x)
'''
def euler(initial_v, initial_y, step, end):

    curr_y = initial_y
    positions = [curr_y]
    times = np.arange(0, end + step, step)
    velocities = [initial_v]
    for index in range(len(times)):
        velocities.append(velocities[index] + acc(velocities[index], positions[index]) * step)
        positions.append(positions[index] + velo(velocities[index]) * step)

    make_plot(times, positions[:-1], velocities[:-1], "Position/ Velocity Approximation using Euler's Method")
    return times, positions, velocities

'''
ODE representing the change in velocity of a 2nd order ODE system
dv/dt = -(cv +  kx) / m 
'''
def acc(v, x):
    m = 10  # mass
    k = 12  # spring constant
    c = 50  # damping
    return -(c*v + k*x) / m


'''
ODE representing the change in position of a 2nd order ODE system
dy/dt = v
'''
def velo(v):
    return v

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
    # fig.savefig("RK4 Method Spring System overdamped small step.png")
    plt.show()


'''
Runge-Kutta Method is a better version basically of Euler's Method.
 t takes four different approximations at each step, then makes the next step an average of the four approximations.

'''
def runge_kutta(initial_v, initial_y, step, end):
    positions = [initial_y]
    times = np.arange(0, end + step, step)
    velocities = [initial_v]
    '''
    Naming Scheme: 
    vel_1 -> velocity approximation 1
    pos_1 -> position approximation 1
    '''
    for index in range(len(times)):  # hasn't hit the ground yet

        pos_1 = velo(velocities[index])
        vel_1 = acc(velocities[index], positions[index])

        pos_2 = velo(velocities[index] + 0.5 * step * vel_1)
        vel_2 = acc(velocities[index] + 0.5 * step * vel_1, positions[index] + 0.5 * step * pos_1)

        pos_3 = velo(velocities[index] + 0.5 * step * vel_2)
        vel_3 = acc(velocities[index] + 0.5 * step * vel_2, positions[index] + 0.5 * step * pos_2)

        pos_4 = velo(velocities[index] + step * vel_3)
        vel_4 = acc(velocities[index] + step * vel_3, positions[index] + 0.5 * step * pos_3)

        velocities.append(velocities[index] + (vel_1 + 2*vel_2 + 2*vel_3 + vel_4) * step / 6)
        positions.append(positions[index] + (pos_1 + 2*pos_2 + 2*pos_3 + pos_4) * step / 6)

    make_plot(times, positions[:-1], velocities[:-1],
              "Position/ Velocity Approximation using Runge-Kutta 4 Approximation")
    return times, positions, velocities


runge_kutta(0, 1, .01, 15)
