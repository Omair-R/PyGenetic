import numpy as np

from PyGenetic.factory import FactoryPopulation


def population_decidor(n_genes, n_pool, n_parents, low_boundery, high_boundery,
                       mutation_prop, crossover_type, mutation_type,
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
                                low_boundery=0,
                                high_boundery=0,
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


class BinaryPopulation(FactoryPopulation):
    def __init__(self, n_genes: int, n_pool: int, n_parents: int,
                 mutation_prop: float, crossover_type: str, mutation_type: str,
                 low_boundery: int, high_boundery: int) -> None:

        self.n_genes = n_genes
        self.n_pool = n_pool
        self.n_parents = n_parents
        self.low_boundery = low_boundery
        self.high_boundery = high_boundery
        self.mutation_propability = mutation_prop
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type

        super().__init__()

        self.pool = np.random.randint(0,
                                      2, (self.n_pool, self.n_genes),
                                      dtype=bool)


class StringPopulation(FactoryPopulation):
    pass


class OptimizationPopulation(FactoryPopulation):
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

        super().__init__()

        self.pool = np.random.uniform(self.low_boundery, self.high_boundery,
                                      (self.n_pool, self.n_genes))
