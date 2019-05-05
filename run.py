import numpy as np
import math
import random
import enum

# Ni ovo ne koristim
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


    print('''(1) za tvoje brojeve\n(2) za random brojeve''')
    mode = int(input('Izbor: '))
    if mode == 1:
        l = input('Brojevi sa kojima radim: ')
        goal = int(input('Krajnji rezultat: '))
        num_set = [int(b) for b in l.split()]
    else:
        goal = random.randint(1, 999)
        veci = random.choice(veci)
        srednji = random.choice(srednji)
        mali = random.sample(set(mali), 4)
        
        print(f'Pocinjem.... Brojevi: {mali} {srednji} {veci}')
        print(f'Treba naci: {goal}')

        num_set = mali
        num_set.append(veci)
        num_set.append(srednji)

    # Ne koristim jos
    nb_jedinki = 500    

    for k in range(5):
        pop = []
        best_loss = 0
        best_zapis = ''
        best_j = None
        i = 0
        while best_loss != goal and i < 100000:
            j = random_jedinka(num_set)
            curr_loss, zapis = loss(j)
            if(curr_loss > best_loss and curr_loss <= goal):
                best_j = j
                best_loss = curr_loss
                best_zapis = zapis
            i += 1
        print(f'{k+1}. {best_zapis} = {str(best_loss)}')
                
    

    if(best_loss == goal):
        print('Nasao tacno resnje')
    else:
        print(f'Razlika {goal-best_loss}')