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

    for i in range(1, len(nums)):
        if ops[i-1] == 0:
            res += nums[i]
        if ops[i-1] == 1:
            res -= nums[i]
        if ops[i-1] == 2:
            res *= nums[i]
        if ops[i-1] == 3:
            res /= nums[i]

    return res
    

def zapis(jedinka):
    global ops_signs
    nums = jedinka[0]
    ops = jedinka[1]
    nb_ops = len(ops)

    ret = str(nums[0])
    for i in range(nb_ops):
        ret += ops_signs[ops[i]] + str(nums[i+1])

    return ret

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
    
    num_set = mali
    num_set.append(veci)
    num_set.append(srednji)

    nb_jedinki = 500
    pop = []

    for i in range(10):
        j = random_jedinka(num_set)
        print(zapis(j) + ' = ' + str(loss(j)))
