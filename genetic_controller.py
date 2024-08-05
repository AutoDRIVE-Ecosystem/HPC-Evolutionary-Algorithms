import random
import numpy as np
import time
import matplotlib.pyplot as plt

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
    return runSimforTime(timer, individual)
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
    simRunner = testRun.testRun()
    try:

        simRunner.newSim()

        time.sleep(7)

        simRunner.newOpenCAV(controls)

        time.sleep(timer)
    except:
        print("An error occured")
    finally:
        simRunner.killOpenCAV()
        simRunner.killSim()

    return simRunner.fitness

def genetic_algorithm():
    try:
        population = init_population(1000, 1000)
        fitness_history = []
    
        for generation in range(1000):
            fitnesses = [fitness(individual, 1000) for individual in population]
            fitness_history.append(max(fitnesses))  # Track the best fitness in each generation
    
            new_population = []
            for _ in range(1000 // 2):
                parent1 = selection(population, fitnesses)
                parent2 = selection(population, fitnesses)
                child1, child2 = crossover(parent1, parent2)
                new_population.append(mutation(child1, 0.02))
                new_population.append(mutation(child2, 0.02))
    
            population = new_population
    
        return fitness_history
    except KeyboardInterrupt:
        return None


if __name__ == "__main__":
    fitness_history = genetic_algorithm()

    plt.plot(fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Genetic Algorithm Performance')
    plt.show()
