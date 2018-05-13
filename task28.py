

def highest(first, second, third):
    if first > second:
        if second > third:
            return first
        else:
            if third > first:
                return third
            else:
                return first
    else:
        if second > third:
            return second
        else:
            return third


print(str(highest(99, 99, 77)))
