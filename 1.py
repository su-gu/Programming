number1 = float(input("Enter the first number\n"))
number2 = float(input("Enter the second Number\n"))
operator = input("Enter the operator\n")
print((number2+number1) if operator == '+' else number1-number2 if operator == '-' else number1*number2 if operator == '*' else number1/number2 if operator == '/' else 'Enter a correct operator')

