def multiples_3_5():
    rng = list(range(0,1000))
    multiples = []
    sum_of_multiples = 0
    for i in rng:
        if i%3 == 0:
            multiples.append(i)
        elif i%5 == 0:
            multiples.append(i)
    for i in multiples:
        sum_of_multiples += i
    return sum_of_multiples