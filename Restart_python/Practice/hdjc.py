def set_intersection(*sets):
    intersection_set=set.intersection(*sets)
    return intersection_set

set1={1,2,3}
set2={4,5,2}
set3={2,6,5}
obj=set_intersection(set1,set2,set3)
print(obj)
