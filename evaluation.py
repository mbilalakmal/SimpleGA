import time

import matplotlib.pyplot as plt
import numpy as np

from genetic_algorithm import GeneticAlgorithm
from parameters import Parameters


def _run_trials(parameters: Parameters, trials: int):
    results = np.empty(shape=(trials,), dtype=bool)

    ga = GeneticAlgorithm(parameters)
    start_time = time.time()
    for i in range(trials):
        results[i] = ga.run()

    finish_time = time.time()

    average_time = (finish_time-start_time) / trials
    success_rate = np.count_nonzero(results) / trials

    return (average_time, success_rate)


def evaluate_chromosome_length(
    start, stop, step, population_size, maximum_generations, trials):

    chromosome_lengths  = []
    completion_times    = []
    success_rates       = []

    for i in range(start, stop, step):
        parameters = Parameters(i, population_size, maximum_generations)
        chromosome_lengths.append(i)
        results = _run_trials(parameters, trials)
        completion_times.append(results[0])
        success_rates.append(results[1]*100)

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect of chromosome length on peformance.')
    plt.plot(chromosome_lengths, completion_times, 'b.-', label='time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Chromosome length [bits]')
    plt.plot(chromosome_lengths, success_rates, 'r.-', label='success rate (%)')
    plt.legend()
    
    plt.show(block=False)


def evaluate_population_size(
    start, stop, step, maximum_generations, chromosome_length, trials):

    population_sizes    = []
    completion_times    = []
    success_rates       = []

    for i in range(start, stop, step):
        parameters = Parameters(chromosome_length, i, maximum_generations)
        population_sizes.append(i)
        results = _run_trials(parameters, trials)
        completion_times.append(results[0])
        success_rates.append(results[1]*100)

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect of population size on peformance.')
    plt.plot(population_sizes, completion_times, 'b.-', label='time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Population size [units]')
    plt.plot(population_sizes, success_rates, 'r.-', label='success rate (%)')
    plt.legend()
    
    plt.show(block=False)


def evaluate_maximum_generations(
    start, stop, step, chromosome_length, population_size, trials):

    maximum_generations = []
    completion_times    = []
    success_rates       = []

    for i in range(start, stop, step):
        parameters = Parameters(chromosome_length, population_size, i)
        maximum_generations.append(i)
        results = _run_trials(parameters, trials)
        completion_times.append(results[0])
        success_rates.append(results[1]*100)

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect of maximum generations on peformance.')
    plt.plot(maximum_generations, completion_times, 'b.-', label='time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Maximum generations [units]')
    plt.plot(maximum_generations, success_rates, 'r.-', label='success rate (%)')
    plt.legend()
    
    plt.show(block=False)