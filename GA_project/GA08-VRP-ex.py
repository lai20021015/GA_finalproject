# 答案 x = [ [0, 8, 6, 2, 5, 0],
#            [0, 7, 1, 4, 3, 0],
#            [0, 9, 10, 16, 14, 0],
#            [0, 12, 11, 15, 13, 0]
# 最佳解 y = 1552

import numpy as np
import math


# ==== 參數設定(與問題相關) ====

NUM_CITY = ?            # 城市個數    # ==== Step 1-1. 設定顧客(城市)個數 ====

# ==== Step 1-2. 設定16個顧客的位置和距離矩陣 ====

# ==== 設定16個顧客的位置 ====
# Type code here

# ==== 設定距離矩陣dist ====
# Type code here

NUM_VEHICLE = ?                        # ==== Step 1-3. 設定車輛個數 ====

# ==== 參數設定(與演算法相關) ====        # ==== Step 4. 調參數 ====

NUM_ITERATION = 100			# 世代數(迴圈數)

NUM_CHROME = 20				   # 染色體個數#
NUM_BIT = NUM_CITY				# 染色體長度    # ==== Step 1-4. 設定bit個數 ====

Pc = 0.5    					# 交配率 (代表共執行Pc*NUM_CHROME/2次交配)
Pm = 0.1   					# 突變率 (代表共要執行Pm*NUM_CHROME*NUM_BIT次突變)

NUM_PARENT = NUM_CHROME                         # 父母的個數
NUM_CROSSOVER = int(Pc * NUM_CHROME / 2)        # 交配的次數
NUM_CROSSOVER_2 = NUM_CROSSOVER*2               # 上數的兩倍
NUM_MUTATION = int(Pm * NUM_CHROME * NUM_BIT)   # 突變的次數

np.random.seed(0)          # 若要每次跑得都不一樣的結果，就把這行註解掉

# ==== 基因演算法會用到的函式 ==== 
def initPop():             # 初始化群體
    p1 = []
    p2 = []
    
    for i in range(NUM_CHROME) :
        # ==== Step 2-1. 產生1~16的隨機排列 ====
        p1.append(np.random.permutation(range(1, NUM_CITY+1)))    # Type code here
        
        # ==== Step 2-2. 產生 2 * NUM_VEHICLE 個(x,y) 隨機座標 ====
        p2.append([np.random.integer(0, 900)for i in range(2*NUM_VEHICLE)])    # Type code here
        
    return p1, p2

def fitFunc(x1, x2):       # 適應度函數    # ==== Step 3. 改適應度函數 ====
    v_dist	= [0, 0, 0, 0]		#用以紀錄4輛車的路徑長
    pre_city	= [0, 0, 0, 0]		#用以紀錄4輛車的目前位置
    for i in range(NUM_BIT):
        j = np.argmin([math.hypot(location[x1[i]][0] - x2[2*k], location[x1[i]][1] - x2[2*k+1]) for k in range(NUM_VEHICLE)])
        v_dist[j] += dist[pre_city[j]][x1[i]]
        pre_city[j] = x1[i]
    
    for i in range(NUM_VEHICLE):
        v_dist[i] += dist[pre_city[i]][0]
    
    return -max(v_dist)           # 因為是最小化問題

def evaluatePop(p1, p2):        # 評估群體之適應度
    return [fitFunc(p1[i], p2[i]) for i in range(len(p1))]

def selection(p1, p2, p_fit):   # 用二元競爭式選擇法來挑父母
    a1 = []
    a2 = []

    for i in range(NUM_PARENT):
        [j, k] = np.random.choice(NUM_CHROME, 2, replace=False)  # 任選兩個index
        if p_fit[j] > p_fit[k] :                      # 擇優
            a1.append(p1[j].copy())
            a2.append(p2[j].copy())
        else:
            a1.append(p1[k].copy())
            a2.append(p2[k].copy())

    return a1, a2

def crossover_uniform(p1, p2):           # 用均勻交配來繁衍子代
    a1 = []
    a2 = []
    
    for i in range(NUM_CROSSOVER) :
        mask1 = np.random.randint(2, size=NUM_BIT)
        mask2 = np.random.randint(2, size=2*NUM_VEHICLE)
       
        [j, k] = np.random.choice(NUM_PARENT, 2, replace=False)  # 任選兩個index
        
        child1, child2 = p1[j].copy(), p1[k].copy()
        remain1, remain2 = list(p1[j].copy()), list(p1[k].copy())     # 存還沒被用掉的城市
       
        for m in range(NUM_BIT):
            if mask1[m] == 1 :
                remain2.remove(child1[m])   # 砍掉 remain2 中的值是 child1[m]
                remain1.remove(child2[m])   # 砍掉 remain1 中的值是 child2[m]
		
        t = 0
        for m in range(NUM_BIT):
            if mask1[m] == 0 :
                child1[m] = remain2[t]
                child2[m] = remain1[t]
                t += 1
        
        a1.append(child1)
        a1.append(child2)
        
        # === for p2 ===
        child3, child4 = p2[j].copy(), p2[k].copy()
       
        for m in range(2*NUM_VEHICLE):
            if mask2[m] == 1 :
                child3[m] = p2[k][m]
                child4[m] = p2[j][m]
        
        a2.append(child3)
        a2.append(child4)

    return a1, a2

def mutation(p1, p2):	           # 突變
    for _ in range(NUM_MUTATION) :
        row = np.random.randint(NUM_CROSSOVER_2)  # 任選一個染色體
        
        if np.random.randint(2) == 0 :
            [j, k] = np.random.choice(NUM_BIT, 2, replace=False)  # 任選兩個基因
      
            p1[row][j], p1[row][k] = p1[row][k], p1[row][j]       # 此染色體的兩基因互換
        else:
            j = np.random.randint(2*NUM_VEHICLE)  # 任選1個基因
            p2[row][j] = np.random.uniform(0, 900)

def sortChrome(a1, a2, a_fit):	    # a的根據a_fit由大排到小
    a_index = range(len(a1))                         # 產生 0, 1, 2, ..., |a|-1 的 list
    
    a_fit, a_index = zip(*sorted(zip(a_fit,a_index), reverse=True)) # a_index 根據 a_fit 的大小由大到小連動的排序
   
    return [a1[i] for i in a_index], [a2[i] for i in a_index], a_fit           # 根據 a_index 的次序來回傳 a，並把對應的 fit 回傳

def replace(p1, p2, p_fit, a1, a2, a_fit):            # 適者生存
    b1 = np.concatenate((p1,a1), axis=0)               # 把本代 p 和子代 a 合併成 b
    b2 = np.concatenate((p2,a2), axis=0)               # 把本代 p 和子代 a 合併成 b
    b_fit = p_fit + a_fit                           # 把上述兩代的 fitness 合併成 b_fit
    
    b1, b2, b_fit = sortChrome(b1, b2, b_fit)                 # b 和 b_fit 連動的排序
    
    return b1[:NUM_CHROME], b2[:NUM_CHROME], list(b_fit[:NUM_CHROME]) # 回傳 NUM_CHROME 個為新的一個世代


# ==== 主程式 ====

pop1, pop2 = initPop()             # 初始化 pop
pop_fit = evaluatePop(pop1, pop2)  # 算 pop 的 fit

best_outputs = []                           # 用此變數來紀錄每一個迴圈的最佳解 (new)
best_outputs.append(np.max(pop_fit))        # 存下初始群體的最佳解

mean_outputs = []                           # 用此變數來紀錄每一個迴圈的平均解 (new)
mean_outputs.append(np.average(pop_fit))        # 存下初始群體的最佳解

for i in range(NUM_ITERATION) :
    parent1, parent2 = selection(pop1, pop2, pop_fit)            # 挑父母
    offspring1, offspring2 = crossover_uniform(parent1, parent2)       # 均勻交配
    mutation(offspring1, offspring2)                            # 突變
    offspring_fit = evaluatePop(offspring1, offspring2)      # 算子代的 fit
    pop1, pop2, pop_fit = replace(pop1, pop2, pop_fit, offspring1, offspring2, offspring_fit)    # 取代

    best_outputs.append(np.max(pop_fit))        # 存下這次的最佳解
    mean_outputs.append(np.average(pop_fit))    # 存下這次的平均解

    if i != NUM_ITERATION-1 :
        print('iteration %d: y = %d'	%(i, -pop_fit[0]))     # fit 改負的
    else:
        print('iteration %d: x1 = %s, x2 = %s, y = %d'	%(i, pop1[0], pop2[0], -pop_fit[0]))     # fit 改負的

# 畫圖
import matplotlib.pyplot
matplotlib.pyplot.plot(best_outputs)
matplotlib.pyplot.plot(mean_outputs)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()