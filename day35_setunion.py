# Enter your code here. Read input from STDIN. Print output to STDOUT
_,n,_,b = (set(input().split()) for _ in range(4))
print(len(n|b))
