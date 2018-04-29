
a = [1, 1, 2, 3, 5,4,67,21, 8, 13, 21, 34, 55, 89,789]

#returns first and last elements of given list
def boundary(plist):
    return (plist[0], plist[plist.__len__()-1])


print(boundary(a))