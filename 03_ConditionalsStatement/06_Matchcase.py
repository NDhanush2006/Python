# Q.Making a Calculator using Match Case.

num1 = int(input("Enter num1 value : "))
num2 = int(input("Enter num2 value : "))

operator = input("Enter any operator: ")

match operator:
    case "+":
        print("Sum is : ", num1 + num2)

    case "-":
        print("Difference is : ", num1 - num2)

    case "*":
        print("Product is : ", num1 * num2)

    case "/":
        print("Quotient is : ", num1 / num2)

    case "_":
        print("Enter a  Valid operator")

    