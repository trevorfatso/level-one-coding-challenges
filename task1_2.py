def three_in_nums(num1, num2):
    sum_nums = int(num1) + int(num2)
    if num1 == 3 or num2 == 3:
        if '3' in list(str(sum_nums)):
            return True
    else:
        return False