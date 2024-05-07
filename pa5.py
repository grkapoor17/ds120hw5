def gcd(a,b):
    if b == 0:
        return a
    else:
        bigger = max(a,b)
        smaller = min(a,b)
        return gcd(smaller, bigger % smaller)

print(gcd(120,80))

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
    

print(remove_pairs("EEWN"))
print(remove_pairs("SSNS"))
print(remove_pairs("ESNW"))
print(remove_pairs("WEWE"))