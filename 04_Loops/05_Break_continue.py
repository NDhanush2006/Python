'''
Topic : - Break and Continue

Break - used to terminate the loop when encou tered

Continue - terminates execution in the current iteration and continues execution of the loop with the next iteration
'''

# Break - used to terminate the loop when encou tered
'''i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1'''

# Continue - terminates execution in the current iteration and continues execution of the loop with the next iteration
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1

# Pass - Pass is a null statement that does nothing , it is a pacehoder for future code
for i in range(2):
    pass
