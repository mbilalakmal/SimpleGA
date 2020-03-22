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
    start, stop, step, pop_size, max_gens, trials):

    # calculate number of iterations [performance]
    iterations = (lambda x,y,z: (y-x)//z + ((y-x)%z>0))(start, stop, step)

    chr_lnth  = np.empty((iterations,), dtype=int)
    completion_times = np.empty((iterations,), dtype=float)
    success_rates = np.empty((iterations,), dtype=float)

    for idx, value in enumerate(range(start, stop, step)):
        parameters = Parameters(value, pop_size, max_gens)
        chr_lnth[idx] = value

        results = _run_trials(parameters, trials)
        completion_times[idx] = results[0]
        success_rates[idx] = results[1]

    # convert rates to percentages
    success_rates *= 100

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect Of Chromosome Length On Performance.',
    style='italic', fontsize=14) # title
    
    plt.plot(chr_lnth, completion_times, 'b.-', label='completion time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Chromosome length [bits]')
    plt.plot(chr_lnth, success_rates, 'r.-', label='success rate (%)')
    plt.legend()

    #Show parameters
    plt.suptitle(
        f'Range({start},{stop},{step}) '
        f'| Population: {pop_size} '
        f'| Maximum Generations: {max_gens} '
        f'| Trials: {trials}',
        fontsize=10, fontweight='light', color='brown'
    )
    
    plt.show(block=False)


def evaluate_population_size(
    start, stop, step, max_gens, chr_lnth, trials):

    # calculate number of iterations [performance]
    iterations = (lambda x,y,z: (y-x)//z + ((y-x)%z>0))(start, stop, step)

    pop_size  = np.empty((iterations,), dtype=int)
    completion_times = np.empty((iterations,), dtype=float)
    success_rates = np.empty((iterations,), dtype=float)

    for idx, value in enumerate(range(start, stop, step)):
        parameters = Parameters(chr_lnth, value, max_gens)
        pop_size[idx] = value

        results = _run_trials(parameters, trials)
        completion_times[idx] = results[0]
        success_rates[idx] = results[1]

    # convert rates to percentages
    success_rates *= 100

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect Of Population Size On Peformance.',
    style='italic', fontsize=14) # title

    plt.plot(pop_size, completion_times, 'b.-', label='completion time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Population size [units]')
    plt.plot(pop_size, success_rates, 'r.-', label='success rate (%)')
    plt.legend()
    
    #Show parameters
    plt.suptitle(
        f'Range({start},{stop},{step}) '
        f'| Chromosome Length: {chr_lnth} '
        f'| Maximum Generations: {max_gens} '
        f'| Trials: {trials}',
        fontsize=10, fontweight='light', color='brown'
    )

    plt.show(block=False)


def evaluate_maximum_generations(
    start, stop, step, chr_lnth, pop_size, trials):

    # calculate number of iterations [performance]
    iterations = (lambda x,y,z: (y-x)//z + ((y-x)%z>0))(start, stop, step)

    max_gens  = np.empty((iterations,), dtype=int)
    completion_times = np.empty((iterations,), dtype=float)
    success_rates = np.empty((iterations,), dtype=float)

    for idx, value in enumerate(range(start, stop, step)):
        parameters = Parameters(chr_lnth, pop_size, value)
        max_gens[idx] = value

        results = _run_trials(parameters, trials)
        completion_times[idx] = results[0]
        success_rates[idx] = results[1]

    # convert rates to percentages
    success_rates *= 100

    # plot Completion Times
    plt.subplot(211)
    plt.title('Effect Of Maximum Generations On Peformance.',
    style='italic', fontsize=14) # title

    plt.plot(max_gens, completion_times, 'b.-', label='completion time (s)')
    plt.legend()

    # plot Success Rates
    plt.subplot(212)
    plt.xlabel('Maximum generations [units]')
    plt.plot(max_gens, success_rates, 'r.-', label='success rate (%)')
    plt.legend()
    
    #Show parameters
    plt.suptitle(
        f'Range({start},{stop},{step}) '
        f'| Chromosome Length: {chr_lnth} '
        f'| Population: {pop_size} '
        f'| Trials: {trials}',
        fontsize=10, fontweight='light', color='brown'
    )

    plt.show(block=False)