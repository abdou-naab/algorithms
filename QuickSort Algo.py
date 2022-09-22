def qsort(l:list):
    if len(l) <= 1:
        return l
    elif len(l)== 2:
        return l if l[0]<l[1] else l[::-1]
    else:
        pivot=l[0]
        rl=[i for i in l[1:] if i>pivot]
        ll=[i for i in l[1:] if i<=pivot]
        new_array = qsort(ll)+[pivot]+qsort(rl)
        return new_array

test_list = [1,3,5,7,4,8,0,54,3,7,34,2,7,465,674,33,42,2,-43,-4,434,43434,-43656]
print(qsort(test_list))