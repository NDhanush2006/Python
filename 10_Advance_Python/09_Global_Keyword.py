a = 89


def funct():
    # Local Variable: it can be executed From the inside function
    # global a
    a = 3
    print(a)

# Global Variable : we can Access Everywhere
funct()
print(a)
