def is_power_of(n,base):
    if n<base:
        return n==1
    return is_power_of(n//base,base)
print(is_power_of(8,2))
print(is_power_of(70,10))