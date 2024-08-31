'''
Topic : Elif
''''''


Elif - it is called ( else if - Elif)
    syntax of Elif:-
        if condition :
            //statement 1
        elif condition :
            //statement 2
        else condition :
            //statement 3 
'''

cost = int(input("Enter the  Cost Price : "))
sell = int(input("Enter the  Sell Price : "))


# if SP is more than CP -> profit
if sell > cost:
    profit = sell - cost
    print("it is Profit and we hade made Profit of Rupees: ", profit,"Rs")

# if SP is less than CP ->Loss
elif sell < cost:
    loss = cost - sell
    print("it is Loss and Loss of Rupees: ", loss,"Rs")

# if SP is equal to CP -> Neither loss or Profit
else:
    print("Neither loss or Profit")

