# Write code for algorithm 2 below

def nat_nums(n, i=1):
    if i > n:
        return
    else:
        print(i, end=' ')
        nat_nums(n, i + 1)

nat_nums(3)
