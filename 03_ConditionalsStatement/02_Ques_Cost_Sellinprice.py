'''
Topic : if else - Practice Question
'''

cost = int(input("Enter the  Cost Price : "))
sell = int(input("Enter the  Sell Price : "))


# if SP is more than CP -> profit
if sell > cost:
    profit = sell - cost
    print("it is Profit and  we hade made Profit  of Rupees: ", profit ,"Rs")

# if SP is less than CP ->Loss
else:
    loss = cost - sell
    print("it is Loss and Loss of Rupees: ", loss ,"Rs")