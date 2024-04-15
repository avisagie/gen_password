import secrets
import math

consonants_lower = 'cdfghjklmnpqrstvwxyz'
consonants = consonants_lower.upper() + consonants_lower
vowels_lower = 'aeiouy'
vowels = vowels_lower.upper() + vowels_lower
numbers = '1234567890'
symbols = '!$%^&*-'


def entropy(p: list[int]) -> float:
    return sum(-math.log2(1/l) for l in p)


def gen(nsyllables=4, nsymbols=1, nnumbers=3):
    def add(lengths: list[int], options: str):
        lengths.append(len(options))
        return secrets.choice(options)

    lengths = []
    pwd = ""

    # "syllables"
    for x in range(nsyllables):
        pwd += add(lengths, consonants)
        pwd += add(lengths, vowels_lower)
        pwd += add(lengths, vowels_lower+consonants_lower)

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
