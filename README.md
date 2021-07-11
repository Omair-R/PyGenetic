# PyGenetic
PyGenetic is a small project that I created to develop a better understanding of genetic algorithms, after all you can't code something you don't understand. I wanted to stop at the most basic implementation for the algorithm, but I grew to love it, and decided to explore further. The project is still greatly under developement with many features remine unfinished, some of which are: 
- String, and binary arrays handling. 
- more crossover methods. 
- error handling and testing (I should have done them earlier I know XD)
- visualization. 
- ... and lot more that I might get to later. 

### usage: 
the project is not a pip package, and I am not sure if it ever will be, but you can simply clone the repository. then do something similar to: 

``` python
import numpy as np
from PyGenetic import genetic_algorithms as pg

function_inputs = [4, -2, 3.5, 0.5, -10, -4.7]

desired_output = 69


def fitness_func(solution):

    output = np.sum(solution * function_inputs)
    fitness = 1.0 / (np.abs(output - desired_output) + 0.000000001)

    return fitness


ga = pg.GA(fitness_function=fitness_func,
           n_generations=100,
           n_genes=6,
           n_pool=100,
           n_parents=25,
           low_boundery=-2,
           high_boundery=5,
           mutation_prop=0.6,
           crossover_type="uniform",
           mutation_type = "swap")

solution, fitness = ga.run(verbose=True)

output = np.sum(solution * function_inputs)

print(
    f"best parent is: {solution}\nwith fitness score of {fitness} \nsolution: {output}"
)
```

### requirements:
pretty much just numpy, I am using numpy==1.18.5
