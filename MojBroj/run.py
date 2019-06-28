import numpy as np
import math
import random
import matplotlib.pyplot as plt
# ----------------------- Funkcije za GA -----------------------

ops_signs = ['+', '-', '*', '/', '']
# Upravo sam zavrsio pisanje ove funkcije i odmah zaboravio kako radi tako da jbg
def crossover(h1, h2, num_set):
    ns = num_set[:]
    all_nums = h1[0] + h2[0]
    all_ops = h1[1] + h2[1]
    nb_nums = len(all_nums)
    j = -1
    i = 0
    while (-1*j + i < len(all_nums)):
        if(all_nums[i] in ns):
            ns.remove(all_nums[i])
        else:
            all_nums.remove(all_nums[i])
        if(all_nums[j] in ns):
            ns.remove(all_nums[j])
        else:
            all_nums.remove(all_nums[j])
        i += 1
        j -= 1

    nb_nums = len(all_nums)
    nb_ops = len(all_ops)
    if(nb_nums > nb_ops+1):
        all_nums = all_nums[:-(nb_nums - nb_ops + 1)]

    ops = []
    for i in range(nb_ops):
        if(i % 2 == 0):
            ops.append(all_ops[i])
        else:
            ops.append(all_ops[-i])
    ops = ops[:nb_nums-1]

    return (all_nums, ops)
    

def mutate(h, num_set):
    ns = num_set[:]
    mut_rate = 0.1
    nums = h[0]
    ops = h[1]

    
    for i in nums:
        if i in ns:
            ns.remove(i)
        
    if random.random() <= mut_rate:
        for i in range(len(ops)):
            if random.random() <= mut_rate:
                ops[i] = random.randint(0, 3)

        for i in range(len(nums)):
            if random.random() <= mut_rate:
                el = nums[i]
                if ns:
                    nums[i] = random.choice(ns)
                ns.append(el)
        
    h = nums, ops

def best_2(pop, goal):
    r_pop = pop[:]
    for j in pop:
        l, _ = loss(j)
        if(l > goal):
            r_pop.remove(j)

    r_pop = sorted(r_pop, key = lambda x : loss(x)[0], reverse=True)
    return r_pop[0], r_pop[1]



# --------------------------------------------------------------




# Ako ne upisujemo mi brojeve ovo su liste za random brojeve sa kojima ce da se radi, u sl imamo 4 broja od 1 do 9, jedan od 5 10 15 20 i jedan od 25 50 75 100


# loss predstavlja rezultat jedinke, sto je veci loss to je jedinka bolja, jbg
# racuna se tako sto se svaki broj vezuje za sl operaciju, (1 3 5 10) i (+ - *) ce biti racunati kao (((1)-3)+5)*10
# s je tekstualna reprezentacija jedinke
def loss(jedinka):
    nums = jedinka[0]
    ops = jedinka[1]
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
            s = '(' + s + ')*' + str(nums[i]) if (i > 1) else s + '*' + str(nums[i])
        if ops[i-1] == 3:
            res /= nums[i]
            s = '(' + s + ')/' + str(nums[i]) if (i > 1) else s + '/' + str(nums[i])
    return res, s

# svi je lista brojeva sa moze da se radi, nums je lista brojeva sa kojim jedinka radi, onb_obs je broj operacija u jedinki, ops su operacije
# ops - plus(0), minus(1), puta(2), deljenje(3) 
# jedinka ce da vrati brojeve i operacije, npr brojevi: 1 3 25 a operacije 0 1(+ -)
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

    return (nums, ops)
   

def random_random(num_set, goal):
    print(f'Treba naci: {goal}')
    for k in range(5):
            pop = []
            best_loss = 0
            best_zapis = ''
            best_j = None
            i = 0
            # i < 100000 ako se zaglavi i ne moze da nadje tacno resenje
            while best_loss != goal and i < 100000:
                j = random_jedinka(num_set)
                curr_loss, zapis = loss(j)
                if(curr_loss > best_loss and curr_loss <= goal):
                    best_j = j
                    best_loss = curr_loss
                    best_zapis = zapis
                i += 1
            print(f'{k+1}. {best_zapis} = {str(best_loss)}')
    return best_loss

def random_input():
    ok = True
    try:
        l = input('Brojevi sa kojima radim: ')
        goal = int(input('Krajnji rezultat: '))
        num_set = [int(b) for b in l.split()]
    except:
        print('Unesi lepo podatke, brojeve u obliku \"5 4 1 2 15 50\" a krajnji rezultat \"546\"')
        ok = False 
    if(ok):
        # Nalazi 5 razlicitih nacina kojima dolazi do resenja
        for k in range(5):
            pop = []
            best_loss = 0
            best_zapis = ''
            best_j = None
            i = 0
            # i < 100000 ako se zaglavi i ne moze da nadje tacno resenje
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
    else:
        print('Prekidam!')



# Genetski pravi
def GA(num_set, goal):    
    print(f'Treba naci: {goal}')

    pop_vel, npop_vel = 500, 500
    max_iter = 200
    pop = []
    for _ in range(pop_vel):
        pop.append(random_jedinka(num_set))
    

    t = 0
    best = None
    best_f = 0
    best_s = None
    best_ever_f = None
    best_ever_sol = None
    lista_najboljih = []


    while best_f != goal and t < max_iter:
        n_pop = pop[:]
        while(len(n_pop) < pop_vel+npop_vel) and t < max_iter:
            # h1 = random.choice(pop)
            # h2 = random.choice(pop)
            h1, h2 = best_2(n_pop, goal)
            h3 = crossover(h1, h2, num_set)
            # print(h3[0])
            mutate(h3, num_set)
            if(loss(h3)[0] < goal):
                n_pop.append(h3)
                pop = sorted(n_pop, key = lambda x : loss(x)[0], reverse=True)
                for j in n_pop:
                    l, s = loss(j)
                    if(l > goal):
                        n_pop.remove(j)
            f, s = loss(pop[0])
            if(f > best_f and f <= goal):
                best_s = s
                best_f = f
                best = pop[0]
            t += 1 
    
    print(best_s)
    print(best_f)
    return best_f

# Ovde poredim GA i random, gde random ispada mnogo bolji, za 95% slucajeva nalazi tacan broj
def uporedi():
    ga_rez = []
    random_rez = []
    goals = []
    xs = [i for i in range(10)]
    for i in xs:
        veci = [25, 50, 75, 100]
        srednji = [5, 10, 15, 20]
        mali = [i for i in range(1, 10)]

        goal = random.randint(1, 999)
        veci = random.choice(veci)
        srednji = random.choice(srednji)
        mali = random.sample(set(mali), 4)

        num_set = mali
        num_set.append(veci)
        num_set.append(srednji)

        ga_rez.append(GA(num_set, goal))
        random_rez.append(random_random(num_set, goal))
        goals.append(goal)
        print()

    plt.scatter(xs, goals, c='b')
    plt.plot(xs, ga_rez, c='r', label='GA')
    plt.plot(xs, random_rez, c='g', label='Random')
    plt.legend()
    plt.show()

# 3 opcije - GA, random i input
# svi zahtevaju zahtevaju listu brojeva sa kojima se rade i resenje, npr. [3, 4, 1, 2, 15, 100] i 567
if __name__ == "__main__":
    choice = int(input('(1) custom unos\n(2) random\n(3) GA i random\n'))
    if choice == 1:
        random_input()
    elif choice == 2:
        veci = [25, 50, 75, 100]
        srednji = [5, 10, 15, 20]
        mali = [i for i in range(1, 10)]

        goal = random.randint(1, 999)
        veci = random.choice(veci)
        srednji = random.choice(srednji)
        mali = random.sample(set(mali), 4)

        num_set = mali
        num_set.append(veci)
        num_set.append(srednji)
        random_random(num_set, goal)
    elif choice == 3:
        uporedi()
    else:
        print('...!')
