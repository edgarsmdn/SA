import numpy as np
import random as rnd
from SA import SA
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

'''

                              Example of SA 

'''

def alpine1(variables):
    '''
    Alpine 1 function
    Minimum at 0 at x = [zeros]
    Usually domain of evaluation is [-10, 10]
    Source: http://infinity77.net/global_optimization/test_functions_nd_A.html#n-d-test-functions-a
    Retrieved: 19/06/2018
    '''
    return np.sum(np.abs(np.multiply(variables, np.sin(variables)) + 0.1 * variables))


f = alpine1
b = (-10, 10)

# Defines parameters
bounds=[b for i in range(2)] 
t_init = 5
t_red = 0.1
rep_M = 5
radii = 8

# Assigns random initial position between the given bounds
p_init = np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(len(bounds))])

# Optimize
results = SA(f, p_init, bounds, t_init, t_red, rep_M, radii)


# Plot Optimization
points             = np.zeros(1, dtype=[("position", float, 2)])
points["position"] = results.traj_x[0]

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.15, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 
start, stop, n_values = b[0], b[1], 100

x       = np.linspace(start, stop, n_values)
y       = np.linspace(start, stop, n_values)
X, Y    = np.meshgrid(x, y)

zs = np.array([f(np.array([x,y])) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z  = zs.reshape(X.shape)

cm = plt.contourf(X, Y, Z, cmap='Blues')
plt.colorbar(cm)
ax.set_title('Alpine 1 function, Temperature: ' + str(results.traj_t[0]))
ax.set_xlabel('x')
ax.set_ylabel('y')

scatter = ax.scatter(points["position"][:,0], points["position"][:,1], c='red', s=50)

xs = results.traj_x
ts = results.traj_t

def update(frame_number):
    points["position"] = xs[frame_number]
    scatter.set_offsets(points["position"])
    ax.set_title('Alpine 1 function, Temperature: ' + str(round(ts[frame_number],2)))
    return scatter, 

anim = FuncAnimation(fig, update, interval=10, frames=range(len(xs)), repeat_delay=2000)
plt.show()

# Save gif
anim.save('SA.gif', writer='imagemagick', fps=400)
