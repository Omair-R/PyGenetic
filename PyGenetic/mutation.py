import numpy as np

from PyGenetic.abstracts import *

class MutationDecidor(AbstractedDecidor):
    def __init__(self, mutation_type, n_genes, mutation_propability,
                 low_boundery, high_boundery):

        self.mutation_type = mutation_type
        self.n_genes = n_genes
        self.mutation_propability = mutation_propability
        self.low_boundery = low_boundery
        self.high_boundery = high_boundery

    def run(self, chromosome: np.array) -> None:
        if self.mutation_type == "random_resetting":
            self.random_resetting(chromosome)

        elif self.mutation_type == "swap":
            self.swap(chromosome)

        elif self.mutation_type == "bit_flip":
            self.bit_flip(chromosome)

    def random_resetting(self, chromosome: np.array) -> None:

        if self.chance_gen():
            mutation_point = np.random.choice(range(self.n_genes))
            chromosome[mutation_point] = np.random.uniform(
                self.low_boundery, self.high_boundery)

    def swap(self, chromosome: np.array) -> None:

        if self.chance_gen():
            mutation_points = np.random.choice(range(self.n_genes),
                                               size=2,
                                               replace=False)

            chromosome[mutation_points[0]], chromosome[
                mutation_points[1]] = chromosome[
                    mutation_points[1]], chromosome[mutation_points[0]]

    def bit_flip(self, chromosome: np.array) -> None:

        if self.chance_gen():
            mutation_point = np.random.choice(range(self.n_genes))
            chromosome[
                mutation_point] = 0 if chromosome[mutation_point] == 1 else 1

    def chance_gen(self) -> bool:

        chance = np.random.uniform(0, 1)
        return True if self.mutation_propability > chance else False

