# -----------------------------------------------------------
# This module represents a parameters object for genetic algorithm.
#
# Parameters include:
# (1) genotype_length       (number of bits used for encoding)
# (2) population_size       (number of chromosomes in a single generation)
# (3) maximum_generations   (number of generations after which execution stops)
# (4) mutation_rate         (probability of a mutation occurring)
# (5) crossover_rate        (probability of a crossover occurring)
#
#
# (C) 2020 Muhammad Bilal Akmal, 17K-3669
# -----------------------------------------------------------

class Parameters:

    def __init__(
        self,
        genotype_length: int=8,
        population_size: int=8,
        maximum_generations: int=100,
        mutation_rate: float=0.05,
        crossover_rate: float=0.80
    ):
        self.genotype_length = max(genotype_length, 2)
        self.population_size = max(population_size, 2)
        self.maximum_generations = max(maximum_generations, 2)
        self.mutation_rate = max(mutation_rate, 0.00)
        self.crossover_rate = max(crossover_rate, 0.00)