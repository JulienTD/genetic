#!/usr/bin/python3

import random

# Characters used to find the string
CHAR_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?,.;/:!'\"\\éèà* 0123456789"

# String to find
STRING_TO_FIND = "test123"

# Max individual in a population
POPULATION_MAX = 100

# Chance of an individual to mutate
CHANCE_TO_MUTATE = 0.1

# Percent of an top-grated individuals to be retained for the next generation
GRADED_RETAIN_PERCENT = 0.2

# Percent of a non top-grated individuals to be retained for the next generation
CHANCE_RETAIN_NONGRATED = 0.05

# Maximum number of generation before stopping the script
GENERATION_COUNT_MAX = 100000

# Individual length
INDIVIDUAL_LENGTH = len(STRING_TO_FIND)

# Maximum fitness
MAXIMUM_FITNESS = len(STRING_TO_FIND)

# Number of top-grated individuals to be retained for the next generation
GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_MAX * GRADED_RETAIN_PERCENT)

# Middle length of the string to find
STRING_TO_FIND_MIDDLE_LENGTH = INDIVIDUAL_LENGTH // 2

# Returns a random char contained in a str
def random_char(str):
    return (str[random.randint(0, len(str) - 1)])

# Generates an individual
def generate_individual():
    individual = []
    for _ in range(INDIVIDUAL_LENGTH):
        individual += random_char(CHAR_LIST)
    return individual

# Generates a population
def generate_population():
    population = []
    for _ in range(POPULATION_MAX):
        population.append(generate_individual())
    return population

# Returns the individual's fitness
def get_individual_fitness(individual):
    fitness = 0
    for c, expected_c in zip(individual, STRING_TO_FIND):
        if c == expected_c:
            fitness += 1
    return fitness

# Calculates the average of population fitness
def average_population_fitness(population):
    total = 0
    for individual in population:
        total += get_individual_fitness(individual)
    return total / POPULATION_MAX

# Sorts population by its fitness
def sort_population_fitness(population):
    sorted_population = []
    for individual in population:
        sorted_population.append((individual, get_individual_fitness(individual)))
    return sorted(sorted_population, key=lambda x: x[1], reverse=True)

# Evolves a population to his next generation
def evolve_population(population):

    # Get individual sorted by grade (top first), the average grade and the solution (if any)
    # To complete

    # End the script when solution is found
    # To complete

    # Filter the top graded individuals
    # To complete

    # Randomly add other individuals to promote genetic diversity
    # To complete

    # Mutate some individuals
    # To complete

    # Crossover parents to create children
    # To complete

    return parents, average_fitness, solution

def main():

    # Create a population and calculate average_fitness
    population = generate_population()
    average_fitness = average_population_fitness(population)
    print("Starting fitness: {0:.2f} / {1:d}".format(average_fitness, MAXIMUM_FITNESS))

    # Make the population evolve
    generation_index = 0
    solution = []
    while len(solution) != POPULATION_MAX and generation_index < GENERATION_COUNT_MAX:
        population, average_fitness, solution = evolve_population(population)
        print("Average fitness: {0:.2f} / {1:d} ({2:d} generation)".format(average_fitness, MAXIMUM_FITNESS, generation_index))
        generation_index += 1

    # Print the final stats
    average_fitness = average_population_fitness(population)
    print("Final fitness: {0:.2f} / {1:d}".format(average_fitness, MAXIMUM_FITNESS))

    # Print the solution
    if solution:
        print("Solution found ({0:d} times) after {1:d} generations.".format(len(solution), generation_index))
    else:
        print("No solution found after {0:d} generations".format(generation_index))

if __name__ == "__main__":
    main()