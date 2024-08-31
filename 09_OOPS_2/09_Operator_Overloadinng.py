class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
n = Number(2)
m = Number(4)

print(n + m)
print(n * m)