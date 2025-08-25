# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
def pattern19(n):
    for i in range(n):
        # stars
        for j in range(n-i):
            print('*',end="")

        # spaces
        for j in range(2*i):
            print(" ",end="")

        for j in range(n-i):
            print('*',end="")
        # stars
        print()
        
    for i in range(n):
        # stars (left)
        for j in range(i + 1):
            print('*', end="")

        # spaces (middle)
        for j in range(2 * (n - i - 1)):
            print(" ", end="")

        # stars (right)
        for j in range(i + 1):
            print('*', end="")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    pattern19(n)