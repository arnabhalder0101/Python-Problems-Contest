# Your code here
inp = int(input())

for i in range(2*inp):
    t = i//2

    if t%2==0:
        for j in range(inp):
            if j%2 == 0:
                print("**", end="")
            elif j%2!=0:
                print("..", end="")
        print()
    elif t%2!=0:
        for k in range(inp):
            if k%2 == 0:
                print("..", end="")
            elif k%2!=0:
                print("**", end="")
        print()
