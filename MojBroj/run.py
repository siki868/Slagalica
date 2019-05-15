import numpy as np
import math
import random
import enum

# Ako ne upisujemo mi brojeve ovo su liste za random brojeve sa kojima ce da se radi, u sl imamo 4 broja od 1 do 9, jedan od 5 10 15 20 i jedan od 25 50 75 100
veci = np.arange(25, 101, 25)
srednji = np.arange(5, 21, 5)
mali = np.arange(1, 10)
ops_signs = ['+', '-', '*', '/', '']

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

    return nums, ops
   

if __name__ == "__main__":

    ok = True

    # Za 1 radi sa nasim brojevima a za 2 sastavlja random vrednosti
    print('''(1) za tvoje brojeve\n(2) za random brojeve''')
    mode = int(input('Izbor: '))
    if mode == 1:
        try:
            l = input('Brojevi sa kojima radim: ')
            goal = int(input('Krajnji rezultat: '))
            num_set = [int(b) for b in l.split()]
        except:
            print('Unesi lepo podatke, brojeve u obliku \"5 4 1 2 15 50\" a krajnji rezultat \"546\"')
            ok = False
    elif mode == 2:
        goal = random.randint(1, 999)
        veci = random.choice(veci)
        srednji = random.choice(srednji)
        mali = random.sample(set(mali), 4)
        
        print(f'Pocinjem.... Brojevi: {mali} {srednji} {veci}')
        print(f'Treba naci: {goal}')

        num_set = mali
        num_set.append(veci)
        num_set.append(srednji)
    else:
        print('Opcije su samo 1 ili 2')
        ok = False
    
    if(ok):
        # Ne koristim jos
        nb_jedinki = 500    

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
