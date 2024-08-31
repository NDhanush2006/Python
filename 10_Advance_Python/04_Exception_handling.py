'''
#ZeroDivisionerror
a = 0
b = 7
c = b/a --> 7/0 (Error)
print(c)
'''
try:
    a = int(input("Enter: "))
    b = 7/a
    print(b)

# it handle both value and zeroDivisionerror
except ZeroDivisionError:
    print("unexpected Error")

except Exception as e:
    print("Error occured: ", e)

# it handle only value error
except ValueError as e:
    print("Error occured: ", e)

finally:
    print("Always Executed")
