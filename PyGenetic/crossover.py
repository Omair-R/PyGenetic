from typing import Tuple
import numpy as np


class CrossoverDecidor:
    def __init__(self, crossover_type, n_gene):
        self.n_gene = n_gene
        self.crossover_types_dict: dict = {
            "single_point": self.single_point,
            "double_point": self.double_point,
            "uniform": self.uniform,
            "order": self.order,
            "cycle": self.cycle,
            "Simulated_binary": self.Simulated_binary,
        }
        self.crossover_function = self.crossover_types_dict[crossover_type]

    def run(self, first_chromo: np.array,
            second_chromo: np.array) -> Tuple[np.array, np.array]:
        return self.crossover_function(first_chromo, second_chromo)

    def single_point(self, first_chromo: np.array,
                     second_chromo: np.array) -> Tuple[np.array, np.array]:

        cross_point = np.random.choice(range(self.n_gene))

        first_child = np.hstack(
            (first_chromo[:cross_point], second_chromo[cross_point:]))
        second_child = np.hstack(
            (second_chromo[:cross_point], first_chromo[cross_point:]))

        return (first_child, second_child)

    def double_point(self, first_chromo: np.array,
                     second_chromo: np.array) -> Tuple[np.array, np.array]:

        first_cp = np.random.choice(range(self.n_gene - 1))
        second_cp = np.random.choice(range(first_cp, self.n_gene + 1))

        first_child = np.hstack(
            (first_chromo[:first_cp], second_chromo[first_cp:second_cp],
             first_chromo[second_cp:]))

        second_child = np.hstack(
            (second_chromo[:first_cp], first_chromo[first_cp:second_cp],
             second_chromo[second_cp:]))

        return (first_child, second_child)

    def uniform(self, first_chromo: np.array,
                second_chromo: np.array) -> Tuple[np.array, np.array]:

        first_child = first_chromo.copy()
        second_child = second_chromo.copy()

        mask = np.random.randint(0, 2, self.n_gene, dtype=bool)

        first_child[mask], second_child[mask] = second_child[
            mask], first_child[mask]

        return (first_child, second_child)

    def order(self, first_chromo: np.array,
              second_chromo: np.array) -> Tuple[np.array, np.array]:
        """ under_construction """
        pass

    def partially_mapped(self, first_chromo: np.array,
                         second_chromo: np.array) -> Tuple[np.array, np.array]:
        """ under_construction """
        pass

    def cycle(self, first_chromo: np.array,
              second_chromo: np.array) -> Tuple[np.array, np.array]:
        """ under_construction """
        pass

    def Simulated_binary(self, first_chromo: np.array,
                         second_chromo: np.array) -> Tuple[np.array, np.array]:
        """ under_construction """
        pass
