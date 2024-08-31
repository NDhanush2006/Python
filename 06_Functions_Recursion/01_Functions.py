"""
Topic :- Functions

Function - Block of statement that performs a speciific task
syntax -  def func_name(parameter1, parameter2..):    <===== Function Definition
                #some work
                return val
          func_name(arg1,arg2..)    #function call --> argument
"""

# Basic Function
def Hello():
    print("hello Dhanush")

Hello()
Hello()
Hello()



# Function Definition
def avg():
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))
    c = int(input("Enter number : "))
    avg = (a+b + c)/ 3
    print(avg)
    return 7
# Function call
result =avg()
# avg()
print(result)


