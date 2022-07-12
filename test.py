# prompts the user to enter two numbers
num1 = int(input("Enter a number between 0 and 999: "))
num2 = int(input("Enter another number between 0 and 999: "))

# ones digits
one_num1 = num1%10
ten_num1 = int(str(num1%100)[0])

# tens digits

one_num2 = num2%10
ten_num2 = int(str(num2%100)[0])


# compute sum of ones
sum_of_ones = one_num1 + one_num2

# compute sum of tens
sum_of_tens = ten_num1 + ten_num2

# compute sum of hundreds


print("Sum of ones =       ", one_num1, "+", one_num2, "=", sum_of_ones)
print("Sum of tens =       ", ten_num1, "+", ten_num2, "=", sum_of_tens)