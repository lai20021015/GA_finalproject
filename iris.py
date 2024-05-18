#coding=utf-8
import random
import numpy as np
import pandas as pd
import csv

distances = [
    [0, 4.9, 39.0, 39.3, 18.4, 5.9, 23.9, 39.4, 23.1, 15.4],
    [4.9, 0, 43.1, 43.3, 22.4, 10.8, 28.0, 43.5, 27.1, 20.3],
    [39.0, 43.1, 0, 0.2, 17.2, 31.7, 13.3, 1.6, 17.7, 27.0],
    [39.3, 43.3, 0.2, 0, 17.5, 31.9, 13.5, 1.9, 17.9, 27.2],
    [18.4, 22.4, 17.2, 17.5, 0, 16.8, 10.5, 17.8, 15.6, 29.9],
    [5.9, 10.8, 31.7, 31.9, 16.8, 0, 15.1, 32.0, 15.3, 18.0],
    [23.9, 28.0, 13.3, 13.5, 10.5, 15.1, 0, 13.7, 3.1, 14.1],
    [39.4, 43.5, 1.6, 1.9, 17.8, 32.0, 13.7, 0, 18.1, 27.4],
    [23.1, 27.1, 17.7, 17.9, 15.6, 15.3, 3.1, 18.1, 0, 12.7],
    [15.4, 20.3, 27.0, 27.2, 29.9, 18.0, 14.1, 27.4, 12.7, 0]
]

ratings = []

with open('苗栗公館_tour.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        if i >= 0 and i <= 9:  # 第四列的2到11行
            rating = float(row['rating'])  
            ratings.append(rating)
# print(ratings)

# 參數設置
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.1
NUM_SELECTED_SPOTS = 5

# 適應度函數,最大化評分總和並最小化距離總和
def fitness_function(chromosome):
    total_distance = 0
    total_rating = 0
    
    # 計算選擇的景點的評分總和
    for spot in chromosome:
        total_rating += 1 * ratings[spot]
    
    # 計算選擇的景點的距離總和
    start = chromosome[0]
    prev = start
    for current in chromosome[1:] + [start]:
        total_distance += distances[prev][current]
        prev = current
    
    # 適應度函數為評分總和減去距離總和
    return total_rating - total_distance

# 初始化種群
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = random.sample(range(len(distances)), NUM_SELECTED_SPOTS)
        while len(set(chromosome)) != NUM_SELECTED_SPOTS or chromosome in population:
            chromosome = random.sample(range(len(distances)), NUM_SELECTED_SPOTS)
        population.append(chromosome)
    return population

# 選擇父母
def selection(population):
    parents = []
    for _ in range(POPULATION_SIZE // 2):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        if fitness_function(parent1) >= fitness_function(parent2):
            parents.append(parent1)
        else:
            parents.append(parent2)
    return parents

# 交配
def crossover(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1 = list(parent1)
        child2 = list(parent2)
        for j in range(NUM_SELECTED_SPOTS):
            if random.random() < 0.5:
                child1[j], child2[j] = child2[j], child1[j]
        
        # 確保子代不包含重複的景點
        while len(set(child1)) != NUM_SELECTED_SPOTS or child1 in offspring:
            child1 = random.sample(range(len(distances)), NUM_SELECTED_SPOTS)
        while len(set(child2)) != NUM_SELECTED_SPOTS or child2 in offspring:
            child2 = random.sample(range(len(distances)), NUM_SELECTED_SPOTS)
        
        offspring.append(child1)
        offspring.append(child2)
    return offspring

# 突變
def mutation(population):
    for chromosome in population:
        if random.random() < MUTATION_RATE:
            idx1, idx2 = random.sample(range(NUM_SELECTED_SPOTS), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return population

# 主程式
import matplotlib.pyplot as plt

best_list_ex = []

def main():
    population = initialize_population()
    best_fitness_list = []
    maxn = -10e5
    for generation in range(MAX_GENERATIONS):
        parents = selection(population)
        offspring = crossover(parents)
        population = mutation(offspring)
        best_chromosome = max(population, key=fitness_function)
        best_fitness = fitness_function(best_chromosome)
        best_fitness_list.append(best_fitness)
        print(f"Generation {generation}: Best fitness = {best_fitness:.2f}, Best chromosome = {best_chromosome}")
        if(maxn<best_fitness):
            maxn = best_fitness
            best_list_ex = best_chromosome
    plt.plot(range(MAX_GENERATIONS), best_fitness_list)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Best Fitness over Generations')
    plt.show()
    return best_list_ex

best_chromosome = main()
print(f'Best solution: {best_chromosome}')
df = pd.read_csv('苗栗公館_tour.csv')
for i in best_chromosome:
    if(i!=best_chromosome[-1]):
        print(df.iloc[i]['name'], end=' -> ')
    else:
        print(df.iloc[i]['name'])

# print(f"Best solution: {best_chromosome}")