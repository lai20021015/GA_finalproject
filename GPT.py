import numpy as np

# 定義問題相關參數
NUM_CITIES = 10  # 城市數量
NUM_SELECTED = 5  # 選擇的城市數量
POP_SIZE = 100  # 種群大小
MAX_GENERATIONS = 10000  # 最大迭代次數
MUTATION_RATE = 0.1  # 突變率

# 城市距離圖
distances = [
    [0, 1.6, 0.7, 2.0, 0.6, 2.0, 3.4, 1.6, 1.6, 1.6],
    [1.6, 0, 1.1, 0.5, 1.2, 0.5, 2.1, 13, 1.2, 1.5],
    [0.7, 1.1, 0, 1.4, 0.5, 1.4, 2.9, 1.0, 1.4, 1.3],
    [2.0, 0.5, 1.4, 0, 1.5, 14, 2.6, 0.5, 1.4, 1.7],
    [0.6, 1.2, 0.5, 1.5, 0, 1.7, 3.3, 1.4, 1.3, 1.3],
    [2.0, 0.5, 1.4, 14, 1.7, 0, 2.6, 0.5, 1.4, 1.7],
    [3.4, 2.1, 2.9, 2.6, 3.3, 2.6, 0, 2.1, 3.6, 3.5],
    [1.6, 13, 1.0, 0.5, 1.4, 0.5, 2.1, 0, 1.2, 1.5],
    [1.6, 1.2, 1.4, 1.4, 1.3, 1.4, 3.6, 1.2, 0, 0.4],
    [1.6, 1.5, 1.3, 1.7, 1.3, 1.7, 3.5, 1.5, 0.4, 0]
]

# 城市評分
ratings = [4.4, 4.1, 3.6, 4.1, 4.5, 4.1, 4.4, 4.3, 3.7, 4.1]

# 計算適應度函數
def fitness(solution):
    total_distance = 0
    total_rating = 0
    for i in range(len(solution) - 1):
        total_distance += distances[solution[i]][solution[i+1]]
        total_rating += ratings[solution[i]]
    total_rating += ratings[solution[-1]]
    return total_distance - total_rating

# 初始化種群
def init_population():
    return [np.random.permutation(NUM_CITIES) for _ in range(POP_SIZE)]

# 交叉操作
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, NUM_CITIES)
    child1 = np.hstack((parent1[:crossover_point], [city for city in parent2 if city not in parent1[:crossover_point]]))
    child2 = np.hstack((parent2[:crossover_point], [city for city in parent1 if city not in parent2[:crossover_point]]))
    return child1, child2

# 突變操作
def mutate(solution):
    if np.random.rand() < MUTATION_RATE:
        idx1, idx2 = np.random.choice(NUM_CITIES, 2, replace=False)
        solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# 主程式
def main():
    population = init_population()
    for generation in range(MAX_GENERATIONS):
        # 計算適應度
        fitness_scores = [fitness(solution) for solution in population]
        # 選擇
        selected_indices = np.random.choice(range(len(population)), size=NUM_SELECTED, replace=False)
        selected_population = [population[i] for i in selected_indices]
        # 確保選擇的父母數量是偶數
        if len(selected_population) % 2 != 0:
            selected_population.append(population[np.random.randint(len(population))])
        # 交叉和突變
        children = []
        for i in range(0, len(selected_population), 2):
            child1, child2 = crossover(selected_population[i], selected_population[i+1])
            child1 = mutate(child1)
            child2 = mutate(child2)
            children.extend([child1, child2])
        # 更新種群
        population = children
    # 選擇最佳解
    best_solution = min(population, key=fitness)
    print("Best solution:", best_solution)
    print("Fitness:", fitness(best_solution))

if __name__ == "__main__":
    main()