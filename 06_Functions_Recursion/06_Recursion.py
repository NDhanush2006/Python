"""
Topic :- Recursion

Recursion :- A function call itself again and  again

factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X ........3 X 2 X 1

factorial(n) = n * factoria(n-1)

# Basic function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("end")
show(3)  
#output - 3
          2
          1
          End
          end
          end

"""
def show(n):
    if(n == 0):
        return
    else:
        print(n)
        show(n-1)
        print("End")

show(3)
'''
#output - 3
          2
          1
          End
          End
          End
'''
# Recursion Through factorial
def fact(n):
    if(n == 0 or n == 1):
        return 2
    else:
        return n * fact(n-1)
        
    
print(f"Factorial of number is : {fact(5)}")
