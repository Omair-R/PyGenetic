import numpy as np

from PyGenetic.populations import *
from PyGenetic.utils import *

class GA:
    """
    This is the main class in the project, upon use, you can define an 
    instance of this class, provide the desired parameters, then use
    the method .run() to run the algorithm. It's as simple as that. 

    This project was mainly done for practice purposes, and to insure 
    that I truely understand how genetic algorithms work. However, it
    might still be of use to many people. 
    
    """
    def __init__(self,
                 fitness_function,
                 n_generations: int = 50,
                 n_genes: int = 6,
                 n_pool: int = 100,
                 n_parents: int = 25,
                 low_boundery: int = -2,
                 high_boundery: int = 5,
                 mutation_prop: float = 0.3,
                 crossover_type: str = "single_point",
                 mutation_type: str = "random_resetting") -> None:

        self.n_gnerations = n_generations
        self.fitness_function = fitness_function

        self.population = population_decidor(n_genes=n_genes,
                                                 n_pool=n_pool,
                                                 n_parents=n_parents,
                                                 low_boundery=low_boundery,
                                                 high_boundery=high_boundery,
                                                 mutation_prop=mutation_prop,
                                                 crossover_type=crossover_type,
                                                 mutation_type=mutation_type,
                                                 population_type="optimization")

    def fitness_computation(self) -> None:

        self.pool_fitness = np.empty(self.population.n_pool)

        for i in range(self.population.n_pool):

            fitness = self.fitness_function(self.population.pool[i])
            self.pool_fitness[i] = fitness


    def run(self, verbose: bool = True) -> None:

        self.fitness_computation()
        self.population.parent_selection(self.pool_fitness)

        for i in range(self.n_gnerations):

            self.population.breed_childern()
            self.fitness_computation()
            self.population.parent_selection(self.pool_fitness)

            if verbose:
                update_progress_bar(i, self.n_gnerations)

        print("")
        self.best_chromosome = self.population.parents[0]

        return self.best_chromosome, np.max(self.pool_fitness)


if __name__ == "__main__":
        
    function_inputs = [4, -2, 3.5, 0.5, -10, -4.7]
    
    desired_output = 69


    def fitness_func(solution):

        output = np.sum(solution * function_inputs)
        fitness = 1.0 / (np.abs(output - desired_output) + 0.000000001)

        return fitness


    ga = GA(fitness_function=fitness_func, crossover_type="uniform")

    solution, fitness = ga.run(verbose=True)

    output = np.sum(solution * function_inputs)

    print(
        f"best parent is: {solution}\nwith fitness score of {fitness} \nsolution: {output}"
    )




