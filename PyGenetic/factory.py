from typing import Tuple
import numpy as np

from PyGenetic.crossover import CrossoverDecidor
from PyGenetic.mutation import MutationDecidor


class FactoryPopulation():
    def __init__(self):
        self.crossover_decidor = CrossoverDecidor(self.crossover_type,
                                                  self.n_genes)

        self.mutation_decidor = MutationDecidor(self.mutation_type,
                                                self.n_genes,
                                                self.mutation_propability,
                                                self.low_boundery,
                                                self.high_boundery)

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
