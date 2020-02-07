import numpy as np
import random as rnd

def SA(f, p_init, bounds, t_init, t_red, rep_M, radii):
    '''
    ------------------------------
    SIMULATED ANNEALING ALGORITM
    ------------------------------
    --- Input ---
    f: (function) Objetive function
    p_init: (array) Initial point for the funtion to be first evaluated
    bounds: (list) Bounds on the search domain
    t_init: (float) Initial Temperature that will be reduced by each iteration
    t_red: (float) Value by which the temperature will be reducted by successive subtraction
    rep_M: (integer) Number of iterations executed at each temperature
    radii: (float) Neighboring radii to performed random sampling
    
    --- Output ---
    Optimum: (class) Results with:
        Optimum.f: (float) The best value of the funtion found in the optimization
        Optimum.x: (array) The best point in which the function was evaluated
        Optimum.traj_f: (array) Trajectory of function values
        Optimum.traj_x: (array) Trajectory of positions
        Optimum.traj_t: (array) Trajectory of temperatures
    '''
    # Initialize
    p_selected = p_init
    t          = t_init
    dim        = len(p_init)
    iteration  = 1
    
    traj_f  = np.ones(int(t_init/t_red))
    traj_x  = np.ones((int(t_init/t_red),dim))
    traj_t  = np.ones(int(t_init/t_red))
    
    # Neighbourhood
    radius     = np.array([bounds[i][1] - bounds[i][0] for i in range(dim)])/radii  
    new_bo     = np.array([[0, 0] for i in range(dim)])
    
    # Loop reducting t and trying rep_M times for each t
    cou = 0
    while t > 1e-8:
        traj_t[cou]  = t
        for m in range(rep_M):
            solution_selected = f(p_selected)
            
            # Consider only neighboring points of the current zone
            for j in range(dim):
                lo = p_selected[j] - radius[j]
                up = p_selected[j] + radius[j]
                if lo < bounds[j][0]:
                    lo = bounds[j][0]
                if up > bounds[j][1]:
                    up = bounds[j][1]
                new_bo[j] = [lo, up]
            p_alt = np.array([rnd.uniform(new_bo[i][0], new_bo[i][1]) for i in range(dim)])
            solution_alt      = f(p_alt)
            
            diff_f            = solution_alt - solution_selected
            
            if diff_f <= 0:
                p_selected    = p_alt
            else:
                probability   = np.exp(- diff_f /t)
                if probability > rnd.random():
                    p_selected = p_alt            
            iteration += 1
        
        traj_f[cou] = solution_selected
        traj_x[cou] = p_selected
        cou += 1
        t -= t_red
    
    traj_f = traj_f[:int(t_init/t_red)]
    traj_x = traj_x[:int(t_init/t_red)]
    traj_t = traj_t[:int(t_init/t_red)]
    
    # Gather results
    class Optimum:
        pass
    Optimum.f         = solution_selected
    Optimum.x         = p_selected
    Optimum.traj_f    = traj_f
    Optimum.traj_x    = traj_x
    Optimum.traj_t    = traj_t
    
    return Optimum
