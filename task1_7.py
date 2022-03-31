def combine(list1, list2):
    n = 1 
    for i in list2:
        list1.insert(n,i)
        n += 2
    return list1