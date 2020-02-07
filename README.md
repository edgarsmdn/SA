# Simulated Annealing

<p align="center">
<img src="https://github.com/edgarsmdn/SA/blob/master/SA_1.gif" width="500"> 
</p>

## Development

This work was part of the project I did during my undergrad research internship in the summer of 2018 at the [Centre for Process Integration](https://www.ceas.manchester.ac.uk/cpi/), The University of Manchester on stochastic optimization.

## Background

Simulated Annealing (SA) is inspired by the physical process performed on metals or glass called annealing. This is a heat treatment in which the solid is heated up at high temperatures and then cool down very slowly. This process causes the internal solid configuration to be rearranged and to reach its minimum lattice energy state (Jacobson, 2010). This algorithm is usually used to address discrete optimization problems; however, its use for continuous problems is also possible.

The general idea behind SA is to store the "best" visited point at each iteration. However, instead of always taking the actual best point found from iteration to iteration, some worse points are accepted according to the probability given by:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%3D%20%5Cexp%20%5Cleft%28%20-%20%5Cfrac%7B%5CDelta%20w%7D%7BT%7D%20%5Cright%29"> 
</p>

where ![eq](https://latex.codecogs.com/gif.latex?P) stands for the probability of accepting a worse point; ![eq](https://latex.codecogs.com/gif.latex?%5CDelta%20w) is the difference between the proposed point with the current best point and ![eq](https://latex.codecogs.com/gif.latex?T) is the temperature that is reduce from iteration to iteration.

The reason for accepting "worse" steps (with less fitness than the current "best" point) is to escape from local minima; otherwise, if only the fitter points are accepted, the algorithm will be easily stuck in a local optimum. The proposed point to move to is chosen randomly in the neighborhood of the current point. As can be seen in the previous equation, the probability is dependent on the temperature, which is progressively reduced. In this way, as the iterations progress, the probability of accepting worse points decreases.

## Prerequisites

The function requires Python 3.0 (or more recent versions).

## Functioning

#### Inputs

```
SA(f, p_init, bounds, t_init, t_red, rep_M, radii)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. The **function** to be optimized. The functions needs to be of the form ![equation](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5En%20%5Crightarrow%20%5Cmathbb%7BR%7D).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. The **initial location** of the first point for the first iteration.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. The **bounds** for each dimension of the fucntion. This has to be a list of the form `[(lb1, ub1), (1b2, ub2), ...]`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. The **initial temperature** which is going to be reduced to zero by succesive substraction of ` t_red`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. The **temperature reduction** applied at each iteration, with the form ![eq](https://latex.codecogs.com/gif.latex?T%5E%7Bt-1%7D%20%3D%20T%5Et%20-%20T_%7Bred%7D).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6. The number of random **proposed locations** at each temperature value.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7. The **radius parameter** used to define the neighborhood of the current best point. This value divides the total extension of the bounds. For instance, if the distance between the lower bound and upper bound is 10, and the `radii` is set to 2, the neightborhood will be defined with a distance of 5 from the current point.

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

* In this version, the neighborhood of the current best point is always restricted to remain within the bounds provided by the user.

* The stopping criterion in this version is the temperature value reaching zero.


### References

Jacobson, A. G. (2010). Simulated Annealing. In J. Y. M. Gendreau, Handbook of Metaheuristics (pp. 1 - 39). Buffalo: International Series in Operations Research & Management Sciences.
