def triangle(integer):
    pound = '#'
    n = 1
    x = 0

    if integer > 0:
        for i in pound:
            while n != integer+1:
                print(f'{i*n}')
                n += 1
    else:
        for i in pound:
            integer = integer *-1
            while x != integer+1:
                print(f'{i*(integer-x)}')
                x += 1 