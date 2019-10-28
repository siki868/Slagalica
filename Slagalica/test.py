import random as rng
import sys
import string
from tqdm import tqdm

goal = input('Goal: ')

def gen_pop(pop_len):
    n = len(goal)
    pop = []
    for i in tqdm(range(pop_len)):
        word = ''.join(rng.choice(string.ascii_lowercase) for _ in range(n))
        pop.append(word)
    return pop

def loss(word):
    l = len(goal)
    for i in range(len(word)):
        if word[i] == goal[i]:
            l -= 1
    l *= 3
    return l

def crossover(h1, h2):
    r = rng.randrange(1, len(h1)-1)
    h3 = h1[:r] + h2[r:]
    h4 = h2[:r] + h1[r:]
    return h3, h4

def mutate(h):
    h = list(h)
    if (rng.random() < 0.02):
        for i in range(len(h)):
            if (rng.random() < 0.1):
                h[i] = rng.choice(string.ascii_lowercase)
    return ''.join(h)
    


if __name__ == "__main__":
    pop_len = int(input('Population: '))
    pop = gen_pop(pop_len)

    max_iter = 5000

    t = 0
    best = None
    best_f = None
    best_ever_f = None
    best_ever_sol = None
    lista_najboljih = []


    while best_f != 0 and t < max_iter:
        n_pop = pop[:]
        while (len(n_pop) < pop_len+len(n_pop)) and t < max_iter:
            h1 = rng.choice(pop)
            h2 = rng.choice(pop)
            h3, h4 = crossover(h1, h2)
            h3 = mutate(h3)
            h4 = mutate(h4)
            n_pop.append(h3)
            n_pop.append(h4)
            pop = sorted(n_pop, key=lambda x : loss(x))
            print(f'{pop[0]}')
            # sys.stdout.write(f'\r{pop[0]}')
            # sys.stdout.flush()
            f = loss(pop[0])
            if best_f is None or best_f > f:
                best_f = f
                best = pop[0]
            t += 1
            if best_ever_f is None or best_ever_f > best_f:
                best_ever_f = best_f
                best_ever_sol = best

