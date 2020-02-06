# Simulated Annealing

<p align="center">
<img src="https://github.com/edgarsmdn/SA/blob/master/SA.gif" width="500"> 
</p>

## Development

This work was part of the project I did during my undergrad research internship in the summer of 2018 at the [Centre for Process Integration](https://www.ceas.manchester.ac.uk/cpi/), The University of Manchester on stochastic optimization.

## Background

 

## Prerequisites

The function requires Python 3.0 (or more recent versions).

## Functioning

#### Inputs

```
SA(f, p_init, bounds, t_init, t_red, rep_M, radii)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. The **function** to be optimized. The functions needs should be of the form ![equation](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5En%20%5Crightarrow%20%5Cmathbb%7BR%7D).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. The **number of particles**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. The **bounds** for each dimension of the fucntion. This has to be a list of the form `[(lb1, ub1), (1b2, ub2), ...]`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. The **maximum number of iterations** which is the stopping criteria in this implementation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. The **cognition** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6. The **social-confidence** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7. The **inertia weight** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8. The **reduction parameter** ![equation](https://latex.codecogs.com/gif.latex?w_%7Bred%7D). This reduces the inertia weight at each iteration following: ![equation](https://latex.codecogs.com/gif.latex?w%5E%7Bt&plus;1%7D%3D%20w_%7Bred%7D%20%7E%20w%5Et) 

#### Outputs

```
Optimum: (class) Results with:
        Optimum.f: (float) The best value of the funtion found in the optimization
        Optimum.x: (array) The best point in which the function was evaluated
        Optimum.traj_f: (array) Trajectory of function values
        Optimum.traj_x: (array) Trajectory of positions
        Optimum.traj_t: (array) Trajectory of temperatures
```

#### General information



### References
