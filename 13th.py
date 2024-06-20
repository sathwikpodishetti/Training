def sum_even(x):
    if x==0:
        return 0
    return x+sum_even(x-2)
x=13
if x%2==0:
    print(sum_even(x))
else:
    print(sum_even(x-1))