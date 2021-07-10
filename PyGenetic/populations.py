from typing import Tuple
import numpy as np

from crossover import *
from mutation import *
from abstracts import *

def population_decidor(n_genes,
                        n_pool,
                        n_parents,
                        low_boundery,
                        high_boundery,
                        mutation_prop,
                        crossover_type,
                        mutation_type,
                        population_type):

    if population_type == "optimization":

        return OptimizationPopulation(n_genes=n_genes,
                                                 n_pool=n_pool,
                                                 n_parents=n_parents,
                                                 low_boundery=low_boundery,
                                                 high_boundery=high_boundery,
                                                 mutation_prop=mutation_prop,
                                                 crossover_type=crossover_type,
                                                 mutation_type=mutation_type)

    elif population_type == "binary":
        return BinaryPopulation(n_genes=n_genes,
                                                 n_pool=n_pool,
                                                 n_parents=n_parents,
                                                 low_boundery=low_boundery,
                                                 high_boundery=high_boundery,
                                                 mutation_prop=mutation_prop,
                                                 crossover_type=crossover_type,
                                                 mutation_type=mutation_type)

    elif population_type == "string":
        return StringPopulation(n_genes=n_genes,
                                                 n_pool=n_pool,
                                                 n_parents=n_parents,
                                                 low_boundery=low_boundery,
                                                 high_boundery=high_boundery,
                                                 mutation_prop=mutation_prop,
                                                 crossover_type=crossover_type,
                                                 mutation_type=mutation_type)


class BinaryPopulation(AbstractPopulation):
    pass


class StringPopulation(AbstractPopulation):
    pass


class OptimizationPopulation(AbstractPopulation):
    def __init__(self, n_genes: int, n_pool: int, n_parents: int,
                 low_boundery: int, high_boundery: int, mutation_prop: float,
                 crossover_type: str, mutation_type: str) -> None:

        self.n_genes = n_genes
        self.n_pool = n_pool
        self.n_parents = n_parents
        self.low_boundery = low_boundery
        self.high_boundery = high_boundery
        self.mutation_propability = mutation_prop
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type

        self.crossover_decidor = CrossoverDecidor(self.crossover_type,
                                                  self.n_genes)

        self.mutation_decidor = MutationDecidor(self.mutation_type,
                                                self.n_genes,
                                                self.mutation_propability,
                                                self.low_boundery,
                                                self.high_boundery)
                                                
        self.pool = np.random.uniform(self.low_boundery, self.high_boundery,
                                      (self.n_pool, self.n_genes))
        


    def crossover(self, first_chromo: np.array,
                  second_chromo: np.array) -> Tuple[np.array, np.array]:

        first_child, second_child = self.crossover_decidor.run(
            first_chromo, second_chromo)

        return (first_child, second_child)

    def mutation(self, chromosome: np.array) -> np.array:

        self.mutation_decidor.run(chromosome)
        

    def parent_selection(self, fitness: np.array) -> None:

        fit_idx = np.argsort(fitness)[::-1]

        self.parents = self.pool[fit_idx[:self.n_parents]]

    def breed_childern(self) -> None:

        for i in range(self.n_pool // 2):
            first_chromo = self.parents[np.random.choice(range(
                self.n_parents))]
            second_chromo = self.parents[np.random.choice(range(
                self.n_parents))]

            first_child, second_child = self.crossover(first_chromo,
                                                       second_chromo)

            self.mutation(first_child)
            self.mutation(second_child)

            self.pool[i:i + 2] = [first_child, second_child]

        self.pool[-1] = self.parents[0]
