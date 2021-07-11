import abc
from typing import Tuple
import numpy as np

from PyGenetic.crossover import CrossoverDecidor
from PyGenetic.mutation import MutationDecidor

class AbstractPopulation(abc.ABC):

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

    @abc.abstractclassmethod
    def parent_selection(self):
        return NotImplementedError

    @abc.abstractclassmethod
    def breed_childern(self):
        return NotImplementedError

