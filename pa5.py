import math

def gcd(a,b):
    if b == 0:
        return a
    else:
        bigger = max(a,b)
        smaller = min(a,b)
        return gcd(smaller, bigger % smaller)

def remove_pairs(path_str):
    if len(path_str) <= 1:
        return path_str
    
    if is_opposite(path_str[0], path_str[1]):
        return remove_pairs(path_str[2:])
    else:
        return path_str[0] + remove_pairs(path_str[1:])

def is_opposite(dir1, dir2):
    if dir1 == "E" and dir2 == "W":
        return True
    if dir1 == "N" and dir2 == "S":
        return True
    if dir1 == "W" and dir2 == "E":
        return True
    if dir1 == "S" and dir2 == "N":
        return True
    else:
        return False

def bisection_root(func, guess1, guess2):
    if abs(func(guess1)) <= 0.001:
        return guess1
    if abs(func(guess2)) <= 0.001:
        return guess2
    if func(guess1) >= 0 and func(guess2) >= 0:
        raise ValueError("Both y-values are the same sign")
    if func(guess1) < 0 and func(guess2) < 0:
        raise ValueError("Both y-values are the same sign")
    
    new_guess = (guess1 + guess2) / 2
    new_y = func(new_guess)

    if (new_y >= 0 and func(guess1) < 0) or (new_y < 0 and func(guess1) >= 0):
        return bisection_root(func, guess1, new_guess)
    elif (new_y >= 0 and func(guess2) < 0) or (new_y < 0 and func(guess2) >= 0):
        return bisection_root(func, new_guess, guess2)
    else:
        raise ValueError("Both y-values are the same sign")