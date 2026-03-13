 #Q1 
import random

def f(x):
    return -x**2 + 6*x

x = random.randint(0,6)

print("Initial x:", x)
print("f(x):", f(x))

while True:
    left = x - 1
    right = x + 1

    best_x = x
    best_val = f(x)

    if left >= 0 and f(left) > best_val:
        best_x = left
        best_val = f(left)

    if right <= 6 and f(right) > best_val:
        best_x = right
        best_val = f(right)

    if best_x == x:
        break

    x = best_x
    print("Move to x:", x, "f(x):", f(x))

print("Final Optimal x:", x)
print("Final Optimal value:", f(x))


#Q2

#q2 
goal = 20
beam_width = 2

def heuristic(n):
    return abs(goal - n)

beam = [1]
path = {1:[1]}

while True:
    candidates = []

    for state in beam:
        next_states = [state+2, state+3, state*2]

        for n in next_states:
            candidates.append(n)
            path[n] = path[state] + [n]

    candidates = list(set(candidates))

    candidates.sort(key=lambda x: heuristic(x))

    beam = candidates[:beam_width]

    print("Current Beam:", beam)

    if goal in beam:
        print("Goal reached!")
        print("Path:", path[goal])
        break


#Q3 

import random

POPULATION_SIZE = 10
GENERATIONS = 15
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01
CHROMOSOME_LENGTH = 5 

def fitness(x):
    return x*x + 2*x
def binary_to_int(binary_str):
    return int(binary_str, 2)

def init_population(size):
    return [''.join(random.choice('01') for _ in range(CHROMOSOME_LENGTH)) for _ in range(size)]

def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
   
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness_values):
        current += f
        if current > pick:
            return population[i]
    return population[-1] 

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2

def mutate(chromosome):
    mutated = []
    for bit in chromosome:
        if random.random() < MUTATION_RATE:
            mutated.append('1' if bit == '0' else '0')
        else:
            mutated.append(bit)
    return ''.join(mutated)

def genetic_algorithm():
    population = init_population(POPULATION_SIZE)

    best_overall_chromosome = None
    best_overall_x = None
    best_overall_fitness = -float('inf')

    for generation in range(GENERATIONS):
      
        x_values = [binary_to_int(chromo) for chromo in population]
        fitness_values = [fitness(x) for x in x_values]

        gen_best_fitness = max(fitness_values)
        if gen_best_fitness > best_overall_fitness:
            best_index = fitness_values.index(gen_best_fitness)
            best_overall_chromosome = population[best_index]
            best_overall_x = x_values[best_index]
            best_overall_fitness = gen_best_fitness

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
          
            parent1 = selection(population, fitness_values)
            parent2 = selection(population, fitness_values)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    print("Best chromosome:", best_overall_chromosome)
    print("Best value of x:", best_overall_x)
    print("Best fitness value:", best_overall_fitness)

if __name__ == "__main__":
    random.seed(42)  
    genetic_algorithm()
