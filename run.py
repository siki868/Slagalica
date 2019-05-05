import numpy as np
import math
import random
import enum

class Op(enum.Enum):
    PLUS = 0
    MINUS = 1
    PUTA = 2
    PODELJENO = 3

veci = np.arange(25, 101, 25)
srednji = np.arange(5, 21, 5)
mali = np.arange(1, 10)
ops_signs = ['+', '-', '*', '/', '']


def loss(jedinka):
    nums = jedinka[0]
    ops = jedinka[1]
    nb_ops = len(ops)
    res = nums[0]
    s = str(nums[0])
    for i in range(1, len(nums)):
        if ops[i-1] == 0:
            res += nums[i]
            s += '+' + str(nums[i])
        if ops[i-1] == 1:
            res -= nums[i]
            s += '-' + str(nums[i])
        if ops[i-1] == 2:
            res *= nums[i]
            s = '(' + s + ')*' + str(nums[i]) 
        if ops[i-1] == 3:
            res /= nums[i]
            s = '(' + s + ')/' + str(nums[i])
    return res, s
    

# def zapis(jedinka):
#     global ops_signs
#     nums = jedinka[0]
#     ops = jedinka[1]
#     nb_ops = len(ops)

#     ret = str(nums[0])
#     for i in range(nb_ops):
#         ret += ops_signs[ops[i]] + str(nums[i+1])

#     return ret

def random_jedinka(num_set):
    svi = list(num_set)
    nums = []
    ops = []
    nb_ops = random.randint(1, 5)

    for i in range(nb_ops):
        ops.append(random.randint(0, 3))

    for i in range(nb_ops + 1):
        el = random.choice(svi)
        svi.remove(el)
        nums.append(el)

    return nums, ops
   

if __name__ == "__main__":


    goal = random.randint(1, 999)
    veci = random.choice(veci)
    srednji = random.choice(srednji)
    mali = random.sample(set(mali), 4)
    
    print(f'Pocinjem.... Brojevi: {mali} {srednji} {veci}')
    print(f'Treba naci: {goal}')

    num_set = mali
    num_set.append(veci)
    num_set.append(srednji)


    nb_jedinki = 500
    pop = []
    best_loss = 0
    best_j = None

    # for i in range(9999):
    #     j = random_jedinka(num_set)
    #     curr_loss = loss(j)
    #     if(curr_loss > best_loss and curr_loss <= goal):
    #         best_j = j
    #         best_loss = curr_loss
    #         print(zapis(best_j) + ' = ' + str(best_loss))

    while best_loss != goal:
        j = random_jedinka(num_set)
        curr_loss, zapis = loss(j)
        if(curr_loss > best_loss and curr_loss <= goal):
            best_j = j
            best_loss = curr_loss
            print(zapis + ' = ' + str(best_loss))
    

    if(best_loss == goal):
        print('Nasao tacno resnje')
    else:
        print(f'Razlika {goal-best_loss}')