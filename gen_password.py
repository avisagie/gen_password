import secrets
import math

consonants = 'cdfghjklmnpqrstvwxyz'
consonants += consonants.upper()
vowels = 'aeiouy'
numbers = '1234567890'
symbols = '!$%^&*-'


def entropy(p: list[int]) -> float:
    entropy = 0.0
    for l in p:
        entropy += -math.log2(1/l)

    return entropy


def gen(nsyllables=4, nsymbols=1, nnumbers=2):
    def add(lengths: list[int], options: str):
        lengths.append(len(options))
        return secrets.choice(options)

    lengths = []
    pwd = ""

    # "syllables"
    for x in range(nsyllables):
        pwd += add(lengths, consonants)
        pwd += add(lengths, vowels)

    # symbol
    for x in range(nsymbols):
        pwd += add(lengths, symbols)

    # some numbers
    for x in range(nnumbers):
        pwd += add(lengths, numbers)

    return pwd, entropy(lengths)


p, entr = gen()
print(f"{p}")
print(f"-> {entr:0.01f} bits")
