from collections import Counter
import random

def load_file(file_name):
    ret = []
    with open(file_name, 'r', encoding='utf-8') as f:
        words = f.read().split('\n')
        for w in words:
            ret.append(w.lower())
    return ret

def possible_words(words, chars):
    ret = []
    for word in words:
        all_chars = list(chars)
        rec = list(word)

        for c in word:
            if c in all_chars and c in rec:
                all_chars.remove(c)
                rec.remove(c)

        if not rec:
            ret.append(word)

    return ret



if __name__ == "__main__":
    words = load_file('./hunspell-sr/sr-Latn.dic')

    mode = int(input('(1) za custom slova\n(2) za random slova\nIzbor: '))
    if mode==1:
        sv = input('Slova (trebaju da su u obliku \'abečhtić\'): ')
        slova = list(sv)
        sve_reci = possible_words(words, slova)
        sve_reci.sort(key=lambda x: len(x))
        print(f'Izabrana slova: {slova}')
        print(f'Najduza rec: {sve_reci[-1]}')
    else:
        abeceda = list('abcčćdđefghijklmnoprstšuvzž')
        for _ in range(5):
            random_slova = []
            for _ in range(12):
                random_slova.append(random.choice(abeceda))

            sve_reci = possible_words(words, random_slova)
            sve_reci.sort(key=lambda x: len(x))
            print(f'Izabrana slova: {random_slova}')
            print(f'Najduza rec: {sve_reci[-1]}')