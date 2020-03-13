# -----------------------------------------------------------
# This module represents a GeneticAlgorithm.
#
# A Chromosome can be:
# (1) initialized randomly,
# (2) mutated,
# (3) initialized by performing crossover,
# (4) fitness calculated
#
#
# (C) 2020 Muhammad Bilal Akmal, 17K-3669
# -----------------------------------------------------------

from chromosome import Chromosome

from parameters import Parameters

import numpy as np

class GeneticAlgorithm:

    def __init__(
        self,
        parameters: Parameters
    ):
        self._parameters = parameters

        self._population = np.empty(
            shape=(parameters.population_size,),
            dtype=Chromosome
        )

        self.generation = 0

        self.best_fitness = 0.0

        self.best_chromosome = None
    

    def initialize(self):
        
        parameters = self._parameters

        for i in range(parameters.population_size):
            self._population[i] = Chromosome(parameters.genotype_length)
            self._population[i].initialize()

        self._track_best()


    def reproduce(self):
        population = np.empty_like(self._population)

        parameters = self._parameters

        for i in range(self._parameters.population_size):
            # select parents
            parent1 = self._tournament_selection()
            parent2 = self._tournament_selection()

            while parent1 is parent2:
                print('OHSNAP')
                parent2 = self._tournament_selection()

            # create child
            offspring = Chromosome(parameters.genotype_length)

            # try crossover
            if np.random.binomial(1, parameters.crossover_rate):

                offspring.crossover(parent1, parent2)
            else:
                offspring.copy(
                    np.random.choice([parent1, parent2])
                )

            # try mutation
            if np.random.binomial(1, parameters.mutation_rate):
                offspring.mutate()

            population[i] = offspring

        self._population = population


    def _tournament_selection(self, pressure: int=4):
        # tournament selection
        if pressure > self._parameters.population_size or pressure < 2:
            pressure = 2

        return np.amax(
            np.random.choice(self._population, size=(pressure,))
        )

    
    def _track_best(self):
        self.best_chromosome = np.argmax(self._population)
        self.best_fitness = np.amax(self._population).fitness


para = Parameters()

ga = GeneticAlgorithm(para)
print(ga.best_chromosome)

ga.initialize()

print(ga.best_fitness)
print(ga.best_chromosome)
for chr in ga._population:
    print(chr.fitness)
    print(chr._genotype)

ga.reproduce()