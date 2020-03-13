# -----------------------------------------------------------
# This module represents an N-bit string Chromosome.
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

import random

import numpy as np

from functools import total_ordering

@total_ordering
class Chromosome:

    def __init__(self, length: int=8):
        '''
        `length`: Length of binary string. Default is 8.
        '''
        self._genotype = np.empty(shape=(length,), dtype=bool)
        self.length = length
        self.fitness = 0.0


    def initialize(self):
        '''
        Fill genotype with a random sequence of `True`s and `False`s.
        '''
        self._genotype = np.random.choice(
            a=[True, False], size=(self.length,)
        )

        self._calculate_fitness()

    
    def mutate(self, size: int=1):
        '''
        Flip `size` genes by inverting them.

        If `size` is not given or greater than length, 1 is used.
        '''
        if size > self.length or size < 1:
            size = 1

        # select target genes to invert
        target_genes = random.sample(range(self.length), size)

        for gene in target_genes:
            self._genotype[gene] = not self._genotype[gene]

        self._calculate_fitness()


    def crossover(
        self,
        parent1: 'Chromosome',
        parent2: 'Chromosome'
    ):
        '''
        Perform uniform crossover using genotypes of `parent1` and `parent2`.
        '''
        for gene in range(self.length):
            # for each gene copy from a random parent
            self._genotype[gene] = random.choice(
                [parent1._genotype[gene], parent2._genotype[gene]]
            )

        self._calculate_fitness()


    def copy(self, parent: 'Chromosome'):
        '''
        Copy genotype from a single chromosome.
        '''
        self._genotype = np.copy(parent._genotype)
        self.fitness = parent.fitness


    def _calculate_fitness(self):
        '''
        Counts the number of `True`s and divides by length.
        '''
        score = np.count_nonzero(self._genotype)
        fitness = score/self.length
        self.fitness = fitness

    
    def __gt__(self, other: 'Chromsome'):
        return self.fitness > other.fitness


    def __eq__(self, other: 'Chromosome'):
        return self.fitness == other.fitness