import random
import numpy as np
import time

import testRun


def init_population(popSize, timesteps):
    population = []

    for _ in range(popSize):
        individual = []
        for i in range(timesteps):
            # Throttle[0, 2], Steering[0, 2], Brake[0 or 1]
            single = [random.randint(-1, 1) + 1, random.randint(-1, 1) + 1, round(random.randint(0, 1))]
            individual.append(single)
        population.append(individual)
    return population

def fitness(individual, timer):
    runSimforTime(timer, individual)
    #Get fitness score from opencav_aeb_genetic.py

def selection(population, fitnesses):
    idx1 = random.randint(0, len(population) - 1)
    idx2 = random.randint(0, len(population) - 1)
    return population[idx1] if fitnesses[idx1] > fitnesses[idx2] else population[idx2]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i][0] = 1 - individual[i][0]  # Flip the bit
            individual[i][1] = 1 - individual[i][1]  # Flip the bit
            individual[i][2] = 1 - individual[i][2]  # Flip the bit
    return individual


def runSimforTime(timer, controls):
    try:
        simRunner = testRun.testRun()

        simRunner.newSim()

        time.sleep(7)

        simRunner.newOpenCAV(controls)

        time.sleep(timer)
    except:
        print("An error occured")
    finally:
        simRunner.killOpenCAV()
        simRunner.killSim()

runSimforTime(10, [[1.5, 1, 0], [1.5, 1.5, 0]])


