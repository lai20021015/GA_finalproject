import numpy as np
import math

# ==== 參數設定(與演算法相關) ====

NUM_ITERATION = 3000			# 世代數(迴圈數)

NUM_CHROME = 20             # 染色體個數
NUM_BIT = 2                 # 染色體長度
SIGMA = 0.2                # 生成子代時用到的干擾

np.random.seed(0)          # 若要每次跑得都不一樣的結果，就把這行註解掉

# ==== 基因演算法會用到的函式 ====
def initPop():             # 初始化群體
    # 產生 NUM_CHROME * NUM_BIT 個[-100, 100]之間的隨機數
	return np.random.uniform(low=-32, high=32, size=(NUM_CHROME,NUM_BIT)) 

def fitFunc(x):            # 適應度函數
    sum1 = sum([(x[i]**2)for i in range(NUM_BIT)]) / NUM_BIT
    sum2 = sum([math.cos(2*math.pi*x[i]) for i in range(NUM_BIT)]) / NUM_BIT
    return -(-20*math.exp(-0.2*math.sqrt(sum1)) - math.exp(sum2) + 20 + math.exp(1))

def evaluatePop(p):        # 評估群體之適應度
    return [fitFunc(p[i]) for i in range(len(p))]

def selection(p):          # 隨機找兩個父母
    [i, j] = np.random.choice(NUM_CHROME, 2, replace=False)  # 任選兩個index
    return [p[i], p[j]]

def reproduction(p):       # 繁衍子代
    return [np.random.uniform(np.min([p[0][j], p[1][j]]), np.max([p[0][j], p[1][j]])) \
            + np.random.uniform(low=-SIGMA, high=SIGMA) for j in range(NUM_BIT)]
    
#    kid = []
#    for j in range(NUM_BIT):
#        min_x = np.min([p[0][j], p[1][j]])
#        max_x = np.max([p[0][j], p[1][j]])
#        kid.append(np.random.uniform(min_x, max_x) + np.random.uniform(low=0, high=SIGMA))
#    return kid

def replace(p, p_fit, k, k_fit):            # 適者生存
    worstIndex = np.argmin(p_fit)
    p[worstIndex] = k
    p_fit[worstIndex] = k_fit
    
    return p, p_fit

# ==== 主程式 ====
pop = initPop()             # 初始化 pop
pop_fit = evaluatePop(pop)  # 算 pop 的 fit

for i in range(NUM_ITERATION) :
    parent = selection(pop)                     # 挑父母
    kid = reproduction(parent)                  # 生子
    kid_fit = fitFunc(kid)                      # 算子代的 fit
    pop, pop_fit = replace(pop, pop_fit, kid, kid_fit)    # 取代

    bestIndex = np.argmax(pop_fit)              # 找此世代最佳解的索引值
    print('iteration %d:y = %f'	%(i, pop_fit[bestIndex])) #   x = %s, pop[bestIndex],

