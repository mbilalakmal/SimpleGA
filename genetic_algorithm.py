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

import numpy as np

from chromosome import Chromosome
from parameters import Parameters


class GeneticAlgorithm:

    def __init__(
        self,
        parameters: Parameters
    ):
        self._population = np.empty(
            shape=(parameters.population_size,),
            dtype=Chromosome
        )

        self.generation = 0
        self.optimum_reached = False
        self.best_fitness = 0.0
        self.best_chromosome = None
        self._parameters = parameters


    def run(self):
        '''
        Orchestrate the whole operation of genetic algorithm.


        (1) A population of chromosomes is initialized.

        (2) Fitness of each chromosome is evaluated.

        (3) Next generation is bred by performing crossover and mutation.

        (4) Stops when either optimum fitness is met or generations exceed the limit.
        '''
        self._initialize()

        while (
            self.best_fitness < 1.0 and
            self.generation < self._parameters.maximum_generations
        ):
            # create next generation by selective crossover and mutation
            self._reproduce()


    def describe(self):
        '''
        Describes current state of the algorithm.
        '''
        print(f'Generation: {self.generation}')
        print(f'Best Fitness: {self.best_fitness}')
        print(f'Best Chromosome: {self.best_chromosome}')
        print(f'Optimum reached: {self.optimum_reached}')


    def _initialize(self):
        '''
        `_population` is filled with randomly initialized chromosomes.

        Also sets `best_fitness` and `best_chromosome`.
        '''
        parameters = self._parameters

        for i in range(parameters.population_size):
            self._population[i] = Chromosome(parameters.genotype_length)
            self._population[i].initialize()

        self._track_best()


    def _reproduce(self):
        '''
        Create next generation from current population.

        Two chromsomes are selected and crossover'd to create new chromosomes.

        The new chromosomes undergo mutation with a probability `mutation_rate`.
        '''
        parameters = self._parameters

        # next generation
        population = np.empty_like(self._population)

        for i in range(parameters.population_size):
            # select parents
            parent1 = self._tournament_selection()
            parent2 = self._tournament_selection()

            while parent1 is parent2:
                # ensure distinct parents
                parent2 = self._tournament_selection()

            # create child
            offspring = Chromosome(parameters.genotype_length)

            # attempt crossover
            if np.random.binomial(1, parameters.crossover_rate):
                offspring.crossover(parent1, parent2)
            else:
                # copy one of the parents
                offspring.copy( np.random.choice([parent1, parent2]) )

            # attempt mutation
            if np.random.binomial(1, parameters.mutation_rate):
                offspring.mutate()

            population[i] = offspring

        self._population = population

        self._track_best()
        
        self.generation += 1


    def _tournament_selection(self, pressure: int=4):
        '''
        Perform tournament selection.

        `pressure` chromosomes are randomly sampled from the population
        and the chromosome with maximum fitness is returned.
        '''
        if pressure > self._parameters.population_size or pressure < 2:
            pressure = 2

        return np.amax(
            np.random.choice(self._population, size=(pressure,))
        )


    def _track_best(self):
        '''
        `best_fitness`: Maximum fitness in current population.

        `best_chromosome`: index of chromosome with `best_fitness`.
        '''
        self.best_chromosome = np.argmax(self._population)
        self.best_fitness = np.amax(self._population).fitness

        if self.best_fitness == 1.0:
            self.optimum_reached = True
