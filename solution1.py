# Write code for algorithm 1 below

def print_numb(n):
    if n < 0:
        return
    else:
        print(n)
        print_numb(n-1)

print_numb(5)

