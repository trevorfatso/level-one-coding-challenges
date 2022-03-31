def longest(string_array):
    n = 0
    for i in string_array:
        if len(i)>n:
            n = len(i)      
    for x in string_array:
        if len(x) == n:
            print(x) 