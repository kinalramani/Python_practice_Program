def Convert_string(n,base):
    new_str='01132845ABDFC'
    if n<base:
        return new_str[n]
    else:
        return Convert_string(n//base,base)+new_str[n%base]
print(Convert_string(215,2))
