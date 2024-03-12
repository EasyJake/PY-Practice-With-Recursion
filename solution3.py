# Write code for algorithm 3 below

def fibseq(n):
    if n <=1:
        return n
    else:
        return fibseq(n-1) + fibseq(n-2)
    
num = fibseq(9)

print(num)