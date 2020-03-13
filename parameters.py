class Parameters:

    def __init__(
        self,
        genotype_length: int=8,
        population_size: int=8,
        maximum_generations: int=10,
        mutation_rate: float=0.05,
        crossover_rate: float=0.80
    ):
        self.genotype_length = genotype_length
        self.population_size = population_size
        self.maximum_generations = maximum_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate