# Course Name: Principles of Programming Languages
# Course Prefix and Number: CS 3210
# Instructor: Dr. Mota
# Student Name: Cameron Jensen


def Exercise():
    source = [2, 3.75, .04, 59, 0.3, 6, 7, 8.5, 9, 10]
    target = [int(x) for x in source]
    print(target)

    divbyseven = [x for x in range(1001) if x%7 == 0]
    print(divbyseven[:11], "...", divbyseven[-10:])

    from itertools import product
    a = list(range(1,10))
    b = [2, 7, 1, 12]
    target = [a+b for (a,b) in product(a, b) if a+b > 10]
    print(a)
    print(b)
    print(target)
    
    print([x for x in range(3,11)])
    print([x for x in range(10,1,-2)])
    print([x**2 for x in range(1,11,3)])


if __name__ == "__main__":
    Exercise()
