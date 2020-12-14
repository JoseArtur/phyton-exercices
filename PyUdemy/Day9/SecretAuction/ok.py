def sparse_dot_product(dict1, dict2):
    result = 0
    for k, v in dict1.items():
        if k in dict2:
            result += dict2[k] * v
    return result

def hash_f(n):
    hash = 0
    while n > 0:
        hash += n % 10
        n //= 10
    return hash % 8
 
def collisions(lista):
    x = {}
    for number in lista:
        hash = hash_f(number)
        if hash in x:
            x[hash] += 1
        else:
            x[hash] = 1
    return x


def roman_to_integer(astring):
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    res = 0
    for i, c in enumerate(astring):
        if i < len(astring) - 1 and roman[c] < roman[astring[i + 1]]:
            res -= roman[c]
        else:
            res += roman[c]
    return res


def isomorphic(astring1, astring2):
    # map astring1 to astring2
    d1 = {}
    for i, c in enumerate(astring1):
        if c not in d1:
            d1[c] = astring2[i]
        elif d1[c] != astring2[i]:
            return "'{}' and '{}' are not isomorphic".format(
                    astring1, astring2)
 
    # map astring2 to astring1
    d2 = {}
    for i, c in enumerate(astring2):
        if c not in d2:
            d2[c] = astring1[i]
        elif d2[c] != astring1[i]:
            return "'{}' and '{}' are not isomorphic".format(
                    astring1, astring2)
    # with comprehensions
    # char_pairs = [(k, v) for k, v in d1.items()]
    char_pairs = []
    for k, v in d1.items():
        char_pairs.append((k, v))
    
    return "'{}' and '{}' are isomorphic because we can map: {}".format(
            astring1, astring2, char_pairs)

def logic(s, operations):
    for op, s2 in operations.items():
        if op == 'and':
            s = s.intersection(s2)
        if op == 'or':
            s = s.union(s2)
        if op == 'xor':
            s = s.symmetric_difference(s2)
        if op == 'not':
            s = s2.difference(s)
    return s


