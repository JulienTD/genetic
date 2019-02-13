#!/usr/bin/python3

import random

CHAR_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?,.;/:!'\"\\éèà* 0123456789"

STRING_TO_FIND = "test123"

POPULATION_MAX = 100
# Enter here the chance for an individual to mutate (range 0-1)
CHANCE_TO_MUTATE = 0.1

# Enter here the percent of top-grated individuals to be retained for the next generation (range 0-1)
GRADED_RETAIN_PERCENT = 0.2

# Enter here the chance for a non top-grated individual to be retained for the next generation (range 0-1)
CHANCE_RETAIN_NONGRATED = 0.05

# Maximum number of generation before stopping the script
GENERATION_COUNT_MAX = 100000
INDIVIDUAL_LENGTH = len(STRING_TO_FIND)

MAXIMUM_FITNESS = len(STRING_TO_FIND)

# Number of top-grated individuals to be retained for the next generation
GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_MAX * GRADED_RETAIN_PERCENT)

# Precompute the length of the expected string (individual are always fixed size objects)
LENGTH_OF_EXPECTED_STR = len(STRING_TO_FIND)

# Precompute LENGTH_OF_EXPECTED_STR // 2
MIDDLE_LENGTH_OF_EXPECTED_STR = LENGTH_OF_EXPECTED_STR // 2

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


# Sort population by its fitness
def sort_population_fitness(population):
    sorted_population = []
    for individual in population:
        sorted_population.append((individual, get_individual_fitness(individual)))
    return sorted(sorted_population, key=lambda x: x[1], reverse=True)


def evolve_population(population):
    """ Make the given population evolving to his next generation. """

    # Get individual sorted by grade (top first), the average grade and the solution (if any)
    sorted_population = sort_population_fitness(population)
    average_fitness = 0
    solution = []
    graded_population = []
    for individual, fitness in sorted_population:
        average_fitness += fitness
        graded_population.append(individual)
        if fitness == MAXIMUM_FITNESS:
            solution.append(individual)
    average_fitness /= POPULATION_MAX

    # End the script when solution is found
    if len(solution) == POPULATION_MAX:
        return population, average_fitness, solution

    # Filter the top graded individuals
    parents = graded_population[:GRADED_INDIVIDUAL_RETAIN_COUNT]

    # Randomly add other individuals to promote genetic diversity
    for individual in graded_population[GRADED_INDIVIDUAL_RETAIN_COUNT:]:
        if random.random() < CHANCE_RETAIN_NONGRATED:
            parents.append(individual)

    # Mutate some individuals
    for individual in parents:
        if random.random() < CHANCE_TO_MUTATE:
            place_to_modify = random.randint(0, LENGTH_OF_EXPECTED_STR - 1)
            individual[place_to_modify] = random_char(CHAR_LIST)

    # Crossover parents to create children
    parents_len = len(parents)
    desired_len = POPULATION_MAX - parents_len
    children = []
    while len(children) < desired_len:
        father = random_char(parents)
        mother = random_char(parents)
        child = father[:MIDDLE_LENGTH_OF_EXPECTED_STR] + mother[MIDDLE_LENGTH_OF_EXPECTED_STR:]
        children.append(child)

    # The next generation is ready
    parents.extend(children)
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