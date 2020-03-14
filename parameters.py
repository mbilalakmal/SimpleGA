# -----------------------------------------------------------
# This module represents a parameters object for genetic algorithm.
#
# Parameters include:
# (1) genotype_length
# (2) population_size
# (3) maximum_generations
# (4) mutation_rate
# (5) crossover_rate
#
#
# (C) 2020 Muhammad Bilal Akmal, 17K-3669
# -----------------------------------------------------------

class Parameters:

    def __init__(
        self,
        genotype_length: int=8,
        population_size: int=8,
        maximum_generations: int=10,
        mutation_rate: float=0.05,
        crossover_rate: float=0.80
    ):
        self.genotype_length = max(genotype_length, 2)
        self.population_size = max(population_size, 4)
        self.maximum_generations = max(maximum_generations, 2)
        self.mutation_rate = max(mutation_rate, 0.01)
        self.crossover_rate = max(crossover_rate, 0.00)
